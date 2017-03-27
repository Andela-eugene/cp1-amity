"""
File      : staff.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Staff class that holds staff specification,
attributes and room allocation procedure

"""

# ============================================================================
# necessary imports
# ============================================================================

from person import Person


class Staff(Person):
    '''
            Staff class inherits from super class Person.
            The class inherits all attributes
            and methods from the parent class.
            Initiates a staff, and assignes the staff role.
    '''

    def __init__(self, fname=None, lname=None):

        super(Staff, self).__init__(fname=fname, lname=lname, role='STAFF')
