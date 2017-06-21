#!/bin/bash

# Disable password auth
sed -i '/PasswordAuthentication/c\PasswordAuthentication no' /etc/ssh/sshd_config;
# Lock root out of system
sed -i '/PermitRootLogin/c\PermitRootLogin no' /etc/ssh/sshd_config;

# Restart SSH
#DEBIAN
#systemctl restart ssh.service;
#CENTOS
service sshd restart
