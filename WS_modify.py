import json
import time
from clear_console import clear_console
from exit import exit

def update_quality(water_quality, user_s_l, wss_change, fname):
    text_to_save = ''

    while True:
        new_quality = input('Please provide the new quality of the water of you water source\n'
                            '(Values available: POTABLE, HIGH, LOW, NON-POTABLE)\n').upper()

        if new_quality == '0':
            exit()
            return

        if new_quality in water_quality:
            break
        print('Invalid Input')

    # logic to save changes in txt file
    for ws in user_s_l:
        l_ws = ws.split(',')
        if wss_change in l_ws and l_ws[-1].strip() == 'WSS':
            l_ws[1] = new_quality

        text_to_save += ','.join(l_ws)
    with open(f'{fname}.txt', 'w') as f:
        f.write(text_to_save)

    # logic to save changes in json file
    with open('water_sources.json', 'r') as ws_json:
        wss = json.load(ws_json)
        wss[wss_change]['quality'] = new_quality
    with open('water_sources.json', 'w') as wss_json:
        json.dump(wss, wss_json, indent=4)



    clear_console()
    print(f'The water quality of {wss_change} was change to {new_quality} succesfully!\n'
          f'Going back to the main menu')
    time.sleep(2)

def update_quantity(user_s_l, wss_change, fname):
    text_to_save = ''
    new_quantity = None
    while new_quantity is None or new_quantity <= 0:
        quantity_val = input('Please, provide the new amount of your water source (Positive number)\n')

        if quantity_val == '0':
            exit()
            return

        try:
            new_quantity = int(quantity_val)
            if new_quantity <= 0:
                print('The quantity should be a positive number')
        except ValueError:
            print('The quantity should be a a positive number')

    # logic to save changes in txt file
    for ws in user_s_l:
        l_ws = ws.split(',')
        if wss_change in l_ws and l_ws[-1].strip() == 'WSS':
            l_ws[2] = str(new_quantity)
        text_to_save += ','.join(l_ws)
    with open(f'{fname}.txt', 'w') as f:
        f.write(text_to_save)

    # logic to save changes in json file
    with open('water_sources.json', 'r') as ws_json:
        wss = json.load(ws_json)
        wss[wss_change]['quantity'] = new_quantity
    with open('water_sources.json', 'w') as wss_json:
        json.dump(wss, wss_json, indent=4)

    # Confirmation
    clear_console()
    print(f'The water quantity of {wss_change} was change to {new_quantity} succesfully!\n'
          f'Going back to the main menu')
    time.sleep(2)

def delete_water_source(user_s_l, wss_change, fname):
    confirmation = input('Are you sure you want to delete your water source? (y/n)\n')
    if confirmation in ['y', 'Y']:
        text_to_save = ''

        # logic to save changes in txt file
        for ws in user_s_l:
            l_ws = ws.split(',')
            if wss_change in l_ws and l_ws[-1].strip() == 'WSS':
                continue
            text_to_save += ','.join(l_ws)

        with open(f'{fname}.txt', 'w') as f:
            f.write(text_to_save)

        # logic to save changes in json file
        with open('water_sources.json', 'r') as ws_json:
            wss = json.load(ws_json)
            wss.pop(wss_change)
        with open('water_sources.json', 'w') as wss_json:
            json.dump(wss, wss_json, indent=4)

        clear_console()
        print(f'{wss_change} was deleted successfully!\n'
              f'Going back to the main menu')
        time.sleep(2)


    else:
        print('Cancelling deletion...')
        time.sleep(1)
        exit()
        return



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
            else:
                for ws in user_s_l:
                    l_of_wss.append(ws.split(',')[0])

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

    update = input('Please, tell us what you would like to do:\n'
                       '- Press 1 to update the quality\n'
                       '- Press 2 to update the quantity\n'
                       '- Press 3 to delete the water source from our system\n'
                       '- Press 0 to go back to the main menu\n')
    while update not in ['0', '1', '2', '3']:
        update = input('Please, select a valid input:\n'
                       '- Press 1 to update the quality\n'
                       '- Press 2 to update the quantity\n'
                       '- Press 3 to delete the water source from our system\n'
                       '- Press 0 to go back to the main menu\n')

    # Update block
    while True:
        if update == '0':
            exit()
            return
        if update == '1':
            update_quality(water_quality, user_s_l, wss_change, fname)
            break

        if update == '2':
            update_quantity(user_s_l, wss_change, fname)
            break

        if update == '3':
            delete_water_source(user_s_l, wss_change, fname)
            break



# with open('luis1987.txt') as f:
#     for n in f.readlines():
#         print(n.split(",")[-1])


