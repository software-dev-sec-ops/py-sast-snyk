# A sample PySpark Application

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, current_timestamp, current_date


def main():
    """
    Main function
    """
    # create a spark session
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

    # create sample data
    data = [
        {"id": 1, "desc": "item1"},
        {"id": 2, "desc": "item2"},
        {"id": 3, "desc": "item3"},
        {"id": 4, "desc": "item4"},
        {"id": 5, "desc": "item5"},
    ]

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


if __name__ == "__main__":
    main()
