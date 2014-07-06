## Openssh-peerbox

Role of Ssh now is to enable controlling the Peerbox and monitoring the state and status of peercoin-daemon until we have more detached solution like web based monitoring I proposed.
Ssh daemon is shaved down, lot's of features removed (kerberos, gssapi, dns) which seemed unnecessary to me.
It comes preconfigured with as much limitations I could think of to maximize the security. 
What is most notable feature is that it is accessible only via local network (192.168.*.*).
