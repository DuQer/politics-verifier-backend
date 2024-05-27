FROM jenkins/jenkins:lts-jdk17

<<<<<<< HEAD
# Your ngrok api key 
ARG NGROK_API_KEY
ARG NGROK_DOMAIN

ENV NGROK_DOMAIN=$NGROK_DOMAIN
# Setting image user to superuser
=======
>>>>>>> parent of 1966bb3 ([FIX] Working Dockerd in Dockerfile)
USER root

# Clean lists, update and upgrade
RUN rm -rf /var/lib/apt/lists/* && apt-get update && apt-get upgrade

# Installing build tools for Python
RUN apt-get update && \
    apt-get install -y git ssh tini docker.io wget jq openssl vim gcc make build-essential libssl-dev sudo zlib1g-dev \
    libncurses5-dev libncursesw5-dev libreadline-dev \
    libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev \
    libexpat1-dev liblzma-dev tk-dev libffi-dev liblzma-dev \
    libbz2-dev uuid-dev libunwind8

# Compile python 3.10.7, crate soft link and rename python3 to python
RUN curl https://pyenv.run/ | bash && ~/.pyenv/bin/pyenv install 3.10.7 && apt-get install python-is-python3

# Changing jenkins membership
USER root
RUN usermod -aG docker jenkins
RUN usermod -aG sudo jenkins

# Jenkins plugins installation
USER jenkins
RUN jenkins-plugin-cli --plugins \
  git \
  job-dsl \
  docker-workflow \
  kubernetes \
  workflow-aggregator

# Ngrok instalation 
USER root
RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
    echo "deb https://ngrok-agent.s3.amazonaws.com/ buster main" | tee /etc/apt/sources.list.d/ngrok.list && \
    apt-get update && \
    apt-get install -y ngrok

# Installing pip and kybra
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py --break-system-packages && \
    python -m pip install kybra --break-system-packages

# Making all members of sudo group capable of using sudo without password
RUN sed -i 's/^%sudo\s\+ALL=(ALL:ALL) ALL/%sudo   ALL=(ALL:ALL) NOPASSWD: ALL/' /etc/sudoers

# Installing dfx and adding it's executable to PATH
USER jenkins
RUN DFXVM_INIT_YES=true sudo -E DFX_VERSION=0.19.0 sh -ci "$(curl -fsSL https://sdk.dfinity.org/install.sh)"
ENV PATH $PATH:/var/jenkins_home/.local/share/dfx/bin
RUN dfxvm default 0.19.0

<<<<<<< HEAD
# Setting ngrok token 
RUN ngrok config add-authtoken $NGROK_API_KEY

RUN cat > /root/.config/dfx/networks.json <<EOF
{
  "local": {
    "bind": "localhost:8000",
    "replica": {
      "subnet_type": "application"
    }
  },
  "ngrok": {
    "providers": [
      "https://$NGROK_DOMAIN"
    ]
  }
}
EOF
=======
# Changing owner of jenkins_home to jenkins and configuring ngrok
USER root
RUN chown -R jenkins:jenkins /var/jenkins_home
RUN ngrok config add-authtoken 2gHQPy1iOHDoeWKoHFJsWvibPRc_WNVqLFfnf6KbcunRmNrJ
>>>>>>> parent of 1966bb3 ([FIX] Working Dockerd in Dockerfile)

# Start script with PID 1 
RUN {\
  echo '#!/bin/bash'; \
  echo 'dfx start --background'; \
  echo 'nohup ngrok http --domain='"$NGROK_DOMAIN"' 8000 &'; \
  echo 'sleep 5'; \
  echo 'URL="$(curl -fs localhost:4040/api/tunnels | jq .tunnels[0].public_url)"'; \
  echo 'echo "Tunneled URL: ${URL:1:-1}"'; \
  echo 'tail -f /dev/null'; \
  } > /root/start.sh && chmod +x /root/start.sh

# Entrypoint 
ENTRYPOINT ["/root/start.sh"]
