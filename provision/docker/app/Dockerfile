FROM okchaty/python:3.6.5

MAINTAINER Israel Gonzales <@israelgp24>

ARG stage
ARG version

LABEL NAME website-app-$stage
LABEL VERSION $version

COPY ./requirements/ /usr/src/requirements/
COPY ./requirements.txt /usr/src/requirements.txt

# set working directory to /usr/src/
WORKDIR /usr/src/

RUN groupadd -g 500 -r python \
  && groupadd developer \
  && useradd -m -g developer -G python developer \
  && chown -R developer:python /usr/local/bin \
  && mkdir -p /usr/src \
  && chown -R developer /usr/src \
  && apt-get update -y \
  && apt-get install -y gcc libgdal20 libev-dev \
  && pip install -r /usr/src/requirements/$stage.txt \
  && apt-get purge \
  && rm -rf /var/lib/apt/lists/*

