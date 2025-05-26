FROM jenkins/jenkins:2.492.3-lts-jdk17

USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends docker.io && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER jenkins
