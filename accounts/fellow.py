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
from amity.amity import Amity

class Fellow(Person):
	
	def __init__(self, name):

		super(Fellow, self).__init__(username = name, role= 'FELLOW')


	# ============================================================================
	# getter and setter methods for class attributes
	# ============================================================================


	@staticmethod
	def add_person(self, accomodation=False):
		'''
			Fellow.add_person()
			
			add_person method adds the fellow to a random room.
            The method checks for available rooms before assigning the fellow
            to the room. Additionally, it checks if the fellow opts for accomodation space.
		'''



		pass

