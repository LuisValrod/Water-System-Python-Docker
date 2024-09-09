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
                          '\n1.- Potable\n2.- High\n3.- Medium\n4.- LOW\n5.- Non-potable\n')