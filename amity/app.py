"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    amity create_room <room_name>
    amity add_person <first_name> <last_name> <role> <wants_accommodation>
    amity reallocate_person <person_identifier> <new_room_name>
    amity load_people
    amity print_rooms
    amity print_allocations [-o=filename]
    amity print_unallocated [-o=filename]
    amity print_room <room_name>
    amity save_state [--db=sqlite_database]
    amity load_state <sqlite_database>
    amity (-i | --interactive)
    amity (-h | --help | --version)
    amity exit
 
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

Note:
    use interactive for best perfomance

"""


import sys
import cmd


from termcolor import cprint, colored
from termcolor import cprint
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit
from amity import Amity

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:

            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print ('Invalid Command!')
            print (e)
            print
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class MyInteractive(cmd.Cmd):

    cprint(figlet_format('AMITY', font='roman'), 'yellow')
    cprint('------------------------------------------------------------------------------------------------------------------', 'magenta')
    cprint("\t\tAmity is a room booking system that allocates free space to fellows or staff", 'yellow')
    cprint('------------------------------------------------------------------------------------------------------------------', 'magenta')
    cprint("\n\t\t'-h' or '--help' provides full list of commands for running the application\n", 'white')

    """
    Usage:
        AMITY create_room <room_name>
        AMITY delete_room <room_name> 
        AMITY add_person <first_name> <last_name> <role> <wants_accommodation>            
        AMITY reallocate_person <person_identifier> <new_room_name>
        AMITY load_people
        AMITY print_rooms
        AMITY print_allocations [-o=filename]
        AMITY print_unallocated [-o=filename]
        AMITY print_room <room_name>
        AMITY save_state [--db=sqlite_database]
        AMITY load_state <sqlite_database>
        AMITY (-i | --interactive)
        AMITY (-h | --help)
        AMITY exit

    Options:
        -i, --interactive  Interactive Mode
        -h, --help  Show this screen and exit.
    """

    prompt = 'Enter a command: amity  '
    file = None

    def do_exit(self, arg):
        """Usage: exit"""
        print
        print "closing"
       
        print

        exit()


    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_name>... [--type=office]"""
        if arg['--type'] is None:
            amity.create_room(arg['<room_name>'], r_type='office')
        else:
            amity.create_room(arg['<room_name>'], r_type=arg['--type'])
        print
        

    @docopt_cmd
    def do_delete_room(self,arg):
        """Usage: delete_room <room_name> """
        pass

    @docopt_cmd
    def do_add_person(self, arg):
        '''Usage: add_person <first_name> <last_name> <role> [--accomodation=accom]'''
        allocation_output = None
        if arg['<role>'].lower() == 'staff':
            allocation_output = amity.add_person(name=arg['<first_name>'], lname=arg['<last_name>'], staff=arg['<role>'])

        elif arg['<role>'].lower() == 'fellow':
            if  arg['--accomodation'] == None:
                allocation_output=amity.add_person(name=arg['<first_name>'], lname=arg['<last_name>'], fellow=arg['<role>'], accomodation=False)
            elif  arg['--accomodation'].lower() == 'y':
                allocation_output=amity.add_person(name=arg['<first_name>'], lname=arg['<last_name>'], fellow=arg['<role>'], accomodation=True)
            elif  arg['--accomodation'].lower() == 'n':
                allocation_output=amity.add_person(name=arg['<first_name>'], lname=arg['<last_name>'], fellow=arg['<role>'], accomodation=False)
            elif  arg['--accomodation'].lower() != 'y' or arg['--accomodation'].lower() != 'n':
                cprint('                                  Invalid accommodation parameter', 'yellow')
        
        cprint('============================================================================', 'magenta')
        cprint('                                  ADD USER {} {}'.format(arg['<first_name>'].upper(), arg['<last_name>'].upper()), 'yellow')
        cprint('============================================================================', 'magenta')
        for output_key, output_value in allocation_output.iteritems():
                if output_key == 'Office_name':
                    if output_value != None:
                        cprint('                                  OFFICE ALLOCATED: {}'.format(output_value), 'yellow')
                        cprint('----------------------------------------------------------------------------', 'magenta')
                    else:
                        cprint('                                  NO OFFICE ALLOCATED, OUT OF SPACE', 'yellow')
                        cprint('----------------------------------------------------------------------------', 'magenta')
                if output_key == 'Accom_name' and arg['<role>'].lower() == 'fellow':
                    if output_value != None:
                        cprint('                                  LIVINGSPACE ALLOCATED: {}'.format(output_value), 'yellow')
                        cprint('----------------------------------------------------------------------------', 'magenta')
                    else:
                        cprint('                                  NO LIVINGSPACE ALLOCATED, OUT OF SPACE', 'yellow')
                        cprint('----------------------------------------------------------------------------', 'magenta')
        print


    @docopt_cmd
    def do_load_people(self, arg):
        """usage: load_people"""
        cprint('============================================================================', 'magenta')
        cprint('                                  LOAD PEOPLE FROM FILE', 'yellow')
        cprint('============================================================================', 'magenta')
        load_return=amity.load_people('persons')

        for load_output in load_return:
            name_string = ''
            wanted_accom = None
            sorted(load_output.keys())
            for output_key, output_value in load_output.iteritems():
                    if output_key == 'first_name':
                        name_string += output_value+ ' '
                    elif output_key == 'last_name':
                        name_string += output_value
                        cprint('                                  {}'.format(name_string), 'yellow')
                    elif output_key == 'Office_name':
                        if wanted_accom == True:
                            if output_value != None:
                                cprint('                                  OFFICE ALLOCATED: {}'.format(output_value), 'yellow')
                            else:
                                cprint('                                  NO OFFICE ALLOCATED, SPACE UNAVAILABLE', 'yellow')
                        elif output_value != None:
                            cprint('                                  OFFICE ALLOCATED: {}'.format(output_value), 'yellow')
                            cprint('----------------------------------------------------------------------------', 'magenta')
                        else:
                            cprint('                                  NO OFFICE ALLOCATED, SPACE UNAVAILABLE', 'yellow')
                            cprint('----------------------------------------------------------------------------', 'magenta')
                    elif output_key == 'wanted_accom':
                        wanted_accom = output_value
                    elif output_key == 'Accom_name' and wanted_accom == True:
                        if output_value != None:
                            cprint('                                  LIVINGSPACE ALLOCATED: {}'.format(output_value), 'yellow')
                            cprint('----------------------------------------------------------------------------', 'magenta')
                        else:
                            cprint('                                  NO LIVINGSPACE ALLOCATED, SPACE UNAVAILABLE', 'yellow')
                            cprint('----------------------------------------------------------------------------', 'magenta')

        cprint('                                  SUCCEESFULY ADDED', 'green')
        cprint('----------------------------------------------------------------------------', 'magenta')

    @docopt_cmd
    def do_print_rooms(self,arg):
        """usage: print_rooms"""
        cprint('============================================================================', 'magenta')
        cprint('                                  PRINT ALL ROOM', 'yellow')
        cprint('============================================================================', 'magenta')
        print amity.print_rooms()
        

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <new_room_name>"""
        cprint('============================================================================', 'magenta')
        cprint('                                  REALLOCATE USER', 'yellow')
        cprint('============================================================================', 'magenta')
        is_assigned = amity.reallocate_person(arg['<person_identifier>'], arg['<new_room_name>'])
        if is_assigned == True:
            cprint('                              SUCCEESFULY REASIGNED', 'green')
            cprint('----------------------------------------------------------------------------', 'magenta')
            print
        else:
            cprint('                              FAILED TO REASIGNED', 'red')
            cprint('----------------------------------------------------------------------------', 'magenta')
        
    @docopt_cmd
    def do_print_users(self, arg):
        """usage: print_users"""
        cprint('============================================================================', 'magenta')
        cprint('                                  PRINT ALL USERS', 'yellow')
        cprint('============================================================================', 'magenta')
        amity.get_persons()


    @docopt_cmd
    def do_print_user_details(self, arg):
        """usage: print_user_details <person_id>"""
        cprint('============================================================================', 'magenta')
        cprint('                                  USER DETAILS', 'yellow')
        cprint('============================================================================', 'magenta')
        amity.get_person_details(arg['<person_id>'])

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [--o=filename]"""
        cprint('============================================================================','magenta')
        cprint('                                 ALLOCATED PERSONS WITH RESPECTIVE ROOMS', 'yellow')
        cprint('============================================================================','magenta')
        if arg['--o'] is not None:
            amity.print_allocated(file_out=arg['--o'])
        else:
            amity.print_allocated()
        print
        
    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [--o=filename]"""
        if arg['--o'] is not None:
            amity.print_unallocated(file_out=arg['--o'])
        else:
            amity.print_unallocated()

    @docopt_cmd
    def do_print_room(self,arg):
        """Usage: print_room <room_name>"""
        cprint('============================================================================', 'magenta')
        cprint('                                  PRINT ROOM OCCUPANTS', 'yellow')
        cprint('============================================================================', 'magenta')
        amity.print_room(arg['<room_name>'])

    @docopt_cmd
    def do_save_state(self,arg):
        """Usage: save_state [--db=sqlite_database]"""
        if arg['--db'] is not None:
            amity.save_state(save_data=arg['--db'])
        else:
            cprint('============================================================================', 'magenta')
            cprint('                                  ERROR: SPECIFY DATABASE', 'red')
            cprint('============================================================================', 'magenta')

    @docopt_cmd
    def do_load_state(self,arg):
        """Usage: load_state <sqlite_database>"""
        amity.load_state(load_data=arg['<sqlite_database>'])
        

        



opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        # print (__doc__)
        amity = Amity()
        MyInteractive().cmdloop()
    except KeyboardInterrupt:
        print "\n"