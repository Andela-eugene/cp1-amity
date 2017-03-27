"""
File      : room.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Room superclass

"""

# ============================================================================
# necessary imports
# ============================================================================
from abc import ABCMeta


class Room(object):

    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        '''
                initiates room arguments
                constructor method that implements room
                attributes and accesser methods
        '''

        self._roomname = kwargs.get('roomname')
        self._roomtype = kwargs.get('roomtype')
        self._room_id = id(self)
        self._room_space = kwargs.get('roomspace')

    # ============================================================================
    # getter and setter methods for class attributes
    # ============================================================================
    def get_roomname(self):
        '''
                retrves the room name
        '''
        return self._roomname

    def set_roomname(self, rmname):
        '''
                sets the room name
        '''
        self._roomname = rmname

    def get_roomtype(self):
        '''
                get room type
        '''
        return self._roomtype

    def set_roomtype(self, rmtype):
        '''
                set room type
        '''
        self._roomtype = rmtype

    def get_room_id(self):
        '''
                get room identification number
        '''
        return self._room_id

    def set_room_id(self, rmid):
        '''
                set room identification number
        '''
        self._room_id = rmid

    def get_room_space(self):
        '''
                get room space available
        '''
        return self._room_space

    def set_room_space(self, rmspace):
        '''
                sets room space available
        '''
        self._room_space = rmspace
