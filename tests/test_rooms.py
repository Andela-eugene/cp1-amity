"""
File      : rooms_test.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Room test file

"""


# ============================================================================
# necessary imports
# ============================================================================

from unittest import TestCase
from amity.rooms.office import Office
from amity.rooms.livingroom import Livingroom


class RoomTest(TestCase):

    def setUp(self):
        self.office = Office('reception')
        self.livingspace = Livingroom('java')

    def get_assert_room_is_created(self):
        self.assertIsNotNone(self.office.get_room_id())

    def test_get_roomname(self):
        self.assertEqual(self.office.get_roomname(), 'reception')

    def test_rename_roomname(self):
        self.office.set_roomname('occulus')
        self.assertEqual(self.office.get_roomname(), 'occulus')

    def test_get_room_role(self):
        self.assertEqual(self.livingspace.get_roomtype(), 'LIVINGROOM')

    def test_get_room_free_space_of_office_and_livingspace(self):
        self.assertEqual(self.office.get_room_space(), 6)
        self.assertEqual(self.livingspace.get_room_space(), 4)

    def test_add_occupant_to_fully_booked_office(self):
        self.office.set_room_space(0)
        self.assertFalse(self.office.update_room_space())

    def test_add_occupant_to_fully_booked_livingspace(self):
        self.livingspace.set_room_space(0)
        self.assertFalse(self.livingspace.update_room_space())

    def test_free_space_in_office_with_occupants(self):
        self.office.set_room_space(0)
        self.assertTrue(self.office.free_room_space())

    def test_free_space_in_livingspace_with_occupants(self):
        self.livingspace.set_room_space(0)
        self.assertTrue(self.livingspace.free_room_space())

    def test_set_room_id(self):
        self.livingspace.set_room_id(22)
        self.assertEqual(self.livingspace.get_room_id(), 22)

    def test_set_room_type(self):
        reset_office = Office('free_room')
        reset_office.set_roomtype('LIVINGROOM')
        self.assertEqual(reset_office.get_roomtype(), 'LIVINGROOM')
