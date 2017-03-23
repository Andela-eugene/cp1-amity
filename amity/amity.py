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

from collections import OrderedDict

from rooms.livingroom import Livingroom
from rooms.office import Office
from person.fellow import Fellow
from person.staff import Staff
from termcolor import cprint, colored

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


    # ============================================================================
    # getter methods
    # ============================================================================
    def get_persons_dict(self):
        return self._persons

    def get_rooms_dict(self):
        return self._rooms_object

    # ============================================================================
    # create room from amity
    # ============================================================================
    def create_room(self, name, r_type='office'):
        is_created = False
        not_created = list()
        created = list()
        if r_type.lower() == 'office':
            for n in name:

                if self.is_room_name_unique(n):
                    new_office = Office(n)

                    office_object_dict = {n: new_office}
                    self._rooms_object['offices'].update(office_object_dict)
                    created.append(n)
                    is_created = True
                else:
                    not_created.append(n)

            if is_created:
                if len(not_created):
                    cprint('============================================================================', 'magenta')
                    cprint('                               ROOM(S) ALREADY EXIST','yellow')
                    cprint('============================================================================', 'magenta')
                    for room_not_created in not_created:
                        cprint('                               {}'.format(room_not_created),'yellow')
                cprint('============================================================================', 'magenta')
                cprint('                               OFFICE ROOM(S) CREATED', 'yellow')
                cprint('============================================================================', 'magenta')
                for room_created in created:
                        cprint('                               {}'.format(room_created),'yellow')
            else:
                cprint('                               NO ROOM(S) CREATED, ROOM(S) ALREADY EXIST', 'yellow')

        elif r_type.lower() == 'accomodation':
            for n in name:
                if self.is_room_name_unique(n):
                    new_living = Livingroom(n)

                    living_dict = {n: new_living}
                    self._rooms_object['livingspace'].update(living_dict)
                    created.append(n)
                    is_created = True
                else:
                    not_created.append(n)
                    
            if is_created:
                if len(not_created):
                    cprint('============================================================================', 'magenta')
                    cprint('                               ROOM(S) ALREADY EXIST','yellow')
                    cprint('============================================================================', 'magenta')
                    for room_not_created in not_created:
                        cprint('                               {}'.format(room_not_created),'yellow')
                cprint('============================================================================', 'magenta')
                cprint('                               LIVINGSPACE ROOM(S) CREATED', 'yellow')
                cprint('============================================================================', 'magenta')
                for room_created in created:
                        cprint('                               {}'.format(room_created),'yellow')
            else:
                cprint('                               NO ROOM(S) CREATED, ROOM(S) ALREADY EXIST', 'yellow')
        return is_created


    # ============================================================================
    # add new person to random room 
    # ============================================================================
    def add_person(self, name=None, lname=None, staff=None, fellow=None, accomodation=False):

        office_allocated = None
        accom_allocated = None

    	if staff is not None and fellow is None:
            new_staff = Staff(fname= name, lname=lname)

            staff_dict = {new_staff.get_person_id(): new_staff}
            self._persons['staff'].update(staff_dict)


            for k, v in self._rooms_object['offices'].iteritems():
                if v.get_room_space() > 0:
                    new_staff.set_office_allocated(v)
                    v.update_room_space()
                    office_allocated = v.get_roomname()
                    break

        elif staff is None and fellow is not None:

            new_fellow = Fellow(fname= name, lname=lname)
            fellow_dict = {new_fellow.get_person_id(): new_fellow}

            self._persons['fellows'].update(fellow_dict)

            if accomodation is True:

                new_fellow.set_boarding(True)

                for k, v in self._rooms_object['livingspace'].iteritems():
                    if v.get_room_space() > 0:
                        new_fellow.set_accomodation_allocated(v)
                        v.update_room_space()
                        accom_allocated = v.get_roomname()
                        break

            for k, v in self._rooms_object['offices'].iteritems():
                if v.get_room_space() > 0:
                    new_fellow.set_office_allocated(v)
                    v.update_room_space()
                    office_allocated = v.get_roomname()
                    break


        return OrderedDict([('first_name', name), ('last_name', lname), ('wanted_accom', accomodation), ('Office_name', office_allocated), ('Accom_name', accom_allocated)])


    # ============================================================================
    # get person details
    # ============================================================================
    def get_person_details(self, user_id):
        user = None
        for k, v in self._persons.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    if k == int(user_id):
                        cprint('                               FIRST NAME {}'.format(x.get_first_name()), 'yellow')
                        cprint('                               LAST NAME {}'.format(x.get_last_name()), 'yellow')
                        cprint('                               ROLE {}'.format(x.get_role()), 'yellow')
                        cprint('                               USER_ID {}'.format(x.get_person_id()), 'yellow')
                        cprint('                               BOARDING {}'.format(x.get_boarding()), 'yellow')
                        if x.get_office_allocated() is not None:
                            cprint('                               OFFICE ASSIGNED {}'.format(x.get_office_allocated().get_roomname()), 'yellow')
                        else:
                            cprint('                               OFFICE ASSIGNED NONE', 'yellow')
                        if x.get_role() == 'FELLOW':
                            if x.get_accomodation_allocated() is not None:
                                cprint('                               ACCOMODATION ASSIGNED {}'.format(x.get_accomodation_allocated().get_roomname()), 'yellow')
                            else:
                                cprint('                               NO ACCOMODATION ASSIGNED', 'yellow')
                        cprint('----------------------------------------------------------------------------', 'magenta')
                        user = x
                        break
        return user

    # ============================================================================
    # get persons
    # ============================================================================
    def get_persons(self):
        count = 0
        for k, v in self._persons.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                        count=+1
                        cprint('                               FIRST NAME {}'.format(x.get_first_name()), 'yellow')
                        cprint('                               LAST NAME {}'.format(x.get_last_name()), 'yellow')
                        cprint('                               ROLE {}'.format(x.get_role()), 'yellow')
                        cprint('                               USER_ID {}'.format(x.get_person_id()), 'yellow')
                        if x.get_office_allocated() is not None:
                            cprint('                               OFFICE ASSIGNED {}'.format(x.get_office_allocated().get_roomname()), 'yellow')
                        else:
                            cprint('                               NO OFFICE ASSIGNED', 'yellow')
                        if x.get_role() == 'FELLOW':
                            if x.get_accomodation_allocated() is not None:
                                cprint('                               ACCOMODATION ASSIGNED {}'.format(x.get_accomodation_allocated().get_roomname()), 'yellow')
                            else:
                                cprint('                               NO ACCOMODATION ASSIGNED', 'yellow')
                        cprint('----------------------------------------------------------------------------', 'magenta')
        return count
    
    # ============================================================================
    # get room details
    # ============================================================================
    def get_room_details(self, room_name):
        for k, v in self._rooms_object.iteritems():
            if isinstance(v ,dict):
                for room_key, room_value in v.iteritems():
                    if room_key == room_name:
                        return room_value

    # ============================================================================
    # get room details by id
    # ============================================================================
    def get_room_details_by_id(self, room_id):
        for k, v in self._rooms_object.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    if room_id != None:
                        if x.get_room_id() == int(room_id):
                            return x
                    else:
                        return None
        

    # ============================================================================
    # add people from a txt file
    # ============================================================================
    def load_people(self, file = None):
        file_loc = None
        if '/' in file:
            file_loc = file
        else:
            file_loc = '/amity/data/{}.txt'.format(file)
        path = os.getcwd() + file_loc
        persons_file = open(path, 'r')
        load_output = list()

        for person_entry in persons_file:
            data = person_entry.split()
            first_name = data[0]
            last_name = data[1]
            person_role = data[2]
            accom = False
            if len(data) > 3:
                if data[3] is not None and data[3] == 'Y':
                    accom = True
            if person_role.lower() == 'staff':
                load_output.append(self.add_person(name=first_name, lname=last_name, staff = person_role))
            elif person_role.lower() == 'fellow':
                load_output.append(self.add_person(name=first_name, lname=last_name, fellow = person_role, accomodation=accom))

        return load_output

    # ============================================================================
    # print un allocated rooms
    # ============================================================================
    def print_unallocated(self, file_out = None):
        data_exists = False
        cprint('============================================================================','magenta')
        cprint('                                 UN-ALLOCATED PERSONS', 'yellow')
        cprint('============================================================================','magenta')
        for k, v in self._persons.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    if x.get_office_allocated() == None:
                        data_exists = True
                        cprint('                                 {} {}:'.format(x.get_first_name(), x.get_last_name()), 'magenta')
                        cprint('                                        UNALLOCATED OFFICESPACE', 'yellow')
                        if x.get_boarding() == True and x.get_accomodation_allocated() == None:
                            cprint('                                        UNALLOCATED LIVINGSPACE', 'yellow')
                    if x.get_office_allocated() != None and x.get_boarding() == True and x.get_accomodation_allocated() == None:
                        data_exists = True
                        cprint('                                 {} {}:'.format(x.get_first_name(), x.get_last_name()), 'magenta')
                        cprint('                                        UNALLOCATED LIVINGSPACE', 'yellow')

        if data_exists == False:
            cprint('                                 NO ALLOCATIONS MADE', 'red')
            cprint('----------------------------------------------------------------------------', 'magenta')

        if file_out != None:
            file_loc = '/data/{}.txt'.format(file_out)
            path = os.getcwd() + file_loc
            alloc_file = open(path, 'w+')

            for k, v in self._persons.iteritems():
                if isinstance(v ,dict):
                    for k, x in v.iteritems():
                        if x.get_office_allocated() == None:
                            print >> alloc_file, '{} {}:'.format(x.get_first_name(), x.get_last_name())
                            print >> alloc_file, '      UNALLOCATED OFFICESPACE'
                            if x.get_boarding() == True and x.get_accomodation_allocated() == None:
                                print >> alloc_file, '      UNALLOCATED LIVINGSPACE'
                        if x.get_office_allocated() != None and x.get_boarding() == True and x.get_accomodation_allocated() == None:
                            print >> alloc_file, '{} {}:'.format(x.get_first_name(), x.get_last_name())
                            print >> alloc_file, '      UNALLOCATED LIVINGSPACE'


            cprint('                                 COPIED TO FILE', 'green')
            cprint('----------------------------------------------------------------------------', 'magenta')
        return data_exists

    # ============================================================================
    # print allocated rooms and the persons allocated
    # ============================================================================
    def print_allocated(self, file_out = None):
        data_exists = False

        for k, v in self._persons.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    if x.get_office_allocated() != None:
                        data_exists = True
                        cprint('                                 {} {}:'.format(x.get_first_name(), x.get_last_name()), 'magenta')
                        cprint('                                        OFFICE: {}'.format(x.get_office_allocated().get_roomname()), 'yellow')
                        if x.get_boarding() == True:
                            if x.get_accomodation_allocated() != None:
                                cprint('                                        ACCOMODATION: {}'.format(x.get_accomodation_allocated().get_roomname()), 'yellow')

                    if x.get_office_allocated() == None and x.get_boarding() == True:
                        if x.get_accomodation_allocated() != None:
                            data_exists = True
                            cprint('                                 {} {}:'.format(x.get_first_name(), x.get_last_name()), 'magenta')
                            cprint('                                        ACCOMODATION: {}'.format(x.get_accomodation_allocated().get_roomname()), 'yellow')

        if data_exists == False:
            cprint('                                 NO ALLOCATIONS MADE', 'red')
            cprint('----------------------------------------------------------------------------', 'magenta')

        if file_out != None:
            file_loc = '/data/{}.txt'.format(file_out)
            path = os.getcwd() + file_loc
            alloc_file = open(path, 'w+')

            for k, v in self._persons.iteritems():
                if isinstance(v ,dict):
                    for k, x in v.iteritems():
                        if x.get_office_allocated() != None:
                            print >> alloc_file, '{} {}'.format(x.get_first_name(), x.get_last_name())
                            print >> alloc_file, '      OFFICE: {}'.format(x.get_office_allocated().get_roomname())
                            if x.get_boarding() == True:
                                if x.get_accomodation_allocated() != None:
                                    print >> alloc_file, '      ACCOMODATION: {}'.format(x.get_accomodation_allocated().get_roomname())
                        if x.get_office_allocated() == None and x.get_boarding() == True:
                            if x.get_accomodation_allocated() != None:
                                print >> alloc_file, '{} {}'.format(x.get_first_name(), x.get_last_name())
                                print >> alloc_file, '      ACCOMODATION: {}'.format(x.get_accomodation_allocated().get_roomname())


            cprint('                                 COPIED TO FILE', 'green')
            cprint('----------------------------------------------------------------------------', 'magenta')

        return data_exists


    # ============================================================================
    # print room details
    # ============================================================================
    def print_room(self, roomname):
        for k, v in self._persons.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    if x.get_office_allocated() != None and x.get_office_allocated().get_roomname() == roomname:
                        cprint('                                 ROOM: {}, OCCUPANT: {} {}'.format(x.get_office_allocated().get_roomname(), x.get_first_name(), x.get_last_name()), 'yellow')
                        cprint('----------------------------------------------------------------------------', 'magenta')
                    if x.get_role() == 'FELLOW' and x.get_accomodation_allocated() != None and x.get_accomodation_allocated().get_roomname() == roomname:
                        cprint('                                 ROOM: {}, OCCUPANT: {} {}'.format(x.get_accomodation_allocated().get_roomname(), x.get_first_name(), x.get_last_name()), 'yellow')
                        cprint('----------------------------------------------------------------------------', 'magenta')



    # ============================================================================
    # print room details
    # ============================================================================
    def print_rooms(self):
        for k, v in self._rooms_object.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    cprint('                                 {}'.format(x.get_roomname()), 'yellow')
                    cprint('                                 {}'.format(x.get_room_id()), 'yellow')
                    cprint('                                 {}'.format(x.get_roomtype()), 'yellow')
                    cprint('                                 {}'.format(x.get_room_space()), 'yellow')
                    cprint('----------------------------------------------------------------------------', 'magenta')

    # ============================================================================
    # create unique room name constaraint
    # ============================================================================
    def is_room_name_unique(self, roomname):
        is_unique = True
        for room_dict_key, room_dict_value in self._rooms_object.iteritems():
            if isinstance(room_dict_value ,dict):
                for room_key, room_value in room_dict_value.iteritems():
                    if room_key == roomname:
                        is_unique = False
                        break
        return is_unique


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
                                    assigned = True
                                elif b.get_person_id() == user.get_person_id() and r_type == 'livingspace' and b.get_role() == 'FELLOW':
                                    v.update_room_space()
                                    b.set_accomodation_allocated(v)
                                    assigned = True

                if r_type == 'offices' and prev_off_room == v.get_roomname():
                    v.free_room_space()
                elif r_type == 'livingspace' and prev_accom_room == v.get_roomname():
                    v.free_room_space()

        self.get_person_details(person_id)

        return assigned


    # ============================================================================
    # save data to database
    # ============================================================================
    def save_state(self, save_data=None):
        '''Save rooms first'''
        roomDB = AmityRoomsDB(dbname = save_data, rooms = 'room')
        personDB = AmityPersonDB(dbname = save_data, person = 'person')
        cprint('                             SAVING ROOMS TO DB', 'yellow')
        for k, v in self._rooms_object.iteritems():
            if isinstance(v ,dict):
                for k, x in v.iteritems():
                    roomDB.insert_room(dict(room_id =x.get_room_id(), roomname= x.get_roomname(), roomtype= x.get_roomtype(), roomspace= x.get_room_space()))

        cprint('                             SAVING ROOMS TO DB COMPLETED', 'yellow')
        cprint('----------------------------------------------------------------------------', 'magenta')

        '''Save persons to db'''
        cprint('                             SAVING PERSONS TO DB', 'yellow')
        cprint('----------------------------------------------------------------------------', 'magenta')
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

                        personDB.insert_person(dict(person_id = x.get_person_id(), firstname = x.get_first_name(), lastname = x.get_last_name(), role = x.get_role(), boarding = x.get_boarding(), office_allocated= off_obj, accomodation_allocated = accom_obj))
                    else:
                        personDB.insert_person(dict(person_id = x.get_person_id(), firstname = x.get_first_name(), lastname = x.get_last_name(), role = x.get_role(), boarding = x.get_boarding(), office_allocated= off_obj))

        cprint('                             SAVING PERSON TO DB COMPLETED', 'yellow')
        cprint('----------------------------------------------------------------------------', 'magenta')
        return 'Done'



    # ============================================================================
    # loads a previously saved state
    # ============================================================================
    def load_state(self, load_data=None):
        roomDB = AmityRoomsDB(dbname = load_data, rooms = 'room')
        personDB = AmityPersonDB(dbname = load_data, person = 'person')
        total_room_person_count = 0

        for records in roomDB.retrive_rooms(): 
            room_count = 0
            db_room_list = list()
            for record_data in records:
                if room_count == 0:
                    db_room_list.append(record_data)
                if room_count == 1:
                    db_room_list.append(record_data)
                if room_count == 2:
                    db_room_list.append(record_data)
                if room_count == 3: 
                    db_room_list.append(record_data)

                room_count+=1
                total_room_person_count +=1

            if db_room_list[2] == 'OFFICE':
                office_object = Office(db_room_list[1])
                office_object.set_roomtype(db_room_list[2])
                office_object.set_room_id(db_room_list[0])
                office_object.set_room_space(db_room_list[3])

                print ' OFFICE CREATED FROM DB: {}, ID: {}, type: {}'.format(office_object.get_roomname(), office_object.get_room_id(), office_object.get_roomtype())

                if self.is_room_name_unique(office_object.get_roomname()):

                    office_object_dict = {office_object.get_roomname(): office_object}
                    self._rooms_object['offices'].update(office_object_dict)

            elif db_room_list[2] == 'LIVINGROOM':
                accom_object = Livingroom(db_room_list[1])
                accom_object.set_roomtype(db_room_list[2])
                accom_object.set_room_id(db_room_list[0])
                accom_object.set_room_space(db_room_list[3])

                print ' LIVINGSPACE CREATED FROM DB: {}, ID: {}, type: {}'.format(accom_object.get_roomname(), accom_object.get_room_id(), accom_object.get_roomtype())

                if self.is_room_name_unique(accom_object.get_roomname()):

                    accom_object_dict = {accom_object.get_roomname(): accom_object}
                    self._rooms_object['livingspace'].update(accom_object_dict)

        for records in personDB.retrive_persons():
            person_count = 0
            db_person_list = list()
            for record_data in records:
                if person_count == 0:
                    db_person_list.append(record_data)
                if person_count == 1:
                    db_person_list.append(record_data)
                if person_count == 2:
                    db_person_list.append(record_data)
                if person_count == 3: 
                    db_person_list.append(record_data)
                if person_count == 4: 
                    db_person_list.append(record_data)
                if person_count == 5: 
                    db_person_list.append(record_data)
                if person_count == 6: 
                    db_person_list.append(record_data)

                person_count+=1
                total_room_person_count +=1

            if db_person_list[3] == 'STAFF':
                staff_object = Staff(fname= db_person_list[1], lname=db_person_list[2])
                staff_object.set_person_id(db_person_list[0])
                staff_object.set_role(db_person_list[3])

                if db_person_list[4]:
                    staff_object.set_boarding(True)
                else:
                    staff_object.set_boarding(False)

                if db_person_list[5] != None:
                    office_room = self.get_room_details_by_id(db_person_list[5])
                    staff_object.set_office_allocated(office_room)

                print ' STAFF CREATED FROM DB: {} {}, ID: {}, ROLE: {}, BOARDING: {}, OFFICE NAME: {}'.format(staff_object.get_first_name(), staff_object.get_last_name(), staff_object.get_person_id(), staff_object.get_role(), staff_object.get_boarding(), staff_object.get_office_allocated().get_roomname())

                staff_dict = {staff_object.get_person_id(): staff_object}
                self._persons['staff'].update(staff_dict)
            if db_person_list[3] == 'FELLOW':
                fellow_object = Fellow(fname= db_person_list[1], lname=db_person_list[2])
                fellow_object.set_person_id(db_person_list[0])
                fellow_object.set_role(db_person_list[3])

                if db_person_list[4]:
                    fellow_object.set_boarding(True)
                else:
                    fellow_object.set_boarding(False)

                if len(db_person_list) > 5:
                    office_room = self.get_room_details_by_id(db_person_list[5])
                    fellow_object.set_office_allocated(office_room)

                if len(db_person_list) > 6:
                    accom_room = self.get_room_details_by_id(db_person_list[6])
                    fellow_object.set_accomodation_allocated(accom_room)

                accomodation = None
                if fellow_object.get_accomodation_allocated() == None:
                    accomodation = 'NO LIVINGSPACE'
                else:
                    accomodation = fellow_object.get_accomodation_allocated().get_roomname()
                print ' FELLOW CREATED FROM DB: {} {}, ID: {}, ROLE: {}, BOARDING: {}, OFFICE NAME: {}, ACCOMODATION NAME: {}'.format(fellow_object.get_first_name(), fellow_object.get_last_name(), fellow_object.get_person_id(), fellow_object.get_role(), fellow_object.get_boarding(), fellow_object.get_office_allocated().get_roomname(), accomodation)

                fellow_dict = {fellow_object.get_person_id(): fellow_object}
                self._persons['fellows'].update(fellow_dict)

        return 'done'


