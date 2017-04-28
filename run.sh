#!/bin/bash
docker run \
	-p 127.0.0.1:4000:4000 \
	-v $PWD/resources:/application/resources \
	pangolin \
	/application/run.py -d /application/resources/faces
