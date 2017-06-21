Assumes root SSH is already configured for password or key access.
(Intended use case is DO droplet created with key for root.)

Assumes private key for root is `id_rsa`.

Note also that this uses the hostname, not the "Host" alias
that should be used in your `~/.ssh/config`.

Finally, bear in mind that this script is intended to create a system user
that can sudo without a password!
This is a nontrivial security decision to make, so make it carefully.
In practice, you should also create a group with more specific permissions.
That way, the user can only run the programs it absolutely needs as root.
