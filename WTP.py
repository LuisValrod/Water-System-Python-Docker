from exit import exit
import time
from WTP_register import WTP_register

def water_treatment_plant_management_system(EFFICIENCY):
    print(' ----------WATER TREATMENT PLANT MANAGEMENT SYSTEM---------- ')
    is_on = True
    while is_on:
        mode = input('1.- Press 1 to register a new water treatment plant\n'
                     '2.- Press 2 to modify an existing water treatment plant\n'
                     '0.- Press 0 to go back to the main menu\n')
        if not mode.isnumeric() or int(mode) not in range(3):
            print('Please, enter a valid command')

        elif mode == '1':
            print('Loading register program ...')
            time.sleep(1)
            WTP_register(EFFICIENCY)
            is_on = False

        elif mode == '2':
            print('Loading modify program ...')
            time.sleep(1)
            #WTP_modify(WATER_QUALITY)
            is_on = False

        elif mode == '0':
            is_on = False
            exit()