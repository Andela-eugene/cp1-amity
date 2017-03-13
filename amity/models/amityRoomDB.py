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
from dbConfig import AmityDatabase

class AmityRoomsDB:

	def __init__(self, **kwargs):
		self.dbname = kwargs.get('dbname')
		self.table = kwargs.get('rooms')
		self._db = AmityDatabase(filename = self.dbname, table = self.table)

		# try:
		# 	self.con = lite.connect(dbPath)
		# 	print "connection created"
		# except lite.Error, e:

		# 	print "Error %s:" % e.args[0]

		# IF NOT EXISTS

		#self._db.sql_do(' DROP TABLE IF EXISTS {}'.format(self.table))
		self._db.sql_do(' CREATE TABLE IF NOT EXISTS {} (room_id INTEGER PRIMARY KEY, roomname TEXT NOT NULL, roomtype TEXT NOT NULL, roomspace INTEGER)'.format(self.table))

	def plain_sql_statement(self, sql, *params):
		self._db.sql_do(sql, params)

	def insert_room(self, row):
		self._db.insert(row)

	def retrive_room(self, key):
		return self._db.getrec(key)

	def retrive_rooms(self):
		return self._db.getrecs()

	def update_room(self, key, rec):
		self._db.update(key, rec)




