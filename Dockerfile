FROM bitnami/kubectl:1.26-debian-11

# Add curl and install helm
RUN apt-get update && apt-get -y install curl && \
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 && \
    chmod 700 get_helm.sh && \
    ./get_helm.sh && \
    rm -rf get_helm.sh /var/lib/apt/lists && \
    rm -rf /var/cache/apt/archives/*

# Set empty entrypoint
ENTRYPOINT [""]
