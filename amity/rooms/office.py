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
    '''
            Office class inherits from Room super class.
            The class inherits all attributes and
            methods from the parent class.
            Initiates a Office room instance.
    '''

    def __init__(self, name):

        super(Office, self).__init__(
            roomname=name, roomtype='OFFICE', roomspace=6)

    # ============================================================================
    # add to room
    # ============================================================================
    def update_room_space(self):
        '''
                Livingroom.update_office_space()

                updates the space available in the office instance.
        '''

        roomspace = self.get_room_space()

        if roomspace:
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

        if 0 <= roomspace < 6:
            self.set_room_space(roomspace + 1)
            return True
        else:
            return False
