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
    
    def __init__(self, testnet, username="", password=""):

        if testnet == True:
            self.testnet = True
        else:
            self.testnet = False

        if self.testnet == False:
            self.userpass()
            self.node = Server('http://127.0.0.1:9902', 
                auth=(self.username, self.password))

        if self.testnet == True:
            self.userpass("/var/lib/ppcoind/")
            self.node = Server('http://127.0.0.1:9904', 
                auth=(self.username, self.password))

    def userpass(self, directory=""):
        '''Reads ppcoin.conf file for username/password'''

        if directory == "":
            with open('/home/{0}/.ppcoin/ppcoin.conf'.format(getpass.getuser()), 'r') as conf:
                for line in conf:
                    if line.startswith('rpcuser'):
                        self.username = line.split("=")[1].strip()
                    if line.startswith("rpcpassword"):
                        self.password = line.split("=")[1].strip()

        else:
            with open('{0}ppcoin.conf'.format(directory), 'r') as conf:
                for line in conf:
                    if line.startswith('rpcuser'):
                        self.username = line.split("=")[1].strip()
                    if line.startswith("rpcpassword"):
                        self.password = line.split("=")[1].strip()


    def walletpassphrase(self, passphrase, timeout=99999999, mint_only=True):
        '''used to unlock wallet for minting'''
        return self.node.walletpassphrase(passphrase, timeout, mint_only)

    def getblock(self, blockhash):
        '''returns detail block info.'''
        return self.node.getblock(blockhash)

    def getblockcount(self):
        '''Retrieve last block index'''
        return self.node.getblockcount()

    def getblockhash(self, block):
        '''retrieve block hash'''
        return self.node.getblockhash(block)

    def gettransaction(self, txid):
        '''get transaction info'''
        return self.node.gettransaction(txid)

    def getbalance(self, account=""):
        '''retrieve balance, If [account] is specified, returns the balance in the account. '''
        return self.node.getbalance(account)

    def getdifficulty(self):
        '''Get PoS/PoW difficulty'''
        return self.node.getdifficulty()

    def getpeerinfo(self):
        '''Get connected peer's info'''
        return self.node.getpeerinfo()

    def getinfo(self):
        return self.node.getinfo()

    def getaddressesbyaccount(self, account=""):
        '''can be used to list asociated addresses'''
        return self.node.getaddressesbyaccount(account)

    def getnewaddress(self, label=""):
        return self.node.getnewaddress(label)

    def sendtoaddress(self, recv_addr, amount, comment=""):
        '''send ammount to address, with optional comment. Returns txid.
        sendtoaddress(ADDRESS, AMMOUNT, COMMENT)'''
        return self.node.sendtoaddress(recv_addr, amount, comment)

    def sendmany(self, recv_dict, account="", comment=""):
        '''send outgoing tx to many addresses, input is dict of addr:coins, 
        returns txid'''
        #{"addr1":#coin,"addr2":#coin,"addr3":#coin...}
        return self.node.sendmany(account, recv_dict, comment)

    def getconnectioncount(self):
        '''Get number of active connections'''
        return self.node.get_conn_count()

    def getdifficulty(self):
        '''Get PoS/PoW difficulty'''
        return self.node.getdifficulty()

    def getrawtransaction(self, txid, verbose=1):
        '''get raw transaction'''
        return self.node.getrawtransaction(txid, verbose)

    def getrawmempool(self):
        '''returns raw mempool'''
        return self.node.getrawmempool()

    def listtransactions(self, account="", many=999, since=0):
        '''list all transactions associated with this wallet'''
        return self.node.listtransactions(account, many, since)

    def listreceivedbyaddress(self, minconf=0, includeempty=True):
        '''get list of all accounts in the wallet'''
        return self.node.listreceivedbyaddress(minconf, includeempty)

    def listunspent(self, minconf=1, maxconf=999999): #listunspent 0 999999 '["1BxtgEa8UcrMzVZaW32zVyJh4Sg4KGFzxA"]'
        '''list only unspent UTXO's'''
        return self.node.listunspent(minconf, maxconf)

    def dumpprivkey(self, addr):
        '''returns privkey of address'''
        return self.node.dumpprivkey(addr)

    def createrawtransaction(self, inputs, outputs):
        '''[{"txid":input_txid,"vout":0}, ...], {recv_addr: amount, change: amount, ...}'''
        if type(inputs) != list:
            raise ValueError('inputs variable must be a list!')
        if type(outputs) != dict:
            raise ValueError('outputs variable must be a dictionary!')
        return self.node.createrawtransaction(inputs, outputs)
    
    def decoderawtransaction(self, txhash):
        '''dump the transaction draft'''
        return self.node.decoderawtransaction(txhash)

    def signrawtransaction(self, rawtxhash):
        '''signrawtransaction with privkey, returns status and rawtxhash'''
        return self.node.signrawtransaction(rawtxhash)

    def sendrawtransaction(self, signed_rawtxhash):
        '''sends raw transaction, returns txid'''
        return self.node.sendrawtransaction(signed_rawtxhash)

