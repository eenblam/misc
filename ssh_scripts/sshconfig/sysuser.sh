#!/bin/bash

# Create a new system user
# User may sudo without password, and logs in only via ssh keys

remoteuser=$1

# Disable password because ssh keys
#DEBIAN
#adduser --disabled-password --gecos "" $remoteuser
#CENTOS
useradd -rm $remoteuser # -r create system user; -m create home directory for system user
passwd -l $remoteuser

# Ansible acts as a system user and sudos without password
# (Scripting visudo is a bit of a pain. Thanks stackoverflow/com/questions/323957/)
echo "${remoteuser}	ALL=NOPASSWD: ALL" | (EDITOR="tee -a" visudo);

mkdir -p "/home/${remoteuser}/.ssh"
touch "/home/${remoteuser}/.ssh/authorized_keys"
