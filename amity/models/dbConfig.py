"""
File      : database.py
Date      : February, 2017
Author    : eugene liyai
Desc      : database model class that connects and persists data to database

"""

# ============================================================================
# necessary imports
# ============================================================================

import sqlite3

class AmityDatabase:

	def __init__(self, **kwargs):

		'''
			db = AmityDatabase([table = ""][ filename=""])
			constructor method that implements CRUD operations
			filename is for connecting to database file
		'''

		self._db = sqlite3.connect('filename')
		self._dbFilename = 'filename'
		self.filename = kwargs.get('filename')
		self.table = kwargs.get('table', '')

	def sql_do(self, sql, params = ()):
		'''
			db.sql_do(sql[, params])
			method for non-select queries
				sql is string containing SQL syntax
				params is list containing parameters

			mehod returns nothing
		'''

		self._db.execute(sql, params)
		self._db.commit()


	# ============================================================================
	# query the database
	# ============================================================================
	def sql_query(self, sql, params = ()):
		'''
			db.sql_query(sql[, params])
			generator method for queries
				sql is string containing SQL syntax
				params is list containing parameters
			return generator with one row per iteration
			each row is a Row Factory
		'''

		c = self._db.cursor()
		c.execute(sql, params)
		for r in c:
			yield r

	# ============================================================================
	# query a row in the database
	# ============================================================================
	def sql_query_row(self, sql, params = ()):
		'''
			db.sql_query_row(sql[, params])
			query for a single row
				sql is string containing SQL syntax
				params is list containing parameters
			return single row from a Row Factory
		'''

		c = self._db.cursor()
		c.execute(sql, params)
		return c.fetchone()

	# ============================================================================
	# query a single value in the database
	# ============================================================================
	def sql_query_value(self, sql, params = ()):
		'''
			db.sql_query_row(sql[, params])
			query for a single value
				sql is string containing SQL syntax
				params is list containing parameters
			return single value
		'''

		c = self._db.cursor()
		c.execute(sql, params)
		return c.fetchone()[0]

	# ============================================================================
	# query a single record in the database
	# ============================================================================
	def getrec(self, id):
		'''
			db.getrec(id)
			get a single row by id
		'''

		query = 'SELECT * FROM {} WHERE id =?'.format(self.table)
		c = self._db.execute(query, (id,))
		for r in c:
			yield r

	# ============================================================================
	# query all rows
	# ============================================================================
	def getrecs(self):
		'''
			db.getrecs()
			get all rows, returns a generator of Row factories
		'''

		query = 'SELECT * FROM {}'.format(self.table)
		c = self._db.execute(query)
		for r in c:
			yield r

	# ============================================================================
	# insert a single value in the database
	# ============================================================================
	def insert(self, rec):
		'''
			db.insert(rec)
			insert a single record into the table
				rec is a dictonary key/value pairs corresponding to table schema
			omit id column to let SQLite generate it
		'''

		klist = sorted(rec.keys())

		# List of values ordered by key
		values = [ rec[v] for v in klist]
		q = 'INSERT INTO {} ({}) VALUES ({})'.format(
				self.table,
				', '.join(klist),
				', '.join('?' for i in range(len(values)))
			)
		c = self._db.execute(q, values)
		self._db.commit()
		return c.lastrowid

	# ============================================================================
	# update a single value/record in the database
	# ============================================================================
	def update(self, id, rec):
		'''
			db.update(id, rec)
			update a row in the table
				id is the value of the id column for the row to be updated
				rec is the dict with key/value pairs corresponding to the table schema
		'''

		klist = sorted(rec.keys())

		# List of values ordered by key
		values = [ rec[v] for v in klist]

		for i, k in enumerate(klist):
			if k == 'id':
				del klist[i]
				del values[i]

		q = 'UPDATE {} SET {} WHERE id =?'.format(
				self.table,
				', '.join(map(lambda str: '{} = ?'.format(str), klist))
			)

		self._db.execute(q, values + [id])
		self._db.commit()


	# ============================================================================
	# delete a single record in the database
	# ============================================================================
	def delete(self, id):
		'''
			db.delete(id)
			delete a row from the table, by id
		'''

		query = 'DELETE FROM {} WHERE id=?'.format(self.table)
		self._db.execute(query, [id])
		self._db.commit()

	# ============================================================================
	# count the records in the table
	# ============================================================================
	def countrecs(self):
		'''
			db.countrecs()
			count the records in the table
			return a single integer value
		'''

		query = 'SELECT COUNT(*) FROM {}'.format(self.table)
		c = self._db.cursor()
		c.execute(query)
		return c.fetchone()[0]

	### Filename property
	@property
	def filename(self):
		return self._dbFilename

	@filename.setter
	def filename(self, fn):
		# self._dbFilename = fn
		# self._db = sqlite3.connect(fn)
		self._db.row_factory = sqlite3.Row

	@filename.deleter
	def filename(self):
		self.close()

	# ============================================================================
	# Diconnect database
	# ============================================================================ 
	def close(self):
		self._db.close()
		del self._dbFilename


# ============================================================================
# test db connection and operations
# ============================================================================
def test():
	import os
	fn = ':memory:'		# in-memory database
	t = 'foo'

	recs = [
		dict(string = 'one'),
		dict(string = 'two'),
		dict(string = 'three')
	]

	print 'Create database file {} ...'.format(fn)
	db = AmityDatabase(filename = fn, table = t)
	print 'Done.'

	print 'Creating table .....'
	db.sql_do(' DROP TABLE IF EXISTS {}'.format(t))
	db.sql_do(' CREATE TABLE {} (id INTEGER PRIMARY KEY, String TEXT) '.format(t))
	print 'Done.'

	print 'Insert into table ... '
	for r in recs:
		db.insert(r)
	print 'Done.'

	print 'Read from table'
	for r in db.getrecs(): 
		print r

	print 'Update table'
	db.update(2, dict(string = 'TWO'))
	print dict(db.getrec(2))

	print 'Insert an extra row ... '
	newid = db.insert(dict(string = 'extra'))
	print '(id is {})'.format(newid)
	print dict(db.getrec(newid))
	print 'Now delete it'
	db.delete(newid)
	for r in db.getrecs(): print r
	db.close()

if __name__ == '__main__':
	test ()