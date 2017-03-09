"""
File      : livingroom.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Livingroom class that holds livingroom specification and attributes

"""

# ============================================================================
# necessary imports
# ============================================================================

from room import Room

class Livingroom(Room):

	def __init__(self, name):

		super(Livingroom, self).__init__(roomname = name, roomtype= 'LIVINGROOM', roomspace= 4)
		self._space_available = 4
		self.OFFICE_MAX_SPACE = 4

	def update_room_space(self):

		'''
			Livingroom.update_office_space()

			updates the space available in the office instance. 
		'''

		if self._space_available - 1 > -1:
			self._space_available = self._space_available - 1
		else:
			return 'out of space'

	def free_room_space(self):

		'''
			Livingroom.free_office_space()

			frees up space in the office instance. 
		'''

		if self._space_available +  1 < 5:
			self._space_available = self._space_available - 1
		else:
			return 'out of space'