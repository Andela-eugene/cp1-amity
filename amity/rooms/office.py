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
        update_space = None
        roomspace = self.get_room_space()

        if roomspace:
            self.set_room_space(roomspace - 1)
            update_space = True
        else:
            update_space = False

        return update_space

    # ============================================================================
    # remove from room
    # ============================================================================
    def free_room_space(self):
        '''
                Livingroom.free_office_space()

                frees up space in the office instance.
        '''
        free_space = False
        roomspace = self.get_room_space()

        if 0 <= roomspace < 6:
            self.set_room_space(roomspace + 1)
            free_space = True

        return free_space
