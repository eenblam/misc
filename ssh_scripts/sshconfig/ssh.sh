#!/bin/bash

remoteuser=$1
hostname=$2
host=$3
keyname="${3}-${1}"

# Set up remote system user
ssh root@${hostname} "bash -s" < ./sysuser.sh "$remoteuser"

# Create remote key
ssh-keygen -f "${HOME}/.ssh/${keyname}"
# Local permissions
chmod 700 ~/.ssh && chmod 600 ~/.ssh/* && chmod 644 ~/.ssh/*.pub

# Add user's key as root (user has no permissions)
cat ~/.ssh/${keyname}.pub | ssh root@${hostname} "cat >> /home/${remoteuser}/.ssh/authorized_keys"
# Fix remote permissions for user
ssh root@${hostname} "bash -s" < ./userpermissions.sh "${remoteuser}"

# Disable all root access and general ssh password access
ssh root@${hostname} "bash -s" < ./lockout.sh
