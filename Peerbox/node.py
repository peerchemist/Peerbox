#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Copyright 2016 Peerchemist
#
# This file is part of Peerbox project.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import os
import getpass
from jsonrpc import Server

class Node:
    
    def __init__(self):
        self.username = ""
        self.password = ""
        self.test = ""
        self.userpass()
        self.testnet()

        if self.testnet == False:
            self.node = Server('http://127.0.0.1:9902', 
                auth=(self.username, self.password))
        else:
            self.node = Server('http://127.0.0.1:9904', 
                auth=(self.username, self.password))

    def userpass(self):
        '''Reads .ppcoin/ppcoin.conf file for username/password'''

        with open('/home/{0}/.ppcoin/ppcoin.conf'.format(getpass.getuser()), 'r') as conf:
            for line in conf:
                if line.startswith('rpcuser'):
                    self.username = line.split("=")[1].strip()
                if line.startswith("rpcpassword"):
                    self.password = line.split("=")[1].strip()

    def testnet(self):
        with open('/home/{0}/.ppcoin/ppcoin.conf'.format(getpass.getuser()), 'r') as conf:
            for line in conf:
                if line.startswith("testnet"):
                    if (line.split("=")[1] == 1 or line.split("=")[1] == True):
                        self.testnet = True
                    else:
                        self.testnet = False
                else:
                    self.testnet = False

    def getblock(self, block):
        '''returns detail block info'''
        return self.node.getblock(block)

    def getblockcount(self):
        '''Retrieve last block index'''
        return self.node.getblockcount()

    def getblockhash(self, block):
        '''retrieve block hash'''
        return self.node.getblockhash(block)

    def getbalance(self):
        '''retrieve balance'''
        return self.node.getbalance()

    def getdifficulty(self):
        '''Get PoS/PoW difficulty'''
        return self.node.getdifficulty()

    def getpeerinfo(self):
        '''Get connected peer's info'''
        return self.node.getpeerinfo()

    def getinfo(self):
        return self.node.getinfo()

    def getaddressesbyaccount(self, account=""):
        '''can be used to list all asociated addresses'''
        return self.node.getaddressesbyaccount(account)

    def createnewaddress(self):
        return self.node.createnewaddress()

    def sendtoaddress(recv_addr, amount, comment=""):
        '''send ammount to address, with optional comment. Returns txid.
        sendtoaddress(ADDRESS, AMMOUNT, COMMENT)'''
        return self.node.sendtoaddress(recv_addr, amount, comment)

    def getconnectioncount(self):
        '''Get number of active connections'''
        return self.node.get_conn_count()

    def getdifficulty(self):
        '''Get PoS/PoW difficulty'''
        return self.node.getdifficulty()

