#!/bin/bash

NAME=cloudowski/flaskdemo

docker build --build-arg SRC=versions/0.1 -t $NAME:0.1 .
docker build --build-arg SRC=versions/0.2 -t $NAME:0.2 .
docker build --build-arg SRC=versions/0.3 -t $NAME:0.3 .
