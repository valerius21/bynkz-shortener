#!/bin/bash

sudo nvidia-ctk runtime configure --runtime=docker --set-as-default
sudo service docker restart

# install docker-compose
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose version

mkdir -p "$HOME"/webtop
cd "$HOME"/webtop
wget "https://bynkz.com/webtop/docker-compose.yml"
