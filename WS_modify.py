import json
import time
from clear_console import clear_console
from exit import exit

def WS_modify(water_quality):
    clear_console()

    # test there are water sources registered or a file with them
    try:
        with open('water_sources.json', 'r') as ws_json:
            wss = json.load(ws_json)
            if not wss:
                print('There is no water sources registered in the database at the moment\nBack to main menu')
                time.sleep(2)
                clear_console()
                return
    except FileNotFoundError:
        print('There is no water sources registered in the database at the moment\nBack to main menu')
        time.sleep(2)
        clear_console()
        return

    # Program if there are water sources registered

    print('--------UPDATING YOUR WATER SOURCE--------\nPrees 0 at any time to go back to he main menu\n')

    fname = ''
    l_of_wss = []
    while True:
        fname = input('Please, enter the name of the file with your water sources, plants, etc... \n')
        if fname == '0':
            exit()
            return
        try:
            with open(f'{fname}.txt') as f:
                user_s_l = f.readlines()
        except FileNotFoundError:
            print('File not found. Make sure you type the right name of the file')
        else:
            l_u_wss = input('Do you want to see a list of your water sources? (y/n)\n')
            if l_u_wss == '0':
                exit()
                return
            elif l_u_wss in ['y', 'Y']:

                for ws in user_s_l:
                    if ws.split(',')[-1].strip() == 'WSS':
                        l_of_wss.append(ws.split(',')[0])
                        print(f'- {ws.split(',')[0]}: {ws.split(',')[1]} quality; {ws.split(',')[2]} litres')
            break


    ident = input('Enter the name of water source you want to modify:\n')
    wss_change = None
    while wss_change is None:
        if ident == '0':
            exit()
            return

        elif ident in l_of_wss:
            wss_change = ident
            clear_console()

        else:
            ident = input('The name is incorrect. Make sure you use right spelling, upper/lower case and numbers\n'
                          '- You can enter the name of the water source\n'
                          '- You can press 1 to see again a list of your water sources\n'
                          '- You can  enter 0 to exit\n')
            if ident == '0':
                exit()
                return
            elif ident == '1':
                for ws in user_s_l:
                    if ws.split(',')[-1].strip() == 'WSS':
                       print(f'- {ws.split(',')[0]}: {ws.split(',')[1]} quality; {ws.split(',')[2]} litres')
                ident = input('Enter the name of your water source. Make sure you use the right spelling, upper/lower case and numbers:\n')

    print(f'You wish to modify {wss_change}')

    update = int(input('Please, tell us what you would like to do:\n'
                       '- Press 1 to update the quality\n'
                       '- Press 2 to update the quantity\n'
                       '- Press 3 to delete the water source from our system\n'
                       '- Press 0 to go back to the main menu\n'))
    while update not in range(0, 4):
        update = int(input('Please, select a valid input:\n'
                       '- Press 1 to update the quality\n'
                       '- Press 2 to update the quantity\n'
                       '- Press 3 to delete the water source from our system\n'
                       '- Press 0 to go back to the main menu\n'))

    # Update block
    while True:
        if update == 0:
            exit()
            return



# with open('luis1987.txt') as f:
#     for n in f.readlines():
#         print(n.split(",")[-1])