import json
from clear_console import clear_console
from exit import exit

def WTP_register(efficiency):
    clear_console()
    register_is_on = True
    while register_is_on:
        print('-------------------REGISTER NEW WATER TREATMENT PLANT-------------------\n'
              'Press 0 at any time to go back to the main menu.')
        try:
            with open('water_treatment_plants.json') as data:
                wtps = json.load(data)
                wtps_ids = [idn for idn in wtps]
        except FileNotFoundError:
            wtps_ids = []

        ident = input('Please, provide a name/id for your water treatment plant\n')

        if ident == '0':
            exit()
            return

        while len(ident) < 3 or ident in wtps_ids or not ident.isalnum():
            if ident == '0':
                exit()
                return
            if ident in wtps_ids:
                ident = input('That id already exists. Choose a different one:\n')
            elif not ident.isalnum():
                ident = input(
                    'The id should have just alphanumeric characters (Letters or numbers). Choose a different one\n')
            else:
                ident = input('The id should be at least 3 characters long. Choose a different one\n')

        w_efficiency = input('Now, you should tell us how efficient if your treatment plant:\n'
                          '1.- High\n2.- Medium\n3.- Low\n').upper()

        while w_efficiency not in efficiency:
            if w_efficiency == '0':
                exit()
                return
            w_efficiency = input('Efficiency just can take the following values: High, Medium, Low\n').upper()

        quantity = None
        while quantity is None or quantity <= 0:
            quantity_val = input('How many litres can your water treatment plant treat? (Positive number)\n')

            if quantity_val == '0':
                exit()
                return

            try:
                quantity = int(quantity_val)
                if quantity <= 0:
                    print('The quantity should be a value greater than 0')
            except ValueError:
                print('The quantity should be a a positive number')

        print(f'Thank you very much, your water treatment plant is {ident}, the efficiency is {w_efficiency} '
              f'and the amount of litres it can'
              f'treat is {quantity} litres')

        # Logic to save the water source in a json file

        new_wtp = {
            ident: {
                'efficiency': w_efficiency,
                'quantity': quantity,
                'quantity_used': 0,
                'potable_available': 0,
                'usage': 0,
                'type': 'WTP'
            }
        }

        while True:
            filename = input(
                'To proceed, with need a name/id that we will use for references to your personal records.\n'
                'What is the name of your file? (This name is necessary to open a file or create a  new one)\n')
            if filename == '0':
                exit()
                return
            if not filename.isalnum() or len(filename) < 3:
                print('Try to use a meaningful name. Just letters or numbers, minimum 3 characters')
            else:
                with open(f'{filename}.txt', 'a') as f:
                    f.write(f'{ident},{w_efficiency},{quantity},0,0,0,WTP\n')
                break

        try:
            with open('water_treatment_plants.json', 'r') as wtps_json:
                wtps = json.load(wtps_json)
                wtps.update(new_wtp)
        except FileNotFoundError:
            with open('water_treatment_plants.json', 'w') as wtps_json:
                json.dump(new_wtp, wtps_json, indent=4)
        else:
            with open('water_treatment_plants.json', 'w') as wtps_json:
                json.dump(wtps, wtps_json, indent=4)

        new_register = input('Would you like to register another water treatment plant? (y/n)\n')

        if new_register in ['y', 'Y']:
            pass

        else:
            # register_is_on = False
            exit()
            return


