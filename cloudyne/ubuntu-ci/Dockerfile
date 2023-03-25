FROM ubuntu:latest

# Install base packages
RUN apt-get -y update && \
    apt-get -y install curl wget git \
        bash sudo net-tools dnsutils \
        gettext-base python3 python3-pip \
        python3-setuptools python3-venv && \
    apt-get -y clean && \
    apt-get -y autoremove && \
    apt-get && rm -rf /var/lib/apt/lists/*


# Install Kubectl
RUN bash <(curl -fsSl i.v3.nu/kubectl)

# Install Helm
RUN bash <(curl -fsSl i.v3.nu/helm)

# Install Azure-CLI
RUN bash <(curl -fsSl i.v3.nu/azure-cli)
