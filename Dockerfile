FROM bitnami/kubectl:1.26-debian-11

# Install helm
ADD get_helm.sh /get_helm.sh
RUN chmod 700 /get_helm.sh && /get_helm.sh && rm /get_helm.sh

# Set empty entrypoint
ENTRYPOINT [""]

