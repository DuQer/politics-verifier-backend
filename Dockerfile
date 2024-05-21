FROM jenkins/jenkins:lts-jdk17

USER root
ENV HOME /var/jenkins_home
# Clean lists, update and upgrade
RUN rm -rf /var/lib/apt/lists/* && apt-get update && apt-get upgrade

# Installing build tools for Python
RUN apt-get update && \
    apt-get install -y git ssh tini docker.io wget jq openssl vim gcc make build-essential libssl-dev sudo zlib1g-dev \
    libncurses5-dev libncursesw5-dev libreadline-dev \
    libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev \
    libexpat1-dev liblzma-dev tk-dev libffi-dev liblzma-dev \
    libbz2-dev uuid-dev

# Compile python 3.10.7, crate soft link and rename python3 to python
RUN curl https://pyenv.run/ | bash && ~/.pyenv/bin/pyenv install 3.10.7 && apt-get install python-is-python3

USER root
RUN usermod -aG docker jenkins

USER jenkins
RUN jenkins-plugin-cli --plugins \
  git \
  job-dsl \
  docker-workflow \
  kubernetes \
  workflow-aggregator

USER root
RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
    echo "deb https://ngrok-agent.s3.amazonaws.com/ buster main" | tee /etc/apt/sources.list.d/ngrok.list && \
    apt-get update && \
    apt-get install -y ngrok

RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py --break-system-packages && \
    python -m pip install kybra --break-system-packages

RUN DFX_VERSION=0.19.0 DFXVM_INIT_YES=true sh -ci "$(curl -fsSL https://sdk.dfinity.org/install.sh)"
RUN chown -R jenkins:jenkins /var/jenkins_home/.local
RUN chown -R jenkins:jenkins /var/jenkins_home/.config

USER jenkins

RUN mkdir -p $HOME/.config/dfx/identity/default
RUN openssl ecparam -name secp256k1 -genkey -noout -out $HOME/.config/dfx/identity/default/identity.pem
ENV PATH $PATH:$HOME/.local/share/dfx/bin

USER root
RUN ngrok config add-authtoken 2gHQPy1iOHDoeWKoHFJsWvibPRc_WNVqLFfnf6KbcunRmNrJ

EXPOSE 8080
EXPOSE 50000

USER root
WORKDIR /var/jenkins_home
