FROM bitnami/kubectl:1.26-debian-11

USER root

RUN apt-get -y update && \
    apt -y install gettext-base && \
    rm -rf /var/cache/apt/archives/*

USER 1001