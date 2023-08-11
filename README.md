# py-sast-snyk
SAST scanning using snyk 
* Containerized fastapi in Python language
* Containerized pyspark application


# Snyk SAST scans

Read [here](docs/snyk_setup.md)

## Developer Setup

### Pre-requisites

* docker desktop installed on local machine

```
# run docker container
docker-compose up --build # build is first time only

# stop docker compose
docker-compose down

# access postgres db
docker exec -it <container_id> /bin/sh -c "psql -U postgres"
```

### Output

**docker-compose up**
![docker compose up](docs/images/docker_compose_up.png)

**fast API**
Access API Swagger docs [here](http://127.0.0.1:18000/docs/)
![fast api swagger docs](docs/images/fast_api_swagger.png)

**Postgres db**
![postgres db](docs/images/postgres_db.png)

**Pyspark Application**
![pyspark app](docs/images/pyspark_app.png)




