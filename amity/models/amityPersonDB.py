"""
File      : amityPersonDB.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Deconstracts database model and issues sql syntax

"""

# ============================================================================
# necessary imports
# ============================================================================

import sys
import os
import sqlite3
from dbConfig import AmityDatabase


class AmityPersonDB:

    def __init__(self, **kwargs):
        self.dbname = kwargs.get('dbname')
        self.table = kwargs.get('person')
        self._db = AmityDatabase(filename=self.dbname, table=self.table)

        self._db.sql_do('''
            CREATE TABLE IF NOT EXISTS {}
            (person_id INTEGER PRIMARY KEY,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            role TEXT NOT NULL,
            boarding INTEGER NOT NULL,
            office_allocated INTEGER,
            accomodation_allocated INTEGER,
            FOREIGN KEY (office_allocated) REFERENCES room(room_id),
            FOREIGN KEY (accomodation_allocated) REFERENCES room(room_id))
            '''.format(self.table))

    def plain_sql_statement(self, sql, *params):
        '''
                execute plaun sql statement
        '''
        self._db.sql_do(sql, params)

    def insert_person(self, row):
        '''
                inserts new person to database
        '''
        self._db.insert(row)

    def retrive_person(self, key):
        '''
                retrives person record from database using person_id as key
        '''
        return self._db.get_record(key)

    def retrive_persons(self):
        '''
                retrive all persons in the database
        '''
        return self._db.get_records()

    def update_person(self, key, rec):
        '''
                update a single person in the database using person_id as key
        '''
        self._db.update(key, rec)

    def delete_person(self, key):
        '''
                deletes person from database using person_id as key
        '''
        self._db.delete(key)
