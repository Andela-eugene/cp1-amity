"""
File      : amity.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Amity is a controller class that runs the application

"""

# ============================================================================
# necessary imports
# ============================================================================

from rooms.livingroom import Livingroom
from rooms.office import Office
from person.fellow import Fellow
from person.staff import Staff

class Amity(object):
    '''
		Amity class is the controller class for the amity project
		It initiates instances of Person and Room parent classes and controlles
		the views of the project.  
	'''

    def __init__(self):
        self._rooms_object = {'offices': {}, 'livingspace': {}}
        self._persons = {"fellows": {}, "staff": {}}

    # ============================================================================
    # create room from amity
    # ============================================================================
    def create_room(self, name, roomtype):
        if roomtype.lower() == 'office':
            new_office = Office(name)

            #office_dict = {name: {'name': new_office.get_roomname(), 'type': new_office.get_roomtype(), 'free-space': 4}}
            #self._rooms['offices'].update(office_dict)

            office_object_dict = {name: new_office}
            self._rooms_object['offices'].update(office_object_dict)

            return 'room created'
        elif roomtype.lower() == 'accomodation':
            new_living = Livingroom(name)

            living_dict = {name: new_living}
            self._rooms_object['livingspace'].update(living_dict)

            return 'room created'


    # ============================================================================
    # add new person to random room 
    # ============================================================================
    def add_person(self, name, staff=None, fellow=None, accomodation=False):

        is_office_allocated = False
        is_accom_allocatied = False

    	if staff is not None and fellow is None:
            new_staff = Staff(name)

            staff_dict = {name: {'name': new_staff.get_username(), 'user_id': new_staff.get_person_id(), 'role': new_staff.get_role(), 'boarding': new_staff.get_boarding()}}
            self._persons['staff'].update(staff_dict)

            for k, v in self._rooms_object['offices'].iteritems():
                if v.get_room_space() > 0:
                    new_staff.set_office_allocated(v)
                    v.update_room_space()
                    is_office_allocated = True
                    break

        elif staff is None and fellow is not None:

            new_fellow = Fellow(name)

            if accomodation is True:

                new_fellow.set_boarding(True)

                fellow_dict = {name: {'name': new_fellow.get_username(), 'user_id': new_fellow.get_person_id(), 'role': new_fellow.get_role(), 'boarding': new_fellow.get_boarding()}}
                self._persons['fellows'].update(fellow_dict)

                for k, v in self._rooms_object['livingspace'].iteritems():
                    if v.get_room_space() > 0:
                        new_fellow.set_accomodation_allocated(v)
                        v.update_room_space()
                        is_accom_allocatied = True
                        break

            for k, v in self._rooms_object['offices'].iteritems():
                if v.get_room_space() > 0:
                    new_fellow.set_office_allocated(v)
                    v.update_room_space()
                    is_office_allocated = True
                    break

    # ============================================================================
    # get person details
    # ============================================================================
    @staticmethod
    def get_person_details(user_id):

    	pass

    # ============================================================================
    # print un allocated rooms
    # ============================================================================
    @staticmethod
    def print_unallocated(file = None):

    	pass

    # ============================================================================
    # print allocated rooms and the persons allocated
    # ============================================================================
    @staticmethod
    def print_allocated(file = None):

    	pass

    # ============================================================================
    # print room details
    # ============================================================================
    @staticmethod
    def print_room(roomname):

    	pass

    # ============================================================================
    # create unique room name constaraint
    # ============================================================================
    def is_room_name_unique(self, roomname):
        pass

    # ============================================================================
    # reallocate person
    # ============================================================================
    def reallocate_person_by_username(self, staffname, roomname):
        pass

    def reallocate_person_by_userid(self, persinid, roomname):
        pass

    # ============================================================================
    # reallocate person
    # ============================================================================
    def save_state(self, save_data):
        pass

    # ============================================================================
    # loads a previously saved state
    # ============================================================================
    def load_state(self, load_data):
        pass

# ============================================================================
# test amity connection and operations
# ============================================================================
def test():

    amity_one = Amity()

    print(amity_one.create_room('reception', 'OFFICE'))
    print(amity_one.create_room('occulus', 'OFFICE'))
    print(amity_one.create_room('java', 'accomodation'))
    print(amity_one.create_room('PHP', 'accomodation'))

    print '============================================================================'
    print '                             Rooms Created'
    print '============================================================================'

    print amity_one._rooms_object['offices']
    print amity_one._rooms_object['livingspace']

    print '============================================================================'
    print '                                 OFFICES'
    print '============================================================================'

    for k, v in amity_one._rooms_object['offices'].iteritems():
        print k, v.get_roomname()
        print v.get_roomtype()
        print v.get_room_id()

    print '============================================================================'
    print '                                 LIVINGSPACE'
    print '============================================================================'

    for k, v in amity_one._rooms_object['livingspace'].iteritems():
        print k, v.get_roomname()
        print v.get_roomtype()
        print v.get_room_id()

if __name__ == '__main__':
    test()
