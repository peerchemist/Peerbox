#!/bin/bash
set -e

wget -O - http://peerbox.me/repo/peerbox.gpg.key | sudo apt-key add -
sudo sh -c "echo 'deb http://peerbox.me/repo jessie main' >> /etc/apt/sources.list.d/peerbox.list"
sudo apt-get update && sudo apt-get install -y peerbox
