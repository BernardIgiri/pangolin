#!/bin/bash
docker run -v $PWD/resources:/application/resources pangolin \
	/application/testRun.py;
