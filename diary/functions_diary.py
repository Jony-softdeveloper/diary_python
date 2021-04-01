"""Main functions' code of the 'diary': a basic CRUD.

Provide almost whole functionality of the diary, even, the function that
shows the menu, to the 'main' module.
Use of model-class Entry to execute and save the data in the diary.
"""

from collections import OrderedDict
from sys import stdin
from typing import Optional, NoReturn, Callable  # To type hints

from entry import Entry
from functions import clear_screen


def enter_title() -> Optional[str]:
    """Three attempts to put a correct and not empty title.

    If it failed, it displays a error message.

    Returns
    -------
    title : str or None
        The input by the user to name the entry.
        Or None when the user attempts three times and fail in these.
    """
    for count in range(3):  # 3 attempts
        title = input("Name of your entry (max. 40 characters): ").strip()
        if not title:       # Empty or ''
            print("Error: did not enter a title. Please, try again!")
            continue
        elif len(title) >= 41 and count != 2:
            print("Error: the title cannot have more of 40 characters. Plese, try again!")
            continue
        return title


def enter_content() -> Optional[str]:
    """Two attempts to save data in entry content.

    If nothing is written, that is to say the content is empty, it prints
    a error message.

    Returns
    -------
    content : str or None
        The text input by user that is crux of the diary entry.
        Or None when the user not write nothing in the two attempts.
    """
    print("\nWrite your comments or thoughts about it...\n(When finish press 'Ctrl + D' in linux and Mac; while "
          + "in cmd in Windows first press 'Enter', after 'Ctrl + Z' and finally 'Enter' again.)")
    for count in range(2):  # 2 attempts
        content = stdin.read().strip()
        if content:
            return content
        print("Error: there is not content. Please, retry it!")
        continue


def add_entry() -> None:
    """Add a new entry.

    The user enter a title and a content/description, also automatically
    is saved with the date-hour (this data works as primary key in DB).

    Returns
    -------
    None
    """
    clear_screen()
    print("Add entry")
    title = enter_title()
    if not title:
        print("\n*Number of attempts exceeded.*")
        return

    content = enter_content()
    if not content:
        # There's no content
        print("\n*Number of attempts exceeded.*")
        return
    # Save in DB
    Entry.create(title=title, content=content)
    print("Data saved.")


def delete_entry(entry: Entry, /) -> None:
    """Delete a specific entry.

    Once an entry is print on screen the user could choose "Delete it".

    Parameters
    ----------
    entry: Entry
        the Entry object which is going to be drop of database.

    Returns
    -------
    None
    """
    print("\nAre you sure want to delete it?")
    confirmation = input("Press 'y' to confirm and any other key to not delete it: ").lower().strip()

    if confirmation == 'y':
        entry.delete_instance()
        print("Entry deleted.\n")
    else:
        print("Entry not deleted.\n")


def update_entry(entry: Entry, /) -> None:
    """Update title or content or the specific entry.

    Once an entry is print on screen the user could choose "Update entry".
    The user can change title or content, even both, rewriting fully the
    section.

    Parameters
    ----------
    entry : Entry
        The Entry object which is going to be change and saved database.

    Returns
    -------
    None

    Notes
    -----
    The data 'day_hour' is not going to change.
    """
    there_is_change = False     # Flag to know there was a change
    print("\n--Update entry--")
    # Change of title
    print("Do you want to change the title? ", end='')
    change_title = input("Yes (press y) or any other key to not change it... ").lower().strip()
    if change_title == 'y':
        new_title = enter_title()
        if not new_title:
            print("\n*Number of attempts exceeded.*")
            return
        entry.title = new_title
        there_is_change = True

    # Change of content
    print("Do you want to change the content? ", end='')
    change_title = input("Yes (press y) or any other key to not change it... ").lower().strip()
    if change_title == 'y':
        new_content = enter_content()
        if not new_content:
            print("\n*Number of attempts exceeded.*")
            return
        entry.content = new_content
        there_is_change = True

    if there_is_change:     # Save in DB
        entry.save()
        print("Changes saved them.\n")
    else:
        print("Did not register any change.\n")


def print_actions_entries(entries: list[Entry], /) -> None:
    """Receive a list of entries and format them correctly to show them.

    After, display options: next entry or delete the current on screen.

    Parameters
    ----------
    entries : list of Entry
        The result of a query to get certain Entries.

    Returns
    -------
    None
    """
    for entry in entries:
        print(f"\t\tNota: '{entry.title}' ({entry.day_hour.strftime('%d/%b/%Y %H:%M')})")
        # Date's format: dd/Mon(3 characters)/yyyy hh(24 hours):MM
        print(entry.content)
        print("\nn) To show the next entry if there is a next one")
        print("d) To delete this entry")
        print("u) To update this entry")
        action: str = input("... or any other key to indicate you are done viewing your notes: ").lower().strip()
        if action == 'd':
            delete_entry(entry)
            continue
        elif action == 'u':
            update_entry(entry)
            continue
        elif action == 'n':
            print()     # A line break to separate the notes
            continue
        break


def show_entry() -> None:
    """Show an entry.

    Get one by one an entry from DB. It's possible select the sort: older
    one first or newer first.

    Returns
    -------
    None
    """

    def older() -> Optional[list[Entry]]:
        """Get the older entries first.

        Returns
        -------
        older : lisf of Entry or None
            If there is at least one Entry. The first positions be the
            older.
            Or None if there is no one Entry.
        """
        older = Entry.select().order_by(Entry.day_hour)
        return older

    def newer() -> Optional[list[Entry]]:
        """Get the newer entries first.

        Returns
        -------
        newer : lisf of Entry or None
            If there is at least one Entry. The first positions be the
            newer.
            Or None if there is no one Entry.
        """
        newer = Entry.select().order_by(Entry.day_hour.desc())      # Last ones first
        return newer

    order = OrderedDict({
        'a': older,
        'b': newer,
    })

    clear_screen()
    print("Show an entry")
    for opt, choose_sort in order.items():
        print(f"{opt}) {choose_sort.__doc__.split('.', maxsplit=1)[0]}", end=".\n")
    while True:
        sort = input("Choose the sort in oder to show you one by one an entry: ").lower().strip()
        if sort == 'a' or sort == 'b':
            break
        print('\nIt is not a valid option. Please, try again.')
        continue

    entries = order[sort]()
    if entries:
        clear_screen()
        print_actions_entries(entries)
    else:
        print("There's no entries.")


def search_entry() -> None:
    """Search an entry.

    Find it by searching for a specific word(s). The user select where is
    looking for that specific word: title or content. If there is at least
    one match, it will call to print_actions_entries() with the list of
    entries.

    Returns
    -------
    None
    """

    def search_in_title(word_phrase: str, /) -> Optional[list[Entry]]:
        """Search in title.

        Look for a word/phrase in diary entries' titles.

        Parameters
        ----------
        word_phrase : str
            The text which is looking for in title.

        Returns
        -------
        searching : list of Entry or None
            If 'word_phrase' appears in some title entries.
            Or None if there is no match with any pattern in some title.
        """
        # contains() is a Peewee's method to look in string with a wild-card as an argument
        searching = Entry.select().where(Entry.title.contains(word_phrase))
        return searching

    def search_in_content(word_phrase: str, /) -> Optional[list[Entry]]:
        """Search in content.

        Look for a word/phrase in diary entries' content.

        Parameters
        ----------
        word_phrase : str
            The text which is looking for in content.

        Returns
        -------
        searching : list of Entry or None
            If 'word_phrase' appears in some content entries.
            Or None whether not match with any pattern in the descriptions.
        """
        # contains() is a Peewee's method to look in string with a wild-card as an argument
        searching = Entry.select().where(Entry.content.contains(word_phrase))
        return searching

    where_search = OrderedDict({
        'a': search_in_title,
        'b': search_in_content,
    })

    clear_screen()
    print("Searching an entry...")
    for opt, query_function in where_search.items():
        print(f"{opt}) {query_function.__doc__.split('.', maxsplit=1)[0]}", end=".\n")
    while True:
        search = input("Choose where do the search: ").lower().strip()
        if search == 'a' or search == 'b':
            break
        print('\nIt is not a valid option. Please, try again.')
        continue
    word_phrase: str = (input('\nNow enter the exactly word or phrase to search (consider this is case sensitive): ')
                   .strip())

    entries = where_search[search](word_phrase)
    clear_screen()
    if not entries:
        print(f"There were not matches with the word '{word_phrase}'. Try again.")
        return
    elif len(entries) == 1:
        print(f"There are one matches. Here there it: ")
    else:
        print(f"There are {len(entries)} matches. Here there are them: ")
    print_actions_entries(entries)


def exit() -> NoReturn:
    """Finish the 'diary' execution."""
    print("Thanks to use 'diary' program. Come back soon!")
    raise SystemExit  # Exactly the same to write system.exit


# The menu options are saved in an ordered dictionary. At this level due to is used in main()
menu_opt = OrderedDict({
    1: add_entry,
    2: show_entry,
    3: search_entry,
    4: exit
})


def show_menu() -> None:
    """Using 'menu_opt' to print the options to users.

    In the future will be able to add new options easily.

    Returns
    -------
    None
    """
    for opt, function in menu_opt.items():
        # The docstring function works as description of the option, but only the first part, until the dot '.'
        print(f"{opt}.- {function.__doc__.split('.', maxsplit=1)[0]}", end=".\n")


def menu() -> int:
    """It's a menu to let the user choose what action to do in the diary.

    Call to show_menu() and after ask for an option.
    Exist a 'option' validation. Currently, the range of the options is
    between 1-4.

    Returns
    -------
    option : int
        The number put by the user.

    Raises
    ------
    ValueError
        When a user write a character which is not a number, it is not
        possible convert to int, so... print a message on screen to user.
    """
    clear_screen()
    print("\t\t-Diary-")
    show_menu()
    while True:
        try:
            option = int(input("What do want to do? ").strip())
        except ValueError:
            print("It's not a number.")
        else:
            if option <= 0 or option > 4:       # Not valid range
                print("It's not a valid option. Please, retry.")
                continue
            break
    return option
