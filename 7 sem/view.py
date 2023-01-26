def show_menu():
    print("""    Меню:
    1-показать все контакты  
    2-открыть телефонную книгу 
    3-сохранить телефонную книгу 
    4-новый контакт 
    5-изменить контакт 
    6-удалить контакт
    7-найти контакт
    8-выйти из программы
    """)
    return int(input("Введите команду: "))

def goodbye():
    print('Работа программы завершена.')

def show_contacts(phone_book:list):
    if len(phone_book)>0:
        for item in phone_book:
            print(*item)
    else:
        print('Телефонная книга пуста!')

def load_success():
    print('Телефонная книга загружена!')

def create_new_contact():
    name=input('Имя: ')
    phone_numb=input('Телефон: ')
    comment=input('Комментарий: ')
    return name, phone_numb,comment

def update_success():
    print('Телефонная книга обновлена!')

def save_success():
    print('Телефонная книга сохранена в файл!')

def find_what():
    return input('Введите поисковой запрос и нажмите Enter: ')

def show_and_confirm__deletion(records_list:list):
    if len(records_list)>0:
        for item in records_list:
            print(*item)
    else:
        print('По запросу не найдено записей в телефонной книге!')
        return 'n'
    return input('Подтвердите удаление...(y/n): ')
def deletion_success(response):
    print(response)

def show_and_confirm_changes(records_list:list):
    if len(records_list)>0:
        for item in records_list:
            print(*item)
    else:
        print('По запросу не найдено записей в телефонной книге!')
        return 'n'
    return input('Подтвердите изменение...(y/n): ')


def deletion_success(response):
    print(response)

def change_success(response):
    print(response)
