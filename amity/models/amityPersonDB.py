"""
File      : amityPersonDB.py
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

class AmityPersonDB:

	def __init__(self, **kwargs):
		self.dbname = kwargs.get('dbname')
		self.table = kwargs.get('person')
		self._db = AmityDatabase(filename = self.dbname, table = self.table)

		# try:
		# 	self.con = lite.connect(dbPath)
		# 	print "connection created"
		# except lite.Error, e:

		# 	print "Error %s:" % e.args[0]

		# IF NOT EXISTS

		#self._db.sql_do(' DROP TABLE IF EXISTS {}'.format(self.table))
		self._db.sql_do(' CREATE TABLE IF NOT EXISTS {} (person_id INTEGER PRIMARY KEY, username TEXT NOT NULL, role TEXT NOT NULL, boarding INTEGER NOT NULL, office_allocated INTEGER, accomodation_allocated INTEGER, FOREIGN KEY (y) REFERENCES room(room_id), FOREIGN KEY (accomodation_allocated) REFERENCES room(room_id))'.format(self.table))

	def plain_sql_statement(self, sql, *params):
		self._db.sql_do(sql, params)

	def insert_person(self, row):
		self._db.insert(row)

	def retrive_person(self, key):
		return self._db.getrec(key)

	def retrive_persons(self):
		return self._db.getrecs()

	def update_person(self, key, rec):
		self._db.update(key, rec)