
import json
import time
from clear_console import clear_console
from exit import exit

def update_efficiency(efficiency, user_s_l, wtp_change, fname):
    text_to_save = ''

    while True:
        new_efficiency = input('Please provide the new efficiency of your water treatment plant\n'
                            '(Values available: HIGH, MEDIUM, LOW\n').upper()

        if new_efficiency == '0':
            exit()
            return

        if new_efficiency in efficiency:
            break
        print('Invalid Input')

    # logic to save changes in txt file
    for wtp in user_s_l:
        l_wtp = wtp.split(',')
        if wtp_change in l_wtp and l_wtp[-1].strip() == 'WTP':
            l_wtp[1] = new_efficiency

        text_to_save += ','.join(l_wtp)
    with open(f'{fname}.txt', 'w') as f:
        f.write(text_to_save)

    # logic to save changes in json file
    with open('water_treatment_plants.json', 'r') as wtp_json:
        wtps = json.load(wtp_json)
        wtps[wtp_change]['efficiency'] = new_efficiency
    with open('water_treatment_plants.json', 'w') as wtp_json:
        json.dump(wtps, wtp_json, indent=4)



    clear_console()
    print(f'The efficiency of {wtp_change} was change to {new_efficiency} succesfully!\n'
          f'Going back to the main menu')
    time.sleep(2)

def update_quantity(user_s_l, wtp_change, fname):
    text_to_save = ''
    new_quantity = None
    while new_quantity is None or new_quantity <= 0:
        quantity_val = input('Please, provide the new amount that your water treatment plant can treat (Positive number)\n')

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
    for wtp in user_s_l:
        l_wtp = wtp.split(',')
        if wtp_change in l_wtp and l_wtp[-1].strip() == 'WTP':
            l_wtp[2] = str(new_quantity)
        text_to_save += ','.join(l_wtp)
    with open(f'{fname}.txt', 'w') as f:
        f.write(text_to_save)

    # logic to save changes in json file
    with open('water_treatment_plants.json', 'r') as wtp_json:
        wtps = json.load(wtp_json)
        wtps[wtp_change]['quantity'] = new_quantity
    with open('water_treatment_plants.json', 'w') as wtp_json:
        json.dump(wtps, wtp_json, indent=4)

    # Confirmation
    clear_console()
    print(f'The quantity that water treatment plant {wtp_change} can treat was change to {new_quantity} succesfully!\n'
          f'Going back to the main menu')
    time.sleep(2)

def delete_water_source(user_s_l, wtp_change, fname):
    confirmation = input('Are you sure you want to delete your water source? (y/n)\n')
    if confirmation in ['y', 'Y']:
        text_to_save = ''

        # logic to save changes in txt file
        for wtp in user_s_l:
            l_wtp = wtp.split(',')
            if wtp_change in l_wtp and l_wtp[-1].strip() == 'WTP':
                continue
            text_to_save += ','.join(l_wtp)

        with open(f'{fname}.txt', 'w') as f:
            f.write(text_to_save)

        # logic to save changes in json file
        with open('water_treatment_plants.json', 'r') as wtp_json:
            wtps = json.load(wtp_json)
            wtps.pop(wtp_change)
        with open('water_treatment_plants.json', 'w') as wtp_json:
            json.dump(wtps, wtp_json, indent=4)

        clear_console()
        print(f'{wtp_change} was deleted successfully!\n'
              f'Going back to the main menu')
        time.sleep(2)


    else:
        print('Cancelling deletion...')
        time.sleep(1)
        exit()
        return



def WTP_modify(efficiency):
    clear_console()

    # test there are water treatment plants registered or a file with them
    try:
        with open('water_treatment_plants.json', 'r') as wtp_json:
            wtps = json.load(wtp_json)
            if not wtps:
                print('There is no water treatment plants registered in the database at the moment\nBack to main menu')
                time.sleep(2)
                clear_console()
                return
    except FileNotFoundError:
        print('There is no water treatment plants registered in the database at the moment\nBack to main menu')
        time.sleep(2)
        clear_console()
        return

    # Program if there are water treatment plants registered

    print('--------UPDATING YOUR WATER TREATMENT PLANT--------\nPrees 0 at any time to go back to he main menu\n')

    fname = ''
    l_of_wtps = []
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
            l_u_wtps = input('Do you want to see a list of your water sources? (y/n)\n')
            if l_u_wtps == '0':
                exit()
                return
            elif l_u_wtps in ['y', 'Y']:

                for wtp in user_s_l:
                    if wtp.split(',')[-1].strip() == 'WTP':
                        l_of_wtps.append(wtp.split(',')[0])
                        print(f'- {wtp.split(',')[0]}: The efficiency is {wtp.split(',')[1]}; {wtp.split(',')[2]} litres')
            else:
                for wtp in user_s_l:
                    if wtp.split(',')[-1].strip() == 'WTP':
                        l_of_wtps.append(wtp.split(',')[0])

            break


    ident = input('Enter the name of water treatment plant you want to modify:\n')
    wtp_change = None
    while wtp_change is None:
        if ident == '0':
            exit()
            return

        elif ident in l_of_wtps:
            wtp_change = ident
            clear_console()

        else:
            ident = input('The name is incorrect. Make sure you use right spelling, upper/lower case and numbers\n'
                          '- You can enter the name of the water treatment plant\n'
                          '- You can press 1 to see again a list of your water treatment plants\n'
                          '- You can  enter 0 to exit\n')
            if ident == '0':
                exit()
                return
            elif ident == '1':
                for wtp in user_s_l:
                    if wtp.split(',')[-1].strip() == 'WTP':
                       print(f'- {wtp.split(',')[0]}: The efficiency is {wtp.split(',')[1]}; {wtp.split(',')[2]} litres')
                ident = input('Enter the name of your water treatment plant. Make sure you use the right spelling, upper/lower case and numbers:\n')

    print(f'You wish to modify {wtp_change}')

    update = input('Please, tell us what you would like to do:\n'
                       '- Press 1 to update the efficiency\n'
                       '- Press 2 to update the quantity\n'
                       '- Press 3 to delete the water treatment plant from our system\n'
                       '- Press 0 to go back to the main menu\n')
    while update not in ['0', '1', '2', '3']:
        update = input('Please, select a valid input:\n'
                       '- Press 1 to update the efficiency\n'
                       '- Press 2 to update the quantity\n'
                       '- Press 3 to delete the water treatment plant from our system\n'
                       '- Press 0 to go back to the main menu\n')

    # Update block
    while True:
        if update == '0':
            exit()
            return
        if update == '1':
            update_efficiency(efficiency, user_s_l, wtp_change, fname)
            break

        if update == '2':
            update_quantity(user_s_l, wtp_change, fname)
            break

        if update == '3':
            delete_water_source(user_s_l, wtp_change, fname)
            break
