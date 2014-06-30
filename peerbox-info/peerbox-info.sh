#!/usr/bin/bash 
txtgrn=$(tput setaf 2) # Peer Green
txtylw=$(tput setaf 3) # Coin Yellow
txtrst=$(tput sgr0) # Resets Text
clear
echo
echo ${txtgrn}PeerBox Node Info${txtrst}. ${txtylw}
ppcoind getinfo | grep -vE 'ip|proxy|{|}'
echo ${txtrst}
echo ${txtgrn}Raspberry Pi Info${txtrst}. ${txtylw}
grep 'Hardware\|Serial' /proc/cpuinfo
echo ${txtrst}
