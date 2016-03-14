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

import urllib
import json

class Health:
	'''Checking health of blockchain'''

	def __init__(self, node):
		self.node = node

	def remote(self):
		api = "http://ppc.blockr.io/api/v1/block/info/last"
		try:
			return json.loads(urllib.urlopen(api).read())
		except:
			print("Can't reach remote API server!")
			return

	def local(self):
		
		local = {}
		local["height"] = self.node.getblockcount()
		local["hash"] = self.node.getblockhash(local["height"])
		block_info = self.node.getblock(local["hash"])

		local["prevHash"] = block_info["previousblockhash"]
		local["mrkRoot"] = block_info["merkleroot"]

		return local

	def check(self):

		local = self.local()
		remote = self.remote()["data"]
		report = {}

		## Block number
		if remote["nb"] == local["height"]:
			report["block_count_matches"] = True
		else:
			report["block_count_matches"] = False

		## Hash of the current block
		if remote["hash"] == local["hash"]:
			report["last_block_hash_matches"] = True
		else:
			report["last_block_hash_matches"] = False

		## Hash of previous block
		if remote["prev_block_hash"] == local["prevHash"]:
			report["previous_block_hash_matches"] = True
		else:
			report["previous_block_hash_matches"] = False

		## hash of the MerkleRoot
		if remote["merkleroot"] == local["mrkRoot"]:
			report["merkle_root_matches"] = True
		else:
			report["merkle_root_matches"] = False

		return report

