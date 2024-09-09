from exit import exit
from WS_register import WS_register
from WS_modify import WS_modify
def water_source_management_system(WATER_QUALITY):
    print(' ----------WATER SOURCE MANAGEMENT SYSTEM---------- ')
    is_on = True
    while is_on:
        mode = input('1.- Press 1 to register a new water source\n'
                     '2.- Press 2 to modify an existing water source\n'
                     '0.- Press 0 to go back to the main menu\n')
        if not mode.isnumeric() or int(mode) not in range(3):
            print('Please, enter a valid command')

        elif mode == '1':
            print('processing register')
            WS_register(WATER_QUALITY)
            is_on = False

        elif mode == '2':
            print('processing modify')
            WS_modify(WATER_QUALITY)
            is_on = False

        elif mode == '0':
            is_on = False
            exit()