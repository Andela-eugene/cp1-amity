"""
File      : staff.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Staff class that holds staff specification, attributes and room allocation procedure

"""

# ============================================================================
# necessary imports
# ============================================================================

from person import Person

class Staff(Person):

	def __init__(self, name):

		super(Staff, self).__init__(username = name, role= 'STAFF')


	@staticmethod
	def add_person(self):
		'''
			Staff.add_person()
			
			add_person method adds the staff member to a random room.
            The method checks for available rooms before assigning the staff
            to the room.
		'''

		pass
