FROM cloudyne/kubectl-envsubst:latest

USER root

RUN apt-get update && apt-get -y install curl && \
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 && \
    chmod 700 get_helm.sh && \
    ./get_helm.sh && \
    rm -rf get_helm.sh /var/cache/apt/archives/* && \
    mkdir /.config /.cache && \
    chown -R 1001:root /.config /.cache && \
    chmod -R 770 /.config /.cache

USER 1001