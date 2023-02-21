FROM bitnami/kubectl:1.26-debian-11

USER root

# Add curl and install helm
RUN apt-get update && apt-get -y install curl && \
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 && \
    chmod 700 get_helm.sh && \
    ./get_helm.sh && \
    rm -rf get_helm.sh /var/lib/apt/lists && \
    rm -rf /var/cache/apt/archives/* && \
    mkdir /.config /.cache && \
    chown -R 1001:root /.config /.cache && \
    chmod -R 770 /.config /.cache

USER 1001

# Set empty entrypoint
ENTRYPOINT [""]