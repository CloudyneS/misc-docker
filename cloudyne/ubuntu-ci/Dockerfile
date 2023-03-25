FROM ubuntu:latest

RUN apt-get -y update && \

    apt-get -y install curl wget git \
        bash sudo net-tools dnsutils \
        gettext-base python3 python3-pip \
        python3-setuptools python3-venv && \

    bash <(curl -fsSl i.v3.nu/kubectl) && \
    bash <(curl -fsSl i.v3.nu/helm) && \
    bash <(curl -fsSl i.v3.nu/azure-cli)