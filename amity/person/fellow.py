"""
File      : fellow.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Fellow class that holds fellow specification, attributes and room allocation procedure

"""

# ============================================================================
# necessary imports
# ============================================================================

from person import Person
from rooms.livingroom import Livingroom
from rooms.office import Office

class Fellow(Person):
	
	def __init__(self, name):

		super(Fellow, self).__init__(username = name, role= 'FELLOW')
		self._accomodation_allocated = None


	# ============================================================================
	# getter and setter methods for class attributes
	# ============================================================================
	def get_accomodation_allocated(self):
		return self._accomodation_allocated

	def set_accomodation_allocated(self, accomname):
		self._accomodation_allocated = accomname

	@staticmethod
	def add_person(self, accomodation= 'N'):
		'''
			Fellow.add_person()
			
			add_person method adds the fellow to a random room.
            The method checks for available rooms before assigning the fellow
            to the room. Additionally, it checks if the fellow opts for accomodation space.
		'''

		

		pass

