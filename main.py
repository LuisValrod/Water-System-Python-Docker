import time
from exit import exit
from clear_console import clear_console
from WS import water_source_management_system

PENALTIES_WS = {'HIGH': 0, 'MEDIUM': 0.1, 'LOW': 0.2 }
PENALTIES_WTP = {'HIGH': 0, 'MEDIUM': 0.1, 'LOW': 0.2 }
WATER_QUALITY = ['POTABLE', 'HIGH', 'MEDIUM', 'LOW', 'NON-POTABLE']
EFFICIENCY = ['HIGH', 'MEDIUM', 'LOW']


def main_menu():
    print('WELCOME TO OUR WATER MANAGEMENT SYSTEM')
    is_on = True
    while is_on:
        print('----------------MAIN MENU----------------')
        choice= input('1.- Press 1 to access the water sources menu\n'
                      '2.- Press 2 to access the water treatment plants menu\n'
                      '3.- Press 3 to access the distribution centers menu\n'
                      '4.- Press 4 to access the interconnections menu\n'
                      '5.- Press 5 to enter simulation of the entire system over a number of days\n'
                      '6.- Press 6 to access your files\n'
                      '0.- Press 0 to exit the program\n'
                      '-------------------------------------------\n')
        if not choice.isnumeric() or int(choice) not in range(7):
            print('Please, select a valid command')

        elif choice =='1':
            clear_console()
            # Water Source
            water_source_management_system(WATER_QUALITY)

        elif choice =='2':
            # Water Treatment Plant
            clear_console()
            print('Program Coming')

        elif choice =='3':
            # Distribution
            clear_console()
            print('Program Coming')

        elif choice =='4':
            # Interconnections
            clear_console()
            print('Program Coming')

        elif choice =='5':
            # Simulation
            clear_console()
            print('Program Coming')

        elif choice == '6':
            # Files
            clear_console()
            print('Program Coming')

        elif choice == '0':
            print('Thank you very much for using our program!')
            time.sleep(2)
            is_on = False


if __name__== '__main__':
    main_menu()