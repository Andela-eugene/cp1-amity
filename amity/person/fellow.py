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

class Fellow(Person):
	'''
		Fellow class inherits from super class Person.
		The class inherits all attributes and methods from the parent class.
		Initiates a fellow, and assignes the fellow role.
	'''
	
	def __init__(self, fname=None, lname=None):

		super(Fellow, self).__init__(fname= fname, lname= lname, role= 'FELLOW')
		self._accomodation_allocated = None


	# ============================================================================
	# getter and setter methods for class attributes
	# ============================================================================
	def get_accomodation_allocated(self):
		'''
			get fellow's room accomodation 
		'''
		return self._accomodation_allocated

	def set_accomodation_allocated(self, accomname):
		'''
			set fellow's room accomodation 
		'''
		self._accomodation_allocated = accomname