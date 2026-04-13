# Health Check API

## Description
This REST API returns the state of a given container inside a Docker environment.

## How to Run

**With Python:**
```bash
python3 health_check.py
```

**With Docker:**
```bash
docker run -d \
  --name health-check-api \
  --network portfolio-network \
  -p 5000:5000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  health-check-api
```

## How to Use

```bash
curl http://lopezberg.dev:5000/container-health?container=<container_name>
```
