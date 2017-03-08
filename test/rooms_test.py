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
from rooms.office import Office
from rooms.room import Room
from rooms.livingroom import Livingroom
from accounts.fellow import Fellow
from accounts.person import Person
from accounts.staff import Staff

class RoomTest(TestCase):

	def setUp(self):
		self.office = Office('reception')
		self.livingspace = Livingroom('java')
		self.fellow_one = Fellow('Matt')
		self.fellow_two = Fellow('Grace')
		self.fellow_three = Fellow('Mike')
		self.fellow_four = Fellow('Anthony')
		self.staff = Staff('Wendy')

	def test_staff_added_to_living_space(self):
		self.assertFalse(self.livingspace.add_user_to_room(self.staff))

	def test_add_occupant_to_fully_booked_room(self):
		self.office.add_user_to_room(self.staff)
		self.office.add_user_to_room(self.fellow_one)
		self.office.add_user_to_room(self.fellow_two)
		self.office.add_user_to_room(self.fellow_three)
		self.assertEqual(self.office.add_user_to_room(self.fellow_four), 'out of space')

	def test_free_space_in_room_with_occupants(self):
		self.assertEqual(self.livingspace.free_room_space(), None)

	def test_unique_room_name_constraint(self):
		new_office = Office('round-table')
		duplicate_office = Office('round-table')

		assert Room.unique_room_name_contsraint(new_office.get_roomname()) == 'already exists'