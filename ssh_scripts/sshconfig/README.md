# Configuring SSH for a new system user
Intended use case:
- New Digital Ocean Debian droplet (support for legacy CentOS releases in comments)
- Droplet should have a copy of your id_rsa.pub for root
- Creates a system user with password-free `sudo`. (**Be careful** and see below.)
- After other scripts complete, root will be locked out,
and password authentication will be revoked for all users.

The reason for doing this is to set up a user for a deployment tool.
Since Python is already available on the target droplet,
this is all that's really necessary to configure the server
in order to carry out the rest of the deployment with Ansible.

Do bear in mind that this script is **not idempotent.**
Run it when you spin up your server, then never again.

## Usage
Setup your DO droplet with your public key, then run `bash ./ssh.sh`.

## Other caveats
Note also that this uses the hostname, not the "Host" alias
that should be used in your `~/.ssh/config`.

Finally, bear in mind that this script is intended to create a system user
that can sudo without a password!
This is a nontrivial security decision to make, so make it carefully.
In practice, you should also create a group with more specific permissions (TODO).
That way, the user can only run the programs it absolutely needs as root.
This script doesn't include that, since it's not clear what programs Ansible will need access to
for your deployment.
