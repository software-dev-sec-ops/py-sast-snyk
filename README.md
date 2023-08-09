# py-sast-snyk
SAST Demo for Snyk


## Sample API

```
# build local docker image
docker build --no-cache --tag sampleapi -f Dockerfile .

# run docker container
docker run -p 18000:18000 --name demo-api sampleapi:latest

# Silently remove all running containers
docker rm -f $(docker ps -aq)


```





