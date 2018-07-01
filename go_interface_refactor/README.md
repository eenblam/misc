# Embedding Structs to Satisfy Go Interfaces
I'm currently refactoring a (relatively) small Go application,
which happens to be my first nontrivial project in the language.
One of my main goals is to make a particular type easier to test around.

Currently, an `SSHConnection` type
(which embeds `golang.org/x/crypto/ssh/Client`)
is used to manage SSH connections to devices,
send commands, handle device state, etc.
I want to break the file defining this type out into a subpackage,
turn it into an interface,
create separate implementations for each target device type,
and then create dummy implementations for testing purposes.

`SSHConnection` has a few quirks, though:
- It has too many methods (more than 10) to be a convenient interface.
- Many methods are independent of the target device.
- The other methods accomplish roughly the same task, but for different devices. E.g. switches need to be rebooted after provisioning, but backhaul devices are able to soft-restart, so I have something along the lines of `c.PushNewBackhaulConfig()` and `c.PushNewSwitchConfig()`

I already knew that I can deal with the shared code by embedding a struct type
with the shared methods defined on it in the connection type for each device.
However, I also need to be sure that the connection types each satisfy the
interface I want.
I was happy to find that methods defined on embedded types are promoted to
satisfy interfaces on the embedding type.
This is just a happy discovery about Go,
in which a fairly basic thing clicked into place for me.

See the attached source file for an example of how this works.
