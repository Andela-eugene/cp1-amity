"""
File      : office.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Office class that holds office specification and attributes

"""

# ============================================================================
# necessary imports
# ============================================================================

from room import Room


class Office(Room):

	def __init__(self, name):

		super(Office, self).__init__(roomname = name, roomtype= 'OFFICE', roomspace= 6)
		self._space_available = 6
		self.OFFICE_MAX_SPACE = 6


	# ============================================================================
	# add to room
	# ============================================================================
	def update_room_space(self):

		'''
			Office.update_office_space()

			updates the space available in the office instance. 
		'''

		if self._space_available - 1 > -1:
			self._space_available = self._space_available - 1
		else:
			return 'out of space'


	# ============================================================================
	# remove from room
	# ============================================================================
	def free_room_space(self):

		'''
			Office.free_office_space()

			frees up space in the office instance. 
		'''

		if self._space_available +  1 < 7:
			self._space_available = self._space_available - 1
		else:
			return 'limit reached'

