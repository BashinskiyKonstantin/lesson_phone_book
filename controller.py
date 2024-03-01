import view
import model
import text
import os 
import glob

def find_contacts(message):
    search_word = view.input_data(message)
    result = model.find_contact(search_word)
    view.show_contacts(result, text.find_contact_no_result(search_word))
    return True if result else False

def first_main_menu_for_app(): ################### Функция для работы с несколькими справочниками
    while True:
        first_user_choice = view.show_first_main_menu()  ### Отображение главного меню
        match first_user_choice:
            case 1: ##### Создание нового справочника
                model.create_phone_book()
                view.show_message(text.phone_books_created)
            case 2:
                print ('\n')
                view.show_list_phone_books () ### Отображение списка справочников
                print ('\n')
            case 3: ###### Выбор справочника для работы
                phone_book = int(input("Введите порядковый номер справочника: "))-1
                path = glob.glob("*.txt")[phone_book] ### Переменная для перемещения по справочникам
                start_app(path)
            case 4: ###### Удаление справочника
                phone_book = int(input("Введите порядковый номер справочника для удаления: "))-1
                os.remove(f"{glob.glob("*.txt")[phone_book]}")
                view.show_message(text.phone_books_deleted)
            case 5:
                break

def start_app(path):
    while True:
        second_user_choice = view.show_second_main_menu()
        match second_user_choice:
            case 1: 
                model.open_phone_book(path)
                view.show_message(text.phone_book_opened_succefull)
            case 2: 
                model.save_phone_book(path,view.show_message(text.phone_book_saved_succefull))
            case 3: 
                view.show_contacts(model.phone_book, text.empty_phone_book_erorr)
            case 4: 
                new_contact = view.input_data(text.input_new_contact)
                model.add_new_contanct(new_contact)
                view.show_message(text.new_contact_added_successful(new_contact[0]))
            case 5:  
                find_contacts(text.input_search_word)
            case 6: 
                if find_contacts(text.input_search_word_for_edit):
                    u_id = int(view.input_data(text.input_id_for_edit))
                    edited_contact = view.input_data(text.edit_contact)
                    name = model.eddit_contact(u_id, edited_contact)
                    view.show_message(text.edit_contact_succeful(name))
            case 7: 
                if find_contacts(text.input_search_word_for_delete):
                    u_id = int(view.input_data(text.input_id_for_delete))
                    name = model.delete_contact(u_id)
                    view.show_message(text.delet_contact_succeful(name))
            case 8: ############################## Импорт (до красоты не успел довести)
                    print ('\n')
                    view.show_list_phone_books ()
                    choice = int(input('\n'"Введите порядковый номер телефонной книги, которую хотите импортировать: "))-1
                    path_2 = glob.glob("*.txt")[choice]
                    with open (path_2, 'r') as first, open (path, 'a') as second:
                                    for line in first:
                                        second.write(line)
                    view.show_message(text.import_phone_book)
            case 9: 
                break
first_main_menu_for_app()