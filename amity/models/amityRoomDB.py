"""
File      : amityRoomDB.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Deconstracts database model and issues sql syntax

"""

# ============================================================================
# necessary imports
# ============================================================================

from dbConfig import AmityDatabase


class AmityRoomsDB:

    def __init__(self, **kwargs):
        self.dbname = kwargs.get('dbname')
        self.table = kwargs.get('rooms')
        self._db = AmityDatabase(filename=self.dbname, table=self.table)

        self._db.sql_do(
            '''
            CREATE TABLE IF NOT EXISTS {} (
            room_id INTEGER PRIMARY KEY,
            roomname TEXT UNIQUE NOT NULL,
            roomtype TEXT NOT NULL,
            roomspace INTEGER)
            '''.format(
                self.table))

    def insert_room(self, row):
        '''
                inserts new room to database
        '''
        self._db.insert(row)

    def retrive_room(self, key):
        '''
                retrives room record from database using room_id as key
        '''
        return self._db.get_record(key)

    def retrive_rooms(self):
        '''
                retrive all rooms in the database
        '''
        return self._db.get_records()

    def delete_room(self, key):
        '''
                deletes room from database using room_id as key
        '''
        self._db.delete(key)
