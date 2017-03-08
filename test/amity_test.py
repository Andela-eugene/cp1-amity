"""
File      : amity_test.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Amity test file

"""

# ============================================================================
# necessary imports
# ============================================================================
from unittest import TestCase

from amity.amity import Amity
from accounts.fellow import Fellow
from accounts.staff import Staff
from rooms.room import Room
from rooms.livingroom import Livingroom


class AmityTest(TestCase):

	def setUp(self):
		self.amity = Amity()
		self.new_staff = Staff('Kim')

	def test_create_room_function(self):
		assert self.amity.create_room('reception', 'OFFICE') == 'room created'

	def test_add_person_function(self):
		self.assertTrue(self.amity.add_person(staff=self.new_staff))

	def test_get_room_details(self):
		new_livingspace = Livingroom('Java')

		self.assertEqual(self.amity.print_room(new_livingspace.get_roomname()), 'Java')

	def test_get_person_details(self):
		self.assertTrue(self.amity.get_person_details(self.new_staff.get_person_id()))

	def test_add_unique_room_name_constraint(self):
		new_livingspace = Livingroom('Java')
		self.assertTrue(self.amity.is_room_name_unique(new_livingspace.get_roomname()))

	def test_reallocate_staff_to_living_spcae(self):
		new_livingspace = Livingroom('Java')
		self.assertFalse(self.amity.reallocate_person_by_username(self.new_staff, new_livingspace))

	def test_reallocate_occupant(self):
		new_livingspace = Livingroom('Java')
		fellow = Fellow('Fred')
		self.assertTrue(self.amity.reallocate_person_by_username(fellow, new_livingspace))

	def test_save_state(self):
		self.assertTrue(self.amity.save_state('amity.db'))

	def test_load_state(self):
		self.assertTrue(self.amity.load_state('amity.db'))
