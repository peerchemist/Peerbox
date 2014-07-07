You can support this repo via peer4commit.
[![tip for next commit](http://peer4commit.com/projects/92.svg)](http://peer4commit.com/projects/92)

# What is Peerbox?

## Intro

Security and quality of Peercoin client (or any Bitcoin based client) is not tested enough. Most coins (the other forks of Bitcoin) wallet's are not being used in this way (running 0-24 with coins inside). They are mined with specialized software, not linked with wallet.
Peercoin minting requires that wallet is unlocked and then connected to 8 peers on the network, each and everyone of those peers now know IP of person minting, thus enabling attack vector.
Running full node is even more risky, now you connect to 20-70 peers and with port 9901 forwarded. That means this port, on which Peercoin wallet is running is now completely open to anyone on the internet, exposing it to attacker.
Due to this, people avoid minting and risk entire network security by doing so. 

This project's goal is to provide maximum security platform for minting and running nodes. Security will be enforced by underlying OS, which will be hardened to repel most of the attack vectors.
Secondary goal of Peerbox is to provide plug&play platform for running Peercoin nodes and to allow safe minting as easily as running a wallet software.

## Design

Peerbox is designed as extension to Arch Linux, well know Linux distribution which focuses on minimalism and simplicity. An ideal distribution to shape to our needs. What is important, Arch Linux provides very simple solution for building packages, it's PKGBUILD scripts allow anyone to compile the entire OS themselves with ease. Best of all, Arch Linux runs on various hardware, starting from high end servers to simple Raspberry Pi, and everything in between.

Peerbox platform uses some of well know security philosophies already used in production servers like “principle of least privilege”, limiting every process to as few right it needs to run along with chrooted environments for essential programs. 
Beside that, system will employ Grsecurity patches for Linux kernel. Grsecurity is an extensive security enhancement to the Linux kernel that defends against a wide range of security threats through intelligent access control, memory corruption-based exploit prevention, and mandatory access control (MAC). A major component of Grsecurity is its approach to memory corruption vulnerabilities and their associated exploit vectors, which is extremely important to Peercoin since it is coded in C++, a programming language well know for memory corruption vulnerabilities.

Peerbox pules packages from upstream Arch Linux repository and pre-configures them to our needs. With dedicated package and git repository so anyone can inspect and build packages them selves, and contribute if they notice something is wrong or just feel like there is better approach. 
It is very important to have user understand risks and dangers involved with crypto currency. We will try to educate our users and explain what can they do to protect their data and privacy in a world that is becoming increasingly hostile to principles of free speech.

## Vision

Peerbox will deliver same experience on all platforms but focus on cheap, energy efficient devices like Raspberry Pi or Beaglebone Black which are compatible to general idea of Peercoin in ecological way. Providing energy efficient crypto currency without need for high end components like GPU's or dedicated mining hardware (ASIC's). If ASIC is term for dedicated and energy efficient mining, then this is ASIC of PoS.

