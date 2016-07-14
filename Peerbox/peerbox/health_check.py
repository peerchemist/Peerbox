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

	def api(self):
		api = "https://peercoin.mintr.org/api/block/latest"
		try:
			return json.loads(urllib.urlopen(api).read())
		except:
			print("Can't reach remote API server!")
			return

	def local(self):
		
		local = {}
		local["height"] = int(self.node.getblockcount())
		local["blockhash"] = self.node.getblockhash(local["height"])
		block_info = self.node.getblock(local["blockhash"])

		local["prev_block_hash"] = block_info["previousblockhash"]
		local["merkleroot"] = block_info["merkleroot"]

		return local

	def remote(self):
		a = self.api()

		remote = {
			"height": int(a["height"]),
			"blockhash": a["blockhash"],
			"prev_block_hash": a["previousblockhash"],
			"merkleroot": a["merkleroot"]
		}

		return remote

	def check(self):

		local = self.local()
		remote = self.remote()
		report = {}

		## Block number
		if remote["height"] == local["height"]:
			report["block_count_matches"] = True
		else:
			report["block_count_matches"] = False

		## Hash of the current block
		if remote["blockhash"] == local["blockhash"]:
			report["block_hash_matches"] = True
		else:
			report["block_hash_matches"] = False

		## Hash of previous block
		if remote["prev_block_hash"] == local["prev_block_hash"]:
			report["previous_block_hash_matches"] = True
		else:
			report["previous_block_hash_matches"] = False

		## hash of the MerkleRoot
		if remote["merkleroot"] == local["merkleroot"]:
			report["merkle_root_matches"] = True
		else:
			report["merkle_root_matches"] = False

		return report

