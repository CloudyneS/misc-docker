FROM bitnami/kubectl:1.26-debian-11

# Install helm
RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 \
    && chmod 700 get_helm.sh \
    && ./get_helm.sh

# Set empty entrypoint
ENTRYPOINT [""]

