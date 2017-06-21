#!/bin/bash

# Fix user ssh permissions on server

remoteuser=$1
dir="/home/${1}"

# Fix permissions
chmod go-w $dir
chmod 700 "${dir}/.ssh"
# Everyone can read the public keys,
# in order to add them to other services
chmod 644 "${dir}/.ssh/authorized_keys"

# User should own files, not root
chown "${remoteuser}:${remoteuser}" "${dir}/.ssh/authorized_keys"
chown "${remoteuser}:${remoteuser}" "${dir}/.ssh"
chown "${remoteuser}:${remoteuser}" "${dir}"
