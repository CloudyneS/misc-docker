FROM node:lts-bookworm

# Install base packages and azure-cli
RUN apt-get update && \
    
    apt-get -y install curl wget git zip tar \
        bash sudo net-tools dnsutils \
        gettext-base python3 python3-pip \
        python3-setuptools python3-venv && \

    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash && \
    
    apt-get clean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*


# Install kubectl
RUN curl -fsSL "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" -o /tmp/v3-kubectl && \
    sudo install -o root -g root -m 0755 /tmp/v3-kubectl /usr/local/bin/kubectl && \
    sudo bash -c 'kubectl completion bash > /etc/bash_completion.d/kubectl' && \
    echo -e '\nalias k="kubectl"\nalias ksetn="k config set-context --current --namespace"' >> ~/.bash_aliases

# Install Helm
RUN curl -fsSl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | sudo bash

# Add script for uploading files to Azure
COPY ./azure-upload.py /usr/local/bin/azure-upload
COPY ./storage-clone.py /usr/local/bin/storage-clone
COPY ./requirements.txt /tmp/requirements.txt

RUN /usr/bin/python3 -m pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    chmod +x /usr/local/bin/azure-upload /usr/local/bin/storage-clone

ENTRYPOINT [""]
