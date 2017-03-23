"""
File      : person.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Person superclass

"""

# ============================================================================
# necessary imports
# ============================================================================
from abc import ABCMeta

class Person(object):

	__metaclass__= ABCMeta
	

	def __init__(self, **kwargs):

		'''
			initiates person arguments
			constructor method that implements room attributes and accesser methods
		'''

		self._first_name = kwargs.get('fname')
		self._last_name = kwargs.get('lname')
		self._role = kwargs.get('role')
		self._person_id = id(self)
		self._boarding = False
		self._office_allocated = None


	# ============================================================================
	# getter and setter methods for class attributes
	# ============================================================================

	def get_first_name(self):
		'''
			retrves person's first name
		'''
		return self._first_name

	def set_first_name(self, uname):
		'''
			sets person's first name
		'''
		self._first_name = uname

	def get_last_name(self):
		'''
			retrves person's last name
		'''
		return self._last_name

	def set_last_name(self, uname):
		'''
			sets person's last name
		'''
		self._last_name = uname

	def get_office_allocated(self):
		'''
			retrves person's assigned office
		'''
		return self._office_allocated

	def set_office_allocated(self, offname):
		'''
			sets person's assigned office
		'''
		self._office_allocated = offname

	def get_role(self):
		'''
			retrves person's role
		'''
		return self._role

	def set_role(self, role):
		'''
			sets person's role
		'''
		self._role = role

	def get_person_id(self):
		'''
			retrves person's identification number
		'''
		return self._person_id

	def set_person_id(self, pid):
		'''
			sets person's identification number
		'''
		self._person_id = pid

	def get_boarding(self):
		'''
			retrves person's boarding status
		'''
		return self._boarding

	def set_boarding(self, board):
		'''
			sets person's boarding status
		'''
		self._boarding = board