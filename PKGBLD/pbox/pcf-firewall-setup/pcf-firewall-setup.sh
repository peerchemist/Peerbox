#!/bin/bash

## Alternate approach: get default route first
#ip route show default | awk '/default/ {print $3}'

## Get default route
function local_ip {
	ip route get "$(ip route show to 0/0 | grep -oP '(?<=via )\S+')" | grep -oP '(?<=src )\S+'
}

function join { 
	local IFS="$1"; shift; echo "$*"; 
}

function get_subnet {
	string=$(local_ip)
	arr=(${string//./ })
	arr[3]=0
	subnet="$(join . "${arr[@]}")"
}

function write_changes {
	cp /usr/share/pcf/firewall/iptables.rules.template /etc/iptables/iptables.rules
	sed -i "s/<SUBNET>/"${subnet}"/g" /etc/iptables/iptables.rules
	touch /etc/pcf/firewall/.lock
}

function log_to_systemd {
	echo "Got subnet address:" $1 | systemd-cat -t pcf-firwall-setup -p notice
	echo "Allowing connections from:" $1/24 | systemd-cat -t pcf-firwall-setup -p alert
}

get_subnet
write_changes
log_to_systemd $subnet

exit
