# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def add_record():
    global last_id, all_data
    name = (input ("Введите ФИО: "))
    number = (input ("Введите номер телефона: "))
    if check(name + " " + number):
        last_id += 1
        all_data.append(str(last_id) + " " + name + " " + number)
        file = open('base.txt', 'w', encoding="utf-8")
        for string in all_data:
            file.write(string+"\n")
        file.close()
    else:
        print ("Такая запись уже существует")

def check(string):
    for str in all_data:
        if string.lower() in str.lower():
            return False
    return True

def search_record():
    search = (input ("Что будем искать? "))
    check = True
    for string in all_data:
        if search.lower() in string.lower():
            print(string)
            check = False
    if check:
        print ("Значение не найдено")

def change():
    global all_data
    search = (input ("Что будем менять? "))
    for i in range (len(all_data)):
        if all_data[i].lower().find(search.lower())>0:
            answer = int (input ("Вы хотите изменить эту запись?\n" + 
                    all_data[i] +"\n" +
                    "1. Да \n" 
                    "2. Нет, другую \n"
                    "3. Я передумал, ничего не буду менять \n"))
            if (answer == 1):
                new_string = (all_data[i].split()[0]+" "+input ("Введите новое значение: "))
                all_data[i] = new_string
                file = open('base.txt', 'w', encoding="utf-8")
                for string in all_data:
                    file.write(string+"\n")
                file.close()
            if (answer == 2):
                change()
    



def delete():
    global last_id, all_data

    search = input ("Введите значение (или  его часть), которое нужно удалить из списка: ")
    for string in all_data:
        if string.lower().find(search.lower())>0:
            answer = int (input ("Вы хотите удалить эту запись?\n" + 
                    string +"\n" +
                    "1. Да \n" 
                    "2. Нет \n"))
            if (answer == 1):
                all_data.remove(string)
    
    file = open('base.txt', 'w', encoding="utf-8")
    for string in all_data:
        file.write(string+"\n")
    file.close()


def delete_all():
    global last_id, all_data
    answer = int (input("Вы уверены:\n"
                       "1. Да\n"
                       "2. Нет\n"))
    if answer == 1:              
        file = open('base.txt', 'w', encoding="utf-8")
        last_id = 0
        all_data.clear()
        file.close()
        
def exp(name):
    newfile=name+'.txt'
    if not path.exists(newfile):
        with open(newfile, "w", encoding="utf-8") as _:
            pass
    file = open(newfile, 'w', encoding="utf-8")
    for string in all_data:
        file.write(string+"\n")
    file.close()


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Delete all\n"
                       "7. Exp/Imp\n"
                       "8. Exit\n")
                       
        match answer:
            case "1":
                show_all()
            case "2":
                add_record()
            case "3":
                search_record()
            case "4":
                change()
            case "5":
                delete()
            case "6":
                delete_all()
            case "7":
                exp(input("Введите имя файла для экспорта базы: "))
            case "8":
                play = False
            case _:
                print("Try again!\n")


main_menu()