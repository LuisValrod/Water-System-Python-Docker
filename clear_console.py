import os

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

clear_console()