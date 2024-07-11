#!/bin/bash

sudo nvidia-ctk runtime configure --runtime=docker --set-as-default
sudo service docker restart

mkdir -p $HOME/webtop
cd $HOME/webtop
wget "https://gist.githubusercontent.com/valerius21/40d9055856e02f00acdb809ea3b36b5b/raw/d915df2acf81bae9c10c332155279c91164981cb/docker-compose.yml"

docker-compose up -d
cd -