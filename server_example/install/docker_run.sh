#!/bin/sh

DIR=$(pwd)
docker run -p 4050:4050 --name example_server example_server