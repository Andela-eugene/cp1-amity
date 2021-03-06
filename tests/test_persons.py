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
from amity.person.fellow import Fellow
from amity.person.staff import Staff


class PersonTest(TestCase):

    def setUp(self):
        self.fellow = Fellow('Kevin', 'Hart', )
        self.staff = Staff('Brian', 'Awori')

    def test_person_is_created(self):
        self.assertIsNotNone(self.fellow.get_person_id())

    def test_get_person_name(self):
        self.assertEqual(self.staff.get_first_name(), 'Brian')
        self.assertEqual(self.staff.get_last_name(), 'Awori')

    def test_set_person_first_name_and_last_name(self):
        self.fellow.set_first_name('KevinTwo')
        self.fellow.set_last_name('HartTwo')
        self.assertEqual(self.fellow.get_first_name(), 'KevinTwo')
        self.assertEqual(self.fellow.get_last_name(), 'HartTwo')

    def test_get_boarding(self):
        self.fellow.set_boarding(True)
        self.assertTrue(self.fellow.get_boarding())

    def test_set_role(self):
        self.fellow.set_role('STAFF')
        self.assertEqual(self.fellow.get_role(), 'STAFF')

    def test_set_person_id(self):
        self.staff.set_person_id(22)
        self.assertEqual(self.staff.get_person_id(), 22)
