# Project Pangolin

Tech Demo of face recognition login system using Python, Go, and Docker.

## Pre-requisits
Install Docker

## How to run

First build
```bash
./build.sh
```

Then you can run the image recognition server
```bash
./run.sh
```

Then you need to run the http server (in a separate terminal)
```bash
cd httpRESTServer/
./main
```

Now you can test it by opening the following urls in the browser
```
localhost:8080/compare/barack-obama.jpg/President-Barack-Obama-2014-billboard-650.jpg
```
and
```
localhost:8080/compare/barack-obama.jpg/Official_portrait_of_Vice_President_Joe_Biden.jpg
```

The first should return true and the second should return false. The pictures are in the resources/faces/unknown directory. You can add photos there and test them the same way.

Eventually run.sh will run both servers in docker but that isn't ready yet. For the time being you can shut the servers down with Ctrl+C. Eventually that will be replaced with shutdown.sh
