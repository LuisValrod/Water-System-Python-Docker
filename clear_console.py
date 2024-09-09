import os
print('Hello World!')

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

clear_console()