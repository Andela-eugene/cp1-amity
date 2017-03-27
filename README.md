# cp1-amity Office and Livingspace allocation

Amity is an application that runs on the terminal/command prompt, allowing allocation of office and living space to personel (fellow and staff). The applciation is modeled after Andela's room allocation system. Offices can occupy a maximum of 6 people while living spaces hold a maximum of 4 people. Moreover, the system should not allow a staff to be assigend to a livingspace and only assign fellows to the living space, only if the fellow opts for one.

## System Requirements.
  - **[Python 2.7 0r 3](https://www.python.org/)**
  - **Python virtual environment**
  - **SQLite Database (sqlite3)**
  
## Installation and running amity

The following Instructions will guide in setting up the CLI application in the development environment

#### Make directory for amity code and virtualenv

```
  $ mkdir -p ~/amity
  $ cd ~/amity
```

#### Prepare virtual environment
  - install requiremnets using `pip`
```
  $ virtualenv -p python amity_env
  $ source amity_env/bin/activate
```

> Use [this guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to create and activate a virtual environment.

#### Clone the repository into local file
```
$ git clone git@github.com:Andela-eugene/cp1-amity.git
```

#### install system requirements

```
pip install -r amity/requirements.txt
```

#### Run the application

> navigate to the application folder and run the file
```
python app.py -i
```
## Usage and comnon amity commands

  - Creating a room in amity
  ```
  amity create_room <room_name>... [--type=office]
  ```
 example
 
 ```
 amity create_room occulus hogwarts --type=office
 ```
     
  - Adding a person
  
  ```
    amity add_person <first_name> <last_name> <role> [--accomodation=accom]
  ```
  
  examle
  
  ```
  amity add_person John Doe Fellow --accomodation=Y
  ```
  
  -Print a particular room allocation
  
  ```
  print_room <room_name>
  ```
  example
  
  ```
  print_room occulus
  ```
    
  - add staff and fellows from file
  
  ```
  load_people
  ```
  This command loads people from a file.
  > **NOTE:** The input file, named `persons.txt` is located in the `data` directory
  
  - Reallocate person to a new room
  
  ```
  reallocate_person <person_identifier> <new_room_name>
  ```
  example
  
  ```
  reallocate_person 8387282891 hogwarts
  ```
  - Save amity's data structure to database
  
  ```
  save_state [--db=sqlite_database]
  ```
  example
  ```
  save_state --db=amity.db
  ```
  
  - Load amity's data structure from database
  ```
  load_state <sqlite_database>
  ```
  example
  ```
  load_state amity.db
  ```
  
  - Print all rooms and the allocations made
  > There is an optional parameter `--o` that indicates whether you would like the allocations to be printed out on a file. The option takes in a string which in turn is used as the filename to be created
  ```
  print_allocations [--o=filename]
  ```
  example
  ```
  print_allocations --o=room_allocations
  ```
  In this case the output file will be `room_allocations.txt`

### Application Screenshots

#### Amity Welcome
![Screenshot of Welcome](https://github.com/Andela-eugene/cp1-amity/blob/master/amity/designs/AmityWelcomeScreen.png "Welcome")

#### Amity Add Person
![Screenshot of Add Person](https://github.com/Andela-eugene/cp1-amity/blob/master/amity/designs/AddPerson.png "Add Person")

#### Amity Create Room
![Screenshot of Create Room](https://github.com/Andela-eugene/cp1-amity/blob/master/amity/designs/CreateRoom.png "Add Person")

#### Amity Print all users
![Screenshot of Print all users](https://github.com/Andela-eugene/cp1-amity/blob/master/amity/designs/PrintAllUsers.png "Add Person")

#### Amity Print Help
![Screenshot of Print all users](https://github.com/Andela-eugene/cp1-amity/blob/master/amity/designs/Help.png "Add Person")


## Help

For assistance using the application the `help` command prints out all valid commands and parametera required to run the application.


## License

### The MIT License (MIT)

Copyright (c) 2017 [Eugene Liyai](https://github.com/Andela-eugene).

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.
