"""Model that creates the table to save the entries using ORM Peewee.

If is not installed in the enviroment when is running the proyect, it
is necessary install it.
To install Peewee, use the Package Installer for Python (PIP).
Write next in a terminal, :
    > pip install peewee

Pewee works:
- A class as a table in DB.
- A class atribute as column in a table.
- An instance of the class will be one register in the table.

This file as script lets create the DB 'diary.db' -using SQLite- and table
'Entry', that is the model-class.
Also, it could be imported as module and contains:
    * The model-class of the table Entry.

References
----------
.. [1] Peewee documentation. Available, [online]:
http://docs.peewee-orm.com/en/latest/

Examples
--------
To run the program, open a terminal and use the command 'cd' to change
directory (diary), if you did not do it. Now, to create the DB and
corresponding table a Entry, write:
> python entry.py
"""

from datetime import datetime

from peewee import *

# Define the file which content the DB. It needs the extension '.db'.
# It's created with autoconnect in True.
db = SqliteDatabase('diary.db')

# Model
class Entry(Model):
    """Class that models a table 'Entry' to represent a page of the diary.

    Attributes
    ----------
    day_hour : DateTimeField (datetime)
        The local time's moment when is created/saved the Entry.
    title : CharField (string)
        A name or significant phrase of the entry.
    content : TextField (string)
        All the information that desire save in the diary.

    Notes
    -----
    This special kinf of class need not a __ini__() method.
    """

    day_hour = DateTimeField(primary_key=True, default=datetime.now())
    title = CharField(40, index=True)
    content = TextField(null=True)

    class Meta:
        """Intern class to define data about DB and Table."""
        database = db               # To what DB is blinded.
        table_name = 'TBL_ENTRY'    # Name of the table in DB.


# Connect to the DB and create tables when run as script
if __name__ == '__main__':
    db.connect()
    db.create_tables([Entry])
    db.close()
