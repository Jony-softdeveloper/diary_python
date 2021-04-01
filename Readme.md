### Personal Diary 📔📗
<hr/>
It is a mini-project created using:

* [Python][] 3(.9) as programming lenguage
* [Peewee][] as ORM
* [SQLite][] as engine of DB

[Python]: https://www.python.org/downloads/ "Python"
[Peewee]: http://docs.peewee-orm.com/en/latest/peewee/installation.html "Peewee"
[SQLite]: https://www.sqlite.org/download.html "SQLite"

Before execute this program and test the functionality of it, you must execute <span>entry.py</span> to create the DB: a file with extension '.db' (will be create in the same directory). <br/>
To run the program, open a terminal and use the command 'cd' to change
directory (diary), if you did not do it. Now, write:

    > python entry.py

To run the diary, it is necessary run this program to execute the 'diary'.

    > python main.py

<br/>
This project has a basic CRUD using *entries* how the entities that make up the diary.

Add and Read(/show) options of the entries are displayed in main menu. Update and delete are options that appears every are is showing an entry.

<br/>

To simplify the program, this was used modular programming, although when modeling the tables with Peewee the 'POO' appears.
Other decision to keep the program simple was to choose SQLite as DB engine.

<br/>

I used PEP 8 to the structure; but the characters' maximum per line it was fixed in 120.<br/>
Also, there are type hints in the functions (they are priorities) and variables. Following the PEP 483, 484, 526...<br/>
The format of docstrings is NumPy/SciPy, following PEP 257. **The four files of code are document.**

<br/>

### Running the program (powershell) 💻
<hr>
Main menu

![Diary menu](\images\Diary_menu.png)

Showing an entry
![Showing an entry](\images\Show_an_entry.png)

Author: Jonathan Garcia S. @Jony-softdeveloper
<br/>
This project is licensed under the terms of the **GPL-3.0-or-later** (see copying.txt   ).
