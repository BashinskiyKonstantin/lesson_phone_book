

first_main_menu = ['Главное меню:', ##### Главное меню
             'Создать новый справочник',
             'Отобразить список справочников',
             'Выбрать справочник для работы',
             'Удалить справочник',
             'Выйти из программы']

second_main_menu = ['Главное меню работы со справочником:',
             'Открыть телефонную книгу',
             'Сохранить телефонную книгу',
             'Показать контакты',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Импортировать содержимое другой телефонной книги',
             'Выход']

input_search_word = "Введите слово для поиска: "
input_search_word_for_edit = "Введите слово для поиска контакта для изменения: "
input_search_word_for_delete = "Введите слово для поиска контакта для удаления: "
input_id_for_edit = "Введите порядковый номер контакта для изменения: "
input_id_for_delete = "Введите порядковый номер контакта для удаления: "
import_phone_book = "Данные из справочника успешно импортированы!"
choice_first_main_menu = f"Выберите пункт меню ({1}-{len(first_main_menu)-1}): "
choice_second_main_menu = f"Выберите пункт меню ({1}-{len(second_main_menu)-1}): "
choice_main_menu_erorr = f"Ошибка выбора пункта меню!"
phone_books_created = "Телефонная книга успешно создана!"
phone_books_deleted = "Телефонная книга успешно удалена!"
phone_book_opened_succefull = "Телефонная книга открыта успешно!"
phone_book_saved_succefull = "Телефонная книга сохранена успешно!" 
empty_phone_book_erorr = "Телефонная книга пуста или не открыта!"

input_new_contact = ["Введите имя контакта: ",
                     "Введите номер контакта: ",
                     "Введите комментарий для контакта: "]

no_changes = "Или ENTER, чтобы оставить без изменений"

edit_contact = [f"Введите новое имя {no_changes}: ",
                f"Введите новый телефон {no_changes}: ",
                f"Введите новый комментарий {no_changes}: "]

def new_contact_added_successful(name: str ) -> str:
    return f"Контакт '{name}' успешно добавлен!"

def find_contact_no_result(word: str) -> str:
    return F'Контакты содержащие "{word}" не найдены!'

def edit_contact_succeful(name) -> str:
    return f'Контакт "{name}" успешно изменен! '

def delet_contact_succeful(name) -> str:
    return f'Контакт "{name}" успешно удален! '