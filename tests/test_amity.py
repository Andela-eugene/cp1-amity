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

from amity.person.fellow import Fellow
from amity.person.staff import Staff
from amity.rooms.room import Room
from amity.rooms.livingroom import Livingroom
from amity.amity import Amity


class AmityTest(TestCase):

    def setUp(self):
        self.amity = Amity()
        self.amity.create_room(['occulus'])
        self.amity.create_room(['krypton'], r_type='accomodation')
        self.amity.create_room(['php'], r_type='accomodation')
        self.amity.add_person('Kim', 'Wang', staff='staff')
        self.amity.add_person(
            'Yung', 'Ping', fellow='fellow', accomodation=True)

    def test_create_room_function(self):
        self.assertTrue(self.amity.create_room('reception', 'OFFICE'))

    def test_add_person_function(self):
        output_list = self.amity.add_person('eugene', 'liyai', staff='fellow')
        self.assertEqual(output_list['first_name'], 'eugene')

    def test_get_person_details(self):
        persons = self.amity.get_persons_dict()
        for person_key, person_value in persons['staff'].iteritems():
            self.assertEqual(self.amity.get_person_details(
                person_key).get_first_name(), 'Kim')
            break

    def test_get_persons_in_amity_data_structure(self):
        self.assertGreater(self.amity.get_persons(), 0)

    def test_print_unallocated_persons(self):
        self.assertFalse(self.amity.print_unallocated())

    def test_print_unallocated_persons(self):
        self.assertTrue(self.amity.print_allocated())

    def test_add_unique_room_name_constraint(self):
        self.amity.create_room('occulus')
        self.assertFalse(self.amity.create_room('occulus'))

    def test_reallocate_staff_to_living_spcae(self):
        persons = self.amity.get_persons_dict()
        for person_key, person_value in persons['staff'].iteritems():
            self.assertFalse(
                self.amity.reallocate_person(person_key, 'krypton'))
            break

    def test_reallocate_occupant(self):
        persons = self.amity.get_persons_dict()
        for person_key, person_value in persons['fellows'].iteritems():
            self.assertTrue(self.amity.reallocate_person(
                person_key, 'krypton'))
            break

    def test_load_people_from_file(self):
        self.assertEqual(len(self.amity.load_people('persons')), 10)

    def test_save_state_into_database(self):
        self.assertEqual(self.amity.save_state('testAmity.db'), 'Done')

    def test_load_state_from_database(self):
        self.assertEqual(self.amity.load_state('testAmity.db'), 'done')
