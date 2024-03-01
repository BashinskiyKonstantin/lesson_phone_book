import text
import glob

THEME = "_"


def show_first_main_menu () -> int : ##### Отображение главного меню
    for i, item in enumerate (text.first_main_menu):
        if i:
            print(f'{i}.\t{item}')
        else: 
            print (f"\t{item}")
    choice = int 
    while True:
        choice = input (text.choice_first_main_menu)
        if choice.isdigit () and 0 < int (choice) < len(text.first_main_menu):
            return int(choice)
        print (text.choice_main_menu_erorr)

def show_second_main_menu () -> int : 
    for i, item in enumerate (text.second_main_menu):
        if i:
            print(f'{i}.\t{item}')
        else: 
            print (f"\t{item}")
    choice = int 
    while True:
        choice = input (text.choice_second_main_menu)
        if choice.isdigit () and 0 < int (choice) < len(text.second_main_menu):
            return int(choice)
        print (text.choice_main_menu_erorr)

def show_first_main_menu () -> int : ### Отображение главного меню
    for i, item in enumerate (text.first_main_menu):
        if i:
            print(f'{i}.\t{item}')
        else: 
            print (f"\t{item}")
    choice = int 
    while True:
        choice = input (text.choice_first_main_menu)
        if choice.isdigit () and 0 < int (choice) < len(text.first_main_menu):
            return int(choice)
        print (text.choice_main_menu_erorr)

def show_list_phone_books () -> int : ### Отображение списка справочников
    for i, item in enumerate (glob.glob("*.txt"),1):
        if i:
            print(f'{i}.\t{item}')
        else: 
            print (f"\t{item}")
 

def show_message (message: str):
    print ('\n' + THEME * len(message) + '\n' )
    print (message)
    print (THEME * len(message) + '\n')


def show_contacts (phone_book: dict[int, str], error_message: str):
     if phone_book: 
        print('\n' + THEME * 71 + '\n')
        for u_id,contacts in phone_book.items():
             print(f'{u_id:<3} {contacts[0]:<20} | {contacts[1]:<20} | {contacts[2]:<20}')
        print('\n' + THEME * 71)

     else:
         show_message(error_message)

def input_data(message) -> list[str] | str:
    if isinstance(message, str):
        return input ('\n' + message)
    return [input(mess) for mess in message]

