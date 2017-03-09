"""
File      : room.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Room superclass

"""

import random

class Room(object):

	def __init__(self, **kwargs):

		'''
			initiates room arguments
			constructor method that implements room attributes and accesser methods
		'''

		self._roomname = kwargs.get('roomname')
		self._roomtype = kwargs.get('roomtype')
		self._room_id = id(self)
		self._room_space = kwargs.get('roomspace')


	# ============================================================================
	# getter and setter methods for class attributes
	# ============================================================================
	def get_roomname(self):
		return self._roomname

	def set_roomname(self, rmname):
		self._roomname = rmname

	def get_roomtype(self):
		return self._roomtype

	def set_roomtype(self, rmtype):
		self._roomtype = rmtype

	def get_room_id(self):
		return self._room_id

	def set_room_id(self, rmid):
		self._room_id = rmid

	def get_room_space(self):
		return self._room_space

	def set_room_space(self, rmspace):
		self._room_space = rmspace

	def get_rooms(self):
		return self._persons

	def add_livingspace_or_office_to_rooms(self, **kwargs):
		added_fellow = kwargs.get('fellow')
		added_staff = kwargs.get('staff')

		return None

	# ============================================================================
	# print room allocation
	# ============================================================================
	def print_allocations(self, output = False):

		'''
			Room.print_allocations()

			Prints a list of room allocations onto the screen. the method also allows
			outputing the result into a text file
		'''

		pass

	# ============================================================================
	# print unallocated people
	# ============================================================================
	def print_unallocated(self, output = False):

		'''
			Room.print_unallocated()

			Prints a list of unallocated people onto the screen. the method also allows
			outputing the result into a text file
		'''

		pass

	# ============================================================================
	# update room space method
	# ============================================================================
	def update_room_space(self):
		pass

	# ============================================================================
	# free up room space.
	# ============================================================================
	def free_room_space(self):
		pass

	# ============================================================================
	# add user to room
	# ============================================================================
	def add_user_to_room(self, user):
		pass

	# ============================================================================
	# unique room name constraint
	# ============================================================================
	@staticmethod
	def unique_room_name_contsraint(room_name):
		pass
