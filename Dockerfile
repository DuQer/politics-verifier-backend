# Debian with appropriate version of GNU Lib C (GLIBC_2.32)
FROM debian:bookworm-20240513

# Your ngrok api key 
ARG NGROK_API_KEY
ARG NGROK_DOMAIN

ENV NGROK_DOMAIN=$NGROK_DOMAIN
# Setting image user to superuser
USER root

# Setting workdir to /root, as /root is root home 
WORKDIR /root
ENV HOME /root

# Dependencies and tools instalations
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    jq \
    git \
    gnupg \
    gpg \
    libfontconfig1 \
    libfreetype6 \
    procps \
    ssh-client \
    unzip \
    tzdata \
    ssh \
    wget \
    vim \
    gcc \
    make \
    build-essential \
    libunwind8 \
    zlib1g-dev \
    openssl \
    bzip2 \
    libffi-dev \
    libbz2-dev \ 
    libncurses5-dev \
    libreadline-dev \
    libssl-dev \
    libsqlite3-dev \
    liblzma-dev \
  && apt-get update && apt-get upgrade && rm -rf /var/lib/apt/lists/*

# Compiling python 3.10.7
RUN curl https://pyenv.run/ | bash && ~/.pyenv/bin/pyenv install 3.10.7
ENV PATH=$PATH:$HOME/.pyenv/versions/3.10.7/bin

# Adding ngrok repository and intalling it (for canister tunneling)
RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
    echo "deb https://ngrok-agent.s3.amazonaws.com/ buster main" | tee /etc/apt/sources.list.d/ngrok.list && \
    apt-get update && \
    apt-get install -y ngrok

# Installig pip and kybra (for canisters deployment)
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py --break-system-packages && \
    python -m pip install kybra --break-system-packages

# DFX installation and setting default version
RUN DFXVM_INIT_YES=true DFX_VERSION=0.19.0 sh -ci "$(curl -fsSL https://sdk.dfinity.org/install.sh)"
ENV PATH $PATH:$HOME/.local/share/dfx/bin
RUN dfxvm default 0.19.0

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


