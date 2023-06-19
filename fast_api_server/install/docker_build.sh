#!/bin/sh
docker build -t fastapi-server  -f fast_api_server/install/Dockerfile .

# docker build -t fastapi-server .