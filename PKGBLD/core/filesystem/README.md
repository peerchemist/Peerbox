## filesystem-peerbox


This package defines file located in /etc directory. 
Package is edited upstream ArchLinux filesystem package, it will always keep up with upstream to keep compatibility 
but it will include changes needed for Peerbox.
It is responsible for "hostname", users, groups, fstab, motd greeter and so on.

### /etc/fstab

This file defines partitions to be used by Peerbox.

* /var/lib/ppcoind partition is placed on f2fs fileystem, the flash friendly filesystem by Samsung optimized for flash memory like SD cards.
This will enable SD cards to live longer, by saving writes or optimizing them (f2fs).

* in KVM image /var/lib/ppcoind is placed on ext4 filesystem

* /var/log is placed in tmpfs, a RAM based filesystem

* /tmp is also placed in tmpfs

Moving /var/log and /tmp in RAM is security feature too, when you shut down Peerbox all the logs go to oblivion.
