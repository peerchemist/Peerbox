#!/bin/bash

## Reset rules {
iptables --flush
iptables --delete-chain
iptables -X
# }

## Drop all {
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT
#}

## Allow loopback {
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
#}

## Log {
iptables -N logdrop
iptables -A logdrop -m limit --limit 3/m --limit-burst 10 -j LOG
iptables -A logdrop -j DROP
iptables -A INPUT -m conntrack --ctstate INVALID -j logdrop
#}

## Allow established connections {
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
#}

## Allow dhcpc {
iptables -A INPUT -p udp --sport 67 --dport 68 -j ACCEPT
#}

## Allow ICMP packets necessary for MTU path discovery {
iptables -A INPUT -p icmp --icmp-type fragmentation-needed -j ACCEPT
#}

## Allow DNS {
iptables -A INPUT -p tcp -m tcp --dport 53 -j ACCEPT
iptables -A INPUT -p udp -m udp --dport 53 -j ACCEPT
#}

# allow MULTICAST mDNS for service discovery
#both must be uncommented for this to work {
iptables -A INPUT -m state --state NEW -m udp -p udp --dport 5353 -d 224.0.0.251 -j ACCEPT
iptables -A INPUT -p udp -d 239.255.255.250 --dport 1900 -j ACCEPT
#}

## Allow SSH {
# 192.168.0.0/24
iptables -A INPUT -p tcp -s 192.168.0.0/24 -m tcp --dport 22 -j ACCEPT
# 192.168.1.0/24
iptables -A INPUT -p tcp -s 192.168.1.0/24 -m tcp --dport 22 -j ACCEPT
# 10.42.0.0/24
iptables -A INPUT -p tcp -s 10.42.0.0/24 -m tcp --dport 22 -j ACCEPT
#}

## Allow Rsync {
#iptables -A INPUT -p tcp -s 192.168.0.0/24 --dport 873 -m state --state NEW,ESTABLISHED -j ACCEPT
#iptables -A INPUT -p tcp -s 192.168.1.0/24 --dport 873 -m state --state NEW,ESTABLISHED -j ACCEPT
#iptables -A INPUT -p tcp -s 10.42.0.0/24 --dport 873 -m state --state NEW,ESTABLISHED -j ACCEPT
#}

## Allow ppcoind {
iptables -A INPUT -p tcp --dport 9901 -j ACCEPT
#}

## Allow ping from LAN {
iptables -A INPUT -p icmp -s 192.168.0.0/24 --icmp-type echo-request -j ACCEPT
iptables -A INPUT -p icmp -s 192.168.1.0/24 --icmp-type echo-request -j ACCEPT
iptables -A INPUT -p icmp -s 10.42.0.0/24 --icmp-type echo-request -j ACCEPT
#}

## Allow upnp {
# 192.168.0.0/24
iptables -A INPUT -p udp --src 192.168.0.0/24 --sport 1900 -j ACCEPT
# 192.168.1.0/24
iptables -A INPUT -p udp --src 192.168.1.0/24 --sport 1900 -j ACCEPT
# 10.42.0.0/24
iptables -A INPUT -p udp --src 10.42.0.0/24 --sport 1900 -j ACCEPT
#}

## Prevent DoS {
#iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT
#}

## Anti SYN-FLOOD {
iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP
#}

## Reject null packets {
iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP
#}

## Deny all what is not covered above {
iptables -A INPUT -j REJECT --reject-with icmp-port-unreachable
#}
