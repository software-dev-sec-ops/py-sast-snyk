"""
Demo PySpark Application
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, current_timestamp, current_date


def main(spark, **kwargs):
    """Entrypoint"""

    # create sample data
    data = create_sample_data(kwargs["num_records"])

    # create a dataframe
    df = spark.createDataFrame(data)

    # print schema
    print(">>>>>>>>>>> dataframe schema")
    df.printSchema()

    # Perform simple transformation
    final_df = (
        df.withColumn("new_id", col("id") * 1)
        .withColumn("current_ts", current_timestamp())
        .withColumn("current_date", current_date())
    )
    print(">>>>>>>>>>>> final_df.show()")
    final_df.show(truncate=False)

    # write final_df locally
    print(">>>>>>>>>>>> write parquet using final_df")
    final_df.write.format("parquet").mode("overwrite").partitionBy("current_date").save(
        "resources/output/final_df"
    )

    # reading data from postgres_db public.item
    print(">>>>>>>>>>>> Read data from postgres_db from public.item table")
    itemDF = (
        spark.read.format("jdbc")
        .option("url", "jdbc:postgresql://postgres_db:5432/postgres")
        .option("dbtable", "public.item")
        .option("user", "postgres")
        .option("password", "XXXXXX")
        .option("driver", "org.postgresql.Driver")
        .load()
    )

    print(">>>>>>>>>>>>> itemDF.show()")
    itemDF.show(truncate=False)

    # stop spark
    spark.stop()


def setup_spark_session():
    """setup spark session with required configurations

    Returns:
        obj: returns a spark session object
    """
    spark = (
        SparkSession.builder.config(
            "spark.jars", "/opt/pyspark_app/jars/postgresql-42.6.0.jar"
        )
        .appName("Sample PySpark")
        .master("local[*]")
        .getOrCreate()
    )
    # spark version
    print(">>>> Spark Version: {}".format(spark.version))
    # turn off verbose logging
    spark.sparkContext.setLogLevel("ERROR")
    return spark


def create_sample_data(num_records: int = 5) -> list[dict]:
    """generates sample data based on the desired number of records

    Args:
        num_records (int, optional): number of sample records to generate. Defaults to 5.

    Returns:
        list[Item]: returns a list of item dictionary objects
    """
    data = [dict(id=i, desc="item" + str(i)) for i in range(num_records)]
    return data


if __name__ == "__main__":
    spark = setup_spark_session()
    input = dict(num_records=5)
    main(spark, **input)
