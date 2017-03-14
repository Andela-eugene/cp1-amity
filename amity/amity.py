"""
File      : amity.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Amity is a controller class that runs the application

"""

# ============================================================================
# necessary imports
# ============================================================================
import os

from rooms.livingroom import Livingroom
from rooms.office import Office
from person.fellow import Fellow
from person.staff import Staff

from models.amityRoomDB import AmityRoomsDB
from models.amityPersonDB import AmityPersonDB

class Amity(object):
    '''
		Amity class is the controller class for the amity project
		It initiates instances of Person and Room parent classes and controlles
		the views of the project.  
	'''

    def __init__(self):
        self._rooms_object = {'offices': {}, 'livingspace': {}}
        self._persons = {"fellows": {}, "staff": {}}
        self._unallocated_persons = {"fellows": {}, "staff_fellow": {}}

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

            # staff_dict = {name: {'name': new_staff.get_username(), 'user_id': new_staff.get_person_id(), 'role': new_staff.get_role(), 'boarding': new_staff.get_boarding()}}
            staff_dict = {name: new_staff}
            self._persons['staff'].update(staff_dict)

            for k, v in self._rooms_object['offices'].iteritems():
                if v.get_room_space() > 0:
                    new_staff.set_office_allocated(v)
                    v.update_room_space()
                    is_office_allocated = True
                    break
            if is_office_allocated == False:
                self._unallocated_persons['staff_fellow'].update(staff_dict)

        elif staff is None and fellow is not None:

            new_fellow = Fellow(name)
            fellow_dict = {name: new_fellow}

            self._persons['fellows'].update(fellow_dict)

            if accomodation is True:

                new_fellow.set_boarding(True)

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

            if is_office_allocated == False:
                self._unallocated_persons['staff_fellow'].update(fellow_dict)

            if is_accom_allocatied == False:
                self._unallocated_persons['staff_fellow'].update(fellow_dict)

        return {'Office': is_office_allocated, 'Living': is_accom_allocatied}

    # ============================================================================
    # get person details
    # ============================================================================
    def get_person_details(self, user_id):
        for k, v in self._persons.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    if x.get_person_id() == user_id:
                        return x

    # ============================================================================
    # get person details
    # ============================================================================
    def get_room_details(self, room_name):
        for k, v in self._rooms_object.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    if x.get_roomname() == room_name:
                        return x
        

    # ============================================================================
    # add people from a txt file
    # ============================================================================
    def load_people(self, file = None):
        file_loc = '/amity/data/{}.txt'.format(file)
        path = os.getcwd() + file_loc
        persons_file = open(path, 'r')

        for person_entry in persons_file:
            data = person_entry.split()
            person_name = data[0]
            person_role = data[1]
            if person_role.lower() == 'staff':
                ret = self.add_person(person_name, staff = person_role)
            elif person_role.lower() == 'fellow':
                ret = self.add_person(person_name, fellow = person_role)

    # ============================================================================
    # print un allocated rooms
    # ============================================================================
    def print_unallocated(self, file = None):
        print '============================================================================'
        print '                                 UN-ALLOCATED PERSONS'
        print '============================================================================'
        for k, v in self._persons.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    if x.get_office_allocated() == None:
                        print '                                 {}'.format(x.get_username())

    # ============================================================================
    # print allocated rooms and the persons allocated
    # ============================================================================
    def print_allocated(self, file = None):
        print '============================================================================'
        print '                                 ALLOCATED PERSONS WITH RESPECTIVE ROOMS'
        print '============================================================================'
        for k, v in self._persons.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    if x.get_office_allocated() != None:
                        print '                                 {}, {}'.format(x.get_username(), x.get_office_allocated().get_roomname())



    # ============================================================================
    # print room details
    # ============================================================================
    def print_room(self, roomname):
        print '============================================================================'
        print '                                 PRINT ROOM OCCUPANTS'
        print '============================================================================'
        for k, v in self._persons.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    if x.get_office_allocated() != None and x.get_office_allocated().get_roomname() == roomname:
                        print '                                 {}, {}'.format(x.get_office_allocated().get_roomname(), x.get_username())




    # ============================================================================
    # create unique room name constaraint
    # ============================================================================
    def is_room_name_unique(self, roomname):
        pass

    # ============================================================================
    # reallocate person to new room
    # ============================================================================
    def reallocate_person(self, person_id, roomname):
        user = self.get_person_details(person_id)
        prev_off_room = user.get_office_allocated().get_roomname()
        prev_accom_room = None

        if user.get_role() == 'FELLOW' and user.get_accomodation_allocated() != None:
            prev_accom_room = user.get_accomodation_allocated().get_roomname()
        room = self.get_room_details(roomname)
        assigned = False

        if room != None and user != None:
            r_type = room.get_roomtype()

            if r_type == 'OFFICE':
                r_type = 'offices'
            else:
                r_type = 'livingspace'

            for k, v in self._rooms_object[r_type].iteritems():
                if k.lower() == roomname.lower() and v.get_room_space() > 0:

                    for x, y in self._persons.iteritems():
                        if isinstance(y ,dict):
                            for a, b in y.iteritems():
                                if b.get_person_id() == user.get_person_id() and r_type == 'offices':
                                    v.update_room_space()
                                    b.set_office_allocated(v)
                                elif b.get_person_id() == user.get_person_id() and r_type == 'livingspace' and b.get_role() == 'FELLOW':
                                    v.update_room_space()
                                    b.set_accomodation_allocated(v)

                if r_type == 'offices' and prev_off_room == v.get_roomname():
                    v.free_room_space()
                elif r_type == 'livingspace' and prev_accom_room == v.get_roomname():
                    v.free_room_space()

                    assigned = True
                

            return assigned

        
    def reallocate_person_by_username(self, staffname, roomname):
        pass


    # ============================================================================
    # save data to database
    # ============================================================================
    def save_state(self, save_data):
        '''Save rooms first'''
        roomDB = AmityRoomsDB(dbname = save_data, rooms = 'room')
        personDB = AmityPersonDB(dbname = save_data, person = 'person')
        print '                             SAVING ROOMS TO DB'
        for k, v in self._rooms_object.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    roomDB.insert_room(dict(room_id =x.get_room_id(), roomname= x.get_roomname(), roomtype= x.get_roomtype(), roomspace= x.get_room_space()))

        print '                             SAVING ROOMS TO DB COMPLETED'

        '''Save persons to db'''
        print '                             SAVING PERSONS TO DB'
        for k, v in self._persons.iteritems():
            if isinstance(v, dict):
                for k, x in v.iteritems():

                    off_obj = x.get_office_allocated()

                    # check that room is asigned
                    if off_obj == None:
                        off_obj = None
                    else:
                        off_obj = off_obj.get_room_id()

                    if x.get_role() == 'FELLOW':
                        accom_obj = x.get_accomodation_allocated()
                        # check that living space is assigned
                        if accom_obj == None:
                            accom_obj = None
                        else:
                            accom_obj = accom_obj.get_room_id()

                        personDB.insert_person(dict(person_id = x.get_person_id(), username = x.get_username(), role = x.get_role(), boarding = x.get_boarding(), office_allocated= off_obj, accomodation_allocated = accom_obj))
                    else:
                        personDB.insert_person(dict(person_id = x.get_person_id(), username = x.get_username(), role = x.get_role(), boarding = x.get_boarding(), office_allocated= off_obj))

        print '                             SAVING PERSON TO DB COMPLETED'



    # ============================================================================
    # loads a previously saved state
    # ============================================================================
    def load_state(self, load_data):
        roomDB = AmityRoomsDB(dbname = load_data, rooms = 'room')
        personDB = AmityPersonDB(dbname = load_data, person = 'person')

        for r in roomDB.retrive_rooms(): 
            print '                                 {}'.format(r)

        for r in personDB.retrive_persons(): 
            print '                                 {}'.format(r)

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

    print '============================================================================'
    print '                                 Add Persons'
    print '============================================================================'

    print amity_one.add_person('John', staff='STAFF', fellow=None, accomodation=False)
    amity_one.add_person('Mark', staff='STAFF', fellow=None, accomodation=False)
    amity_one.add_person('Ian', staff=None, fellow='FELLOW', accomodation=True)
    amity_one.add_person('Mat', staff=None, fellow='FELLOW', accomodation=True)
    amity_one.add_person('Mary', staff=None, fellow='FELLOW', accomodation=True)
    amity_one.add_person('Sally', staff=None, fellow='FELLOW', accomodation=True)
    amity_one.add_person('Daisy', staff=None, fellow='FELLOW', accomodation=True)
    amity_one.add_person('Stacy', staff=None, fellow='FELLOW', accomodation=False)

    print '============================================================================'
    print '                                 PERSONS IDS'
    print '============================================================================'

    for k, v in amity_one._persons['fellows'].iteritems():
        print v.get_person_id()

    for k, v in amity_one._persons['staff'].iteritems():
        print v.get_person_id()

    print '============================================================================'
    print '                                 LIVINGSPACE ALLOCATED'
    print '============================================================================'

    for k, v in amity_one._rooms_object['livingspace'].iteritems():
        print v.get_roomname()
        print v.get_roomtype()
        print v.get_room_id()
        print v.get_room_space()

    print '============================================================================'
    print '                                 OFFICES ALLOCATED'
    print '============================================================================'

    for k, v in amity_one._rooms_object['offices'].iteritems():
        print v.get_roomname()
        print v.get_roomtype()
        print v.get_room_id()
        print v.get_room_space()

    print '============================================================================'
    print '                                 GET USER ID'
    print '============================================================================'

    for k, v in amity_one._persons['fellows'].iteritems():

        print '============================================================================'
        print '                                 searching for user with id {} '.format(v.get_person_id())
        print '============================================================================'

        pers = amity_one.get_person_details(v.get_person_id())

        print '                                 {} '.format(pers.get_username())
        print '                                 {} '.format(pers.get_role())
        print '                                 room name {} '.format(pers.get_office_allocated().get_roomname())
        print '                                 room id {} '.format(pers.get_office_allocated().get_room_id())

        print '============================================================================'
        print '                                 Reallocate person with id {} '.format(v.get_person_id())
        print '============================================================================'

        amity_one.reallocate_person(v.get_person_id(), 'reception')

        print '                                 {} '.format(v.get_username())
        print '                                 {} '.format(v.get_role())
        print '                                 room name {} '.format(v.get_office_allocated().get_roomname())
        print '                                 room id {} '.format(v.get_office_allocated().get_room_id())

        break

    print '============================================================================'
    print '                                 NEW LIVINGSPACE ALLOCATIONS'
    print '============================================================================'

    for k, v in amity_one._rooms_object['livingspace'].iteritems():
        print v.get_roomname()
        print v.get_roomtype()
        print v.get_room_id()
        print v.get_room_space()

    print '============================================================================'
    print '                                 NEW OFFICES ALLOCATIONS'
    print '============================================================================'

    for k, v in amity_one._rooms_object['offices'].iteritems():
        print v.get_roomname()
        print v.get_roomtype()
        print v.get_room_id()
        print v.get_room_space()

    print '============================================================================'
    print '                                 SHOW PERSONS FROM FILE'
    print '============================================================================'
    amity_one.load_people(file = 'persons')
    for k, v in amity_one._persons.iteritems():
        if isinstance(v ,dict):
            for n, x in v.iteritems():
                print '                                 {}, {}'.format(x.get_username(), x.get_role())

    amity_one.print_allocated()

    print '============================================================================'
    print '                                 NEW OFFICES ALLOCATIONS'
    print '============================================================================'

    for k, v in amity_one._rooms_object['offices'].iteritems():
        print v.get_roomname()
        print v.get_roomtype()
        print v.get_room_id()
        print v.get_room_space()

    amity_one.print_unallocated()

    amity_one.print_room('occulus')

    amity_one.save_state('amity.db')

    amity_one.load_state('amity.db')

if __name__ == '__main__':
    test()
