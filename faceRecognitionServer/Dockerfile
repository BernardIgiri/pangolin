FROM python:3.5-slim

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    python3-pip \
    cmake \
    libboost-python-dev \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN pip3 install --upgrade pip

RUN pip3 install dlib --user

RUN pip3 install face_recognition --user

RUN mkdir -m 770 -p /application/resources

COPY ./src/ /application

EXPOSE 4000
