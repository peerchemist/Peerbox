#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sh
from colored import fore, style

def unlock_wallet():

	print
	print(fore.RED + style.BOLD + "WARNING! It is still not recommended to mint coins on Peerbox." + style.RESET)
	print(style.UNDERLINED + "This tool is here mearly to enable faster testing." + style.RESET)
	print

	password = raw_input("Enter wallet password: ")

	try:
		sh.ppcoind("ppcoind walletpassphrase {0} 999999999 true").format(password)
	except:
		print("Something went wrong")

if __name__ == "__main__":

	unlock_wallet()	