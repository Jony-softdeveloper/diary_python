'''General functions not strictly in relation with 'diary'.'''

# Module that lets use system("cls") in windows or system("clear") in linux
from os import system, name


def clear_screen() -> None:
    '''To clear screen terminal indepently of Operating system.

    Returns
    -------
    None
    '''
    system('cls' if name == 'nt' else 'clear')
