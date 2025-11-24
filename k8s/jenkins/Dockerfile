FROM jenkins/jenkins:lts-jdk17

USER root

# Tools zum Download von kubectl
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Neueste stabile kubectl-Version installieren
RUN KUBECTL_VERSION=$(curl -L -s https://dl.k8s.io/release/stable.txt) \
 && curl -LO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl" \
 && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl \
 && rm kubectl

USER jenkins