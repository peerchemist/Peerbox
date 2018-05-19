# What is Peerbox?

## Intro

Peerbox is created to address security and privacy concerns regarding using cryptocurrencies.
Security and quality of Peercoin client (or any Bitcoin based client) is not tested enough and is taken for granted. Most crypto coins, the other forks of Bitcoin have wallets that are not being used in the same way as Peercoin's wallet, that is running 0-24h connected to the Internet. They are mined with specialized software, not linked with wallet and thus coins are not exposed to attack as they are simply not connected. These kind of cryptocurrencies, the POW ones, are the most popular cryptocurrencies at the moment, and this approach that takes security and privacy for granted just works for most of people.
Peercoin however utilizes a process called *minting* that requires that wallet is unlocked and then connected to at least 8 peers on the network, each and everyone of those peers now knows the IP of person minting, thus enabling attack vector.
Running full node is even more risky, now you connect to 20-70 peers with port 9901 forwarded. That means this port, on which Peercoin wallet is running is now completely open to anyone on the internet, exposing it to attacker. Knowing this people tend to avoid minting and risk entire network security by doing so. 
One way to solve this is to develop *cold-locked minting* where coins remain encrypted even if in minting mode. So, they are safe even if attacker does succeed and hacks the wallet. In my opinion this is not an elegant solution, as it calls for changing the protocol itself and will probably cost a lot of time to develop and properly test. I do admit that it will ease a lot of minds and persuade them to start minting.
Peerbox is taking a different approach to this, instead of dealing with Peercoin code and protocol it ensures that the underlying OS is secure and limits possible attack vectors. So, it protects the wallet software and thus indirectly coins in it.

Thus, this project's ultimate goal is to provide maximum security platform for minting and running nodes. 
* Security will be enforced by underlying OS, which will be hardened by default to repel most of the attack vectors. 
* Secondary goal of Peerbox is to provide plug&play platform for running Peercoin nodes and to allow safe minting as easily as running a wallet software.

## Design

Peerbox is designed as extension to Debian Linux, as well as the Raspbian - the fork of Debian for Raspberry Pi platform. 

Peerbox platform uses some of well know security philosophies already used in production servers like “principle of least privilege”, limiting every process to as few rights it needs to run along with chrooted environments for essential programs. 

It is very important to have user understand risks and dangers involved with crypto currency. We will try to educate our users and explain what they can do to protect their data and privacy in a world that is becoming increasingly hostile to principles of free speech.

## Vision

Peerbox will deliver same experience on all platforms but focus on cheap, energy efficient devices like Raspberry Pi or Beaglebone Black (Green) which are compatible to general idea of Peercoin in ecological way. Peerbox primary platforms will be those who are cheap and easy to find, as well as recycled computers and parts. Peerbox will compliment Peercoin's goal of providing energy efficient cryptocurrency without need for high end components like GPU's or dedicated mining hardware (ASIC's). 
If ASIC is term for dedicated and energy efficient mining, then Peerbox the is ASIC of PoS.

