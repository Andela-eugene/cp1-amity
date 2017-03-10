"""
File      : person_test.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Person test file

"""

# ============================================================================
# necessary imports
# ============================================================================
from unittest import TestCase
from person.fellow import Fellow
from person.person import Person
from person.staff import Staff

class PersonTest(TestCase):

	def setUp(self):
		self.fellow = Fellow('Kevin')
		self.staff = Staff('Brian')


	def test_unique_username_constraint(self):

		fellow_one = Fellow('Kevin')
		duplicate_fellow = Fellow('Kevin')

		person = Person()
		self.assertEqual(person.add_fellow_or_staff_to_persons(fellow=fellows_list), 'added')

	def test_get_person_by_id(self):

		self.assertIsNotNone(Person.get_person_by_id(2))

	def test_get_person_by_name(self):

		self.assertIsNotNone(Person.get_person_by_username('Brian'))

	def test_number_of_persons(self):
		persons = Person()
		self.assertEqual(len(persons.get_persons()['Fellows']), 2)

