phone_book=[]
path='phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book

def update_phone_book(new_contact:list):
    global phone_book
    phone_book.append(new_contact)


def open_phone_book():
    global phone_book
    global path
    with open(path,'r',encoding='UTF-8') as file:
        data=file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))

def save_phone_book():
    global phone_book
    global path
    temp=[]
    for line in phone_book:
        temp.append(";".join(line))
    with open(path,'w',encoding='UTF-8') as file:
        temp=file.write('\n'.join(temp))

def search_contact(search:str):
    global phone_book
    search_results=[]
    for line in phone_book:
        for field in line:
            if search in field:
                search_results.append(line)
                break
    return search_results
    
def delete_contact(records_list:list,confirmation:str):
    global phone_book
    if 'y' in confirmation.lower():
        for i in range(len(records_list)):
            for j in range(len(phone_book)):
                if records_list[i]==phone_book[j]:
                    phone_book.pop(j)
                    response='Удаление произведено успешно!'
                    break
        return response
    else:
        response='Операция удаления отменена.'
        return response

def search_contact_far_changes(search:str): 
    # отличие от основного поиска в том, что в поиске для изменения нам нужно только один контакт найти
    global phone_book
    search_results=[]
    for line in phone_book:
        for field in line:
            if search in field:
                search_results.append(line)
                return search_results
    
def change_contact(record_list:list,confirmation:str,new_contact:list):
    if 'y' in confirmation.lower():
        for i in range(len(record_list)):
            for j in range(len(phone_book)):
                if record_list[i]==phone_book[j]:
                    phone_book[j]=new_contact
                    response='Изменение произведено успешно!'
                    break
        return response
    else:
        response='Операция изменения отменена.'
        return response
