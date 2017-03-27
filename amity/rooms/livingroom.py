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
    '''
            Livingroom class inherits from Room super class.
            The class inherits all attributes and
            methods from the parent class.
            Initiates a Livingroom room instance.
    '''

    def __init__(self, name):

        super(Livingroom, self).__init__(
            roomname=name, roomtype='LIVINGROOM', roomspace=4)

    # ============================================================================
    # add to room
    # ============================================================================
    def update_room_space(self):
        '''
                Livingroom.update_office_space()

                updates the space available in the office instance.
        '''

        roomspace = self.get_room_space()

        if roomspace > 0:
            self.set_room_space(roomspace - 1)
            return True
        else:
            return False

    # ============================================================================
    # remove from room
    # ============================================================================
    def free_room_space(self):
        '''
                Livingroom.free_office_space()

                frees up space in the office instance.
        '''
        roomspace = self.get_room_space()

        if 0 <= roomspace < 4:
            self.set_room_space(roomspace + 1)
            return True
        else:
            return False
