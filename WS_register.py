import json
from clear_console import clear_console
from exit import exit

def WS_register(water_quality):
    clear_console()
    register_is_on =  True
    while register_is_on:
        print('-------------------REGISTER NEW WATER SOURCE-------------------\n'
              'Press 0 at any time to go back to the main menu.')
        try:
            with open('water_sources.json') as data:
                wss = json.load(data)
                wss_ids = [idn for idn in wss]
        except FileNotFoundError:
            wss_ids=[]

        ident = input('Please, provide a name/id for your water source\n')

        if ident == '0':
            exit()
            return

        while len(ident) < 3 or ident in wss_ids or not ident.isalnum():
            if ident == '0':
                exit()
                return
            if ident in wss_ids:
                ident=  input('That id already exists. Choose a different one:\n')
            elif not ident.isalnum():
                ident = input('The id should have just alphanumeric characters (Letters or numbers). Choose a different one\n')
            else:
                ident = input('The id should be at least 3 characters long. Choose a different one\n')

        w_quality = input('Now, you should tell us what is the water quality of your water source:\n'
                          '1.- Potable\n2.- High\n3.- Medium\n4.- Low\n5.- Non-potable\n').upper()

        while w_quality not in water_quality:
            if w_quality == '0':
                exit()
                return
            w_quality = input('Water quality just can take the following values: Potable, High, Medium, Low and '
                              'Non-potable\n').upper()

        quantity = None
        while quantity is None or quantity <= 0:
            quantity_val = input('How many litres does you water source hold? (Positive number)\n')

            if quantity_val == '0':
                exit()
                return

            try:
                quantity = int(quantity_val)
                if quantity <= 0:
                  print('The quantity should be a value greater than 0')
            except ValueError:
                print('The quantity should be a a positive number')

        print(f'Thank you very much, your water source is {ident}, the quality is {w_quality} and the quantity is'
              f' {quantity} litres')

        # Logic to save the water source in a json file

        new_wss = {
            ident: {
                'quality': w_quality,
                'quantity': quantity,
                'usage': 0,
                'type': 'WSS'
            }
        }

        while True:
            filename = input('To proceed, with need a name/id that we will use for references to your personal records.\n'
                'What is the name of your file? (This name is necessary to open a file or create a  new one)\n')
            if filename == '0':
                exit()
                return
            if not filename.isalnum() or len(filename)<3:
                print('Try to use a meaningful name. Just letters or numbers, minimum 3 characters')
            else:
                with open(f'{filename}.txt', 'a') as f:
                    f.write(f'{ident},{w_quality},{quantity},0,WSS\n')
                break



        try:
            with open('water_sources.json', 'r') as wss_json:
                wss = json.load(wss_json)
                wss.update(new_wss)
        except FileNotFoundError:
            with open('water_sources.json', 'w') as wss_json:
                json.dump(new_wss, wss_json, indent=4)
        else:
            with open('water_sources.json', 'w') as wss_json:
                json.dump(wss, wss_json, indent=4)





        new_register = input('Would you like to register another water source? (y/n)\n')

        if new_register in ['y', 'Y']:
            pass

        else:
            register_is_on = False
            exit()
            return




                