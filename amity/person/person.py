"""
File      : person.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Person superclass

"""

class Person(object):
	

	def __init__(self, **kwargs):

		'''
			initiates person arguments
			constructor method that implements room attributes and accesser methods
		'''

		self._username = kwargs.get('username')
		self._role = kwargs.get('role')
		self._person_id = id(self)
		self._boarding = False
		self._total_persons = 0
		self._persons = {"Fellows": {}, "Staff": {}}
		self._office_allocated = None


	# ============================================================================
	# getter and setter methods for class attributes
	# ============================================================================

	def get_username(self):
		return self._username

	def set_username(self, uname):
		self._username = uname

	def get_office_allocated(self):
		return self._username

	def set_office_allocated(self, offname):
		self._office_allocated = offname

	def get_role(self):
		return self._role

	def set_role(self, role):
		self._role = role

	def get_person_id(self):
		return self._person_id

	def set_person_id(self, pid):
		self._person_id = pid

	def get_boarding(self):
		return self._boarding

	def set_boarding(self, board):
		self._boarding = board

	def get_total_persons(self):
		return self._total_persons

	def set_total_persons(self, ttlPpl):
		self._total_persons = ttlPpl

	def get_persons(self):
		return self._persons

	def add_fellow_or_staff_to_persons(self, **kwargs):
		added_fellow = kwargs.get('fellow')
		added_staff = kwargs.get('staff')

		return None


	# ============================================================================
	# reallocates person to new room
	# ============================================================================
	def reallocate_person(self, userid, roomname):
		'''
			Person.reallocate_person()
			
			reallocates people to another room. the method takes the user identification number
			and the roomname as parameters. 
		'''

		pass

	# ============================================================================
	# loads people to rooms from a text file
	# ============================================================================
	def load_people(self):
		'''
			Person.load_people()
			
			load_poeple populates room with data from a text file.
		'''

		pass

	# ============================================================================
	# get all users username
	# ============================================================================
	def get_all_usernames(self):
		'''
			Person.get_all_usernames()
			
			returns people's usernames in a list
		'''

		return []

	# ============================================================================
	# get person by user_id
	# ============================================================================
	@staticmethod
	def get_person_by_id(id):
		return None

	# ============================================================================
	# get person by user_id
	# ============================================================================
	@staticmethod
	def get_person_by_username(name):
		return None