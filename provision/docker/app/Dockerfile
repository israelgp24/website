FROM python:3.6.4

MAINTAINER Israel Gonzales <@israelgp24>

ARG stage
ARG version

LABEL NAME website-app-$stage
LABEL VERSION $version

COPY ./requirements/ /usr/src/requirements/
COPY ./requirements.txt /usr/src/requirements.txt

# set working directory to /usr/src/
WORKDIR /usr/src/

RUN apt-get update -y \
    && apt-get -y install --no-install-recommends binutils libproj-dev gdal-bin \
    # zlib
    zlib1g-dev \
    # bjoern
    libev-dev libevdev2 \
    # install python dependencies
    && pip install -r /usr/src/requirements/$stage.txt \
    && apt-get purge \
    && rm -rf /var/lib/apt/lists/*
