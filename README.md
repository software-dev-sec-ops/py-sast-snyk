# py-sast-snyk
SAST scanning using snyk 
* Containerized fastapi in Python language
* Containerized pyspark application



## Sample API

```
# build local fastapi docker image
docker build --no-cache --tag sampleapi -f Dockerfile.fastapi .

# run docker container
docker-compose up

# stop docker compose
docker-compose down

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

```
docker exec -it <container_id> /bin/sh -c "psql -U postgres"
```




