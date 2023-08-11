# py-sast-snyk
SAST Demo for Snyk


## Sample API


```
# build local docker image
docker build --no-cache --tag sampleapi -f Dockerfile .

# run docker container
docker run -p 18000:18000 --name demo-api sampleapi:latest

# Access API Swagger docs
# http://127.0.0.1:18000/docs/

```

## Postgres db

```
docker exec -it <container_id> /bin/sh -c "psql -U postgres"
```



