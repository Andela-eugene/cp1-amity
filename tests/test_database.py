"""
File      : test_databases.py
Date      : February, 2017
Author    : eugene liyai
Desc      : database test file

"""

# ============================================================================
# necessary imports
# ============================================================================
from unittest import TestCase

from amity.models.amityPersonDB import AmityPersonDB
from amity.models.amityRoomDB import AmityRoomsDB
from amity.person.fellow import Fellow
from amity.person.staff import Staff
from amity.rooms.livingroom import Livingroom


class DatabaseTest(TestCase):

    def setUp(self):

        self.room_db_object = AmityRoomsDB(
            dbname='testDatabase.db', rooms='rooms')
        self.person_db_object = AmityPersonDB(
            dbname='testDatabase.db', person='person')

        self.fellow = Fellow('Mark', 'Bundi')
        self.staff = Staff('Edward', 'Smith')
        self.staff_two = Staff('Frey', 'Michael')
        self.livingroom = Livingroom('occulu')

    def test_add_persons_to_db(self):

        self.person_db_object.insert_person(dict(person_id=self.fellow.get_person_id(), firstname=self.fellow.get_first_name(
        ), lastname=self.fellow.get_last_name(), role=self.fellow.get_role(), boarding=self.fellow.get_boarding()))
        self.person_db_object.insert_person(dict(person_id=self.staff.get_person_id(), firstname=self.staff.get_first_name(
        ), lastname=self.fellow.get_last_name(), role=self.staff.get_role(), boarding=self.staff.get_boarding()))
        self.person_db_object.insert_person(dict(person_id=self.staff_two.get_person_id(), firstname=self.staff_two.get_first_name(
        ), lastname=self.fellow.get_last_name(), role=self.staff_two.get_role(), boarding=self.staff_two.get_boarding()))

        self.assertIsNotNone(self.person_db_object.retrive_persons())

    def test_update_person_in_db(self):
        self.person_db_object.update_person(
            self.fellow.get_person_id(), dict(firstname='Bernard'))
        person_details = [person for person in self.person_db_object.retrive_person(
            self.fellow.get_person_id())]
        self.assertEqual(person_details[0][1], 'Bernard')

    def test_retrive_all_users_from_db(self):
        self.assertGreater(self.person_db_object.retrive_persons(), 1)

    def test_insert_room_in_db(self):
        self.room_db_object.insert_room(dict(room_id=self.livingroom.get_room_id(), roomname=self.livingroom.get_roomname(
        ), roomtype=self.livingroom.get_roomtype(), roomspace=self.livingroom.get_room_space()))
        self.assertIsNotNone(self.room_db_object.retrive_rooms())

    def test_delete_room_in_db(self):
        self.room_db_object.delete_room(self.livingroom.get_room_id())
        room_details = [room for room in self.room_db_object.retrive_room(
            self.livingroom.get_room_id())]
        self.assertEqual(room_details, [])
