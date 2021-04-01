'''Main module of the 'diary'. Define the logic of the program.

It is necessary run this program to execute the 'diary'.

Notes
-----
It programmed in python 3.9
Author: Jonathan Garcia S. (johygasa@hotmail.com)

To simplify the program, this was used modular programming, altought when
modeling the tables with Peewee the 'POO' appears.
Other decision to keep the program simple was to choose SQLite as DB
engine, it is necessary to install before test the program.

I used PEP 8 to the structure; but the characters' maximum per line it
was fixed in 120.
Also, there are type hints in the functions (they are priorities) and
variables. Following the PEP 483, 484, 526...
The format of doctstrings is NumPy/SciPy, following PEP 257.

Examples
--------
Before execute this program, you must execute 'entry.py'.
To run the program, open a terminal and use the command 'cd' to change
directory (diary), if you did not do it. Now, just write:
> python main.py
'''

from functions_diary import menu, menu_opt


def main() -> None:
    '''Call 'menu()' and the diary functionality selected by the user.

    Returns
    -------
    None
    '''
    while True:
        option = menu()
        menu_opt[option]()

        to_continue = input("\nDo you want do anything else? yes (press 'y') or any other key to exit: ").lower().strip()
        if to_continue == 'y':
            continue
        else:
            print("Thanks to use 'diary' program. Come back Soon!")
            break


if __name__ == '__main__':
    main()
