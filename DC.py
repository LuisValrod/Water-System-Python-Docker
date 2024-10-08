import time
from exit import exit
# from cd_alta import cd_Alta
# from cd_update import cd_Modificacion
#-----------------------------------------Centro de distribucion --------------------------------------------------#
def distribution_center_management_system():
    print(' ----------DISTRIBUTION CENTER MANAGEMENT SYSTEM---------- ')
    is_on = True

    while is_on:
        mode = input('1.- Press 1 to register a new distribution center\n'
                         '2.- Press 2 to modify an existing distribution center\n'
                         '0.- Press 0 to go back to the main menu\n')

        if not mode.isnumeric() or int(mode) not in range(3):
            print('Please, enter a valid command')

        elif mode == '1':
            print('Loading register program ...')
            time.sleep(1)
            # WTP_register(EFFICIENCY)
            is_on = False

        elif mode == '2':
            print('Loading modify program ...')
            time.sleep(1)
            # WTP_modify(EFFICIENCY)
            is_on = False

        elif mode == '0':
            is_on = False
            exit()
