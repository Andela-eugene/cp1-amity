"""
File      : amityRoomDB.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Deconstracts database model and issues sql syntax 

"""

# ============================================================================
# necessary imports
# ============================================================================

import sys, os
import sqlite3
from dbConfig import 

class AmityRoomsDB:

	def __init__(self, **kwargs):
		self.dbname = kwargs.get('amity.db')
		self.table = kwargs.get('rooms')
		self._db = AmityDatabase(filename = self.dbname, table = self.table)

		# try:
		# 	self.con = lite.connect(dbPath)
		# 	print "connection created"ß
		# except lite.Error, e:

		# 	print "Error %s:" % e.args[0]

		self._db.sql_do(' CREATE TABLE IF NOT EXISTS {} (room_id INTEGER PRIMARY KEY)'.format(t))

	def plain_sql_statement(self, sql, *params):
		self._db.sql_do(sql, params)

	def insert_room(self, row):
		self._db.insert(row)

	def retrive_room(self, key):
		return self._db.getrec(key)

	def update_room(self, key, rec):
		self._db.update(key, rec)




