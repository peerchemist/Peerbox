#!/bin/bash
# Make sure only root can run our script
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root!" 1>&2
   exit 1
fi

function configure_pam {
	cp /usr/share/pcf/gauth/gauth/pam-sshd.gauth /etc/pam.d/sshd
}

function deconfigure_pam {
	cp /usr/share/pcf/gauth/gauth/pam-sshd.default /etc/pam.d/sshd
}

function configure_sshd {
	sed -i "s/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/g" /etc/ssh/sshd_config
	systemctl reload sshd
}

function deconfigure_sshd {
	sed -i "s/ChallengeResponseAuthentication yes/ChallengeResponseAuthentication no/g" /etc/ssh/sshd_config
	systemctl reload sshd
}

if [[ $1 == "true" ]]; then
	configure_pam
	configure_sshd
	systemctl reload sshd
	echo "Enabled google-authenticator for SSH access." | systemd-cat -t pcf-gauth -p alert
fi

if [[ $1 == "false" ]]; then
	deconfigure_pam
	deconfigure_sshd
	systemctl reload sshd
	echo "Disabled google-authenticator for SSH access." | systemd-cat -t pcf-gauth -p alert
fi

exit