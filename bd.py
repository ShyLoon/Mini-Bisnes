import sqlite3
import random
import re
import  openpyxl as ox
import xlsxwriter
import pandas as pd

db = sqlite3.connect("test2.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS "users" (
    "Id_users" INTEGER PRIMARY KEY,
    "username"  TEXT,
    "password"  TEXT,
    "balance_users" INTEGER)""")

sql.execute("""CREATE TABLE IF NOT EXISTS "admins" (
    "Id_admins" INTEGER PRIMARY KEY,
    "login_admin"  TEXT,
    "password_admin"  TEXT)""")

db.commit()
# db.close

id = ""
summaNach = 4180
bal = random.randint(20, 40)
balance = summaNach + round(((bal/100)*summaNach))


f = "Фарш"
t = "Помидоры"
l = "Лук"
ll = "Листы лазаньи"
ch = "Твёрдый сыр"

farsh = 300
tomato = 100
listLazan = 60
lyk = 30
cheese = 50 

countFarsh = 5
countTomato = 5
countlistLazan = 5
countLyk = 5
countCheese = 5

def dish():
    balUser = balance
    print(balUser)

    check_list = [""]
    summa = 0
    dish = 0

    print(id)

    # sql_update_balance = sql.execute(f"Update users set balance_users = '{balance}' where username = '{username}'")
    

    while True:        
        print('''
        Хелоу, что вы хотите?
        1. Собрать лозанью
        2. Узнать стоимость
        3. Покинуть заведение
        4. Получить чек''')


        user_control = input()
        if user_control == '1':
            dish += 1
            i = 0

            count = int(input("Введите количество блюд: "))


            while(True):
                print(f'''Чтобы заказть блюдо, вам нужно выбрать ингридиенты:
                1. {f}  
                2. {t}
                3. {l}
                4. {ll}
                5. {ch} 
                0. Иди готовь''')

                a = random.randint(1, 6)
                if (a == 5):
                    check_list.append('Новичок')


                if (balUser < summa):
                    print("Тебе больше ни на что не хватит, бомж")
                    
                    sql.execute(f"Update users set balance_users = '{balUser}' where Id_users = '{id}'")
                    db.commit()
                    
                    break
                
                collection = input()
                if(count > countFarsh or count > countTomato or count > countLyk or count > countlistLazan or count > countCheese):
                    print("У нас нет столько продуктов, закажите чуть меньше")
                    count = int(input("Введите количество блюд: "))
                else:
                    match collection:
                        case '1':
                            if(count == 5):
                                print('Благодарю за покупку, 5 блюдо вам в подарок')
                                check_list.append(f'{f}') 
                                summa += farsh * (count-1)
                                balUser = balUser - summa
                                print(balUser)
                            else:
                                check_list.append(f'{f}') 
                                summa += farsh * count
                                balUser = balUser - summa
                                print(balUser)
                        case '2':
                            if(count == 5):
                                print('Благодарю за покупку, 5 блюдо вам в подарок')
                                check_list.append(f'{t}') 
                                summa += tomato * (count-1)
                                balUser = balUser - summa
                                print(balUser)
                            else:
                                check_list.append(f'{t}') 
                                summa += tomato * count
                                balUser = balUser - summa
                                print(balUser)
                        case '3':
                            if(count == 5):
                                print('Благодарю за покупку, 5 блюдо вам в подарок')
                                check_list.append(f'{l}') 
                                summa += lyk * (count-1)
                                balUser = balUser - summa
                                print(balUser)
                            else:
                                check_list.append(f'{l}') 
                                summa += lyk * count
                                balUser = balUser - summa
                                print(balUser)
                        case '4':
                            if(count == 5):
                                print('Благодарю за покупку, 5 блюдо вам в подарок')
                                check_list.append(f'{ll}') 
                                summa += listLazan * (count-1)
                                balUser = balUser - summa
                                print(balUser)
                            else:
                                check_list.append(f'{ll}') 
                                summa += listLazan * count
                                balUser = balUser - summa
                                print(balUser)
                        case '5':
                            if(count == 5):
                                print('Благодарю за покупку, 5 блюдо вам в подарок')
                                check_list.append(f'{ch}') 
                                summa += cheese * (count-1)
                                balUser = balUser - summa
                                print(balUser)
                            else:
                                check_list.append(f'{ch}') 
                                summa += cheese * count
                                balUser = balUser - summa
                                print(balUser)
                        case '0':
                            b = random.randint(1,6)
                            if(b == 5):
                                print('Ой, в вашем блюде Новичок')
                                print("Приносим свои извинения(Нет), сделаем вам скидку 30%, но вы всё равно помрёте :) ")
                                summa = summa - ((summa*30)/100)
                            break
                        case default:
                            print ("Такого у нас нет")
            i += 1
            continue
        elif (user_control == '2'):
            print('Стоимость вашего блюда:', summa)
            print(list(filter(None, check_list)))
            
        elif (user_control == '3'):
            exit()
        elif (user_control == '4'):
            check_list.append(summa)
            df = pd.DataFrame(check_list)
            
            dft = df.T
            dft.to_excel('check.xlsx')

roleUser = ""


def admin():
    balanceAdmin = 1000000
    global farsh
    global tomato
    global lyk
    global listLazan
    global cheese
    while(True):
        print('''
            Хелоу, что вы хотите?
            1. Закупить товар
            2. Сменить цену состовляющих 
            3. Сменить ингридиенты в блюде
            4. Выйти''')
        
        admin_control = input()
        match admin_control:
                        case '1':
                            global countFarsh
                            global countTomato
                            global countlistLazan
                            global countLyk
                            global countCheese
                            print('''
                                    1. Фарш  
                                    2. Помидоры
                                    3. Лук
                                    4. Листы лазаньи
                                    5. Твёрдый сыр 
                                    0. Назад''')
                            tovar = input()
                            match tovar:
                                case '1':
                                    print('Сколько хотите закупить? ')
                                    count = int(input())
                                    countFarsh = countFarsh + count
                                    balanceAdmin = balanceAdmin - (count * farsh)
                                    print(countFarsh)
                                    print('Успешная закупка')
                                case '2':
                                    print('Сколько хотите закупить? ')
                                    count = int(input())
                                    countTomato = countTomato + count
                                    balanceAdmin = balanceAdmin - (count * tomato)
                                    print('Успешная закупка')
                                case '3':
                                    print('Сколько хотите закупить? ')
                                    count = int(input())
                                    countLyk = countLyk + count
                                    balanceAdmin = balanceAdmin - (count * lyk)
                                    print('Успешная закупка')
                                case '4':
                                    print('Сколько хотите закупить? ')
                                    count = int(input())
                                    countlistLazan = countlistLazan + count
                                    balanceAdmin = balanceAdmin - (count * listLazan)
                                    print('Успешная закупка')
                                case '5':
                                    print('Сколько хотите закупить? ')
                                    count = int(input())
                                    countCheese = countCheese + count
                                    balanceAdmin = balanceAdmin - (count * cheese)
                                    print('Успешная закупка')
                                case '0':
                                    break
                                case default:
                                    print ("Такого у нас нет")
                                    
                                
                        case '2':
                            
                            print('''
                                    1. Фарш  
                                    2. Помидоры
                                    3. Лук
                                    4. Листы лазаньи
                                    5. Твёрдый сыр 
                                    0. Назад''')
                            tovar = input()
                            match tovar:
                                case '1':
                                    print("Текущая цена: " + str(farsh) + " Введите нужную цену: ")
                                    farsh = int(input())
                                    print('Успешная смена цены')
                                    print(farsh)
                                case '2':
                                    print(' Текущая цена ' + str(tomato) + ' Введите нужную цену: ')
                                    tomato = int(input())
                                    print('Успешная смена цены')
                                case '3':
                                    print(' Текущая цена ' + str(lyk) + ' Введите нужную цену: ')
                                    lyk = int(input())
                                    print('Успешная смена цены')
                                case '4':
                                    print('Текущая цена ' + str(listLazan) + ' Введите нужную цену: ')
                                    listLazan = int(input())
                                    print('Успешная смена цены')
                                case '5':
                                    print('Текущая цена ' + str(cheese) + ' Введите нужную цену: ')
                                    cheese = int(input())
                                    print('Успешная смена цены')
                                case '0':
                                    break
                        case '3':
                            global f
                            global t
                            global l
                            global ll
                            global ch
                            print('''
                                    1. Фарш  
                                    2. Помидоры
                                    3. Лук
                                    4. Листы лазаньи
                                    5. Твёрдый сыр 
                                    0. Назад''')
                            tovar = input()
                            match tovar:
                                case '1':
                                    print('Выбранный ингридиент' + f + 'Введите новый: ')
                                    f = input()
                                    print('Успешная смена ингридиента')
                                case '2':
                                    print('Выбранный ингридиент' + t + 'Введите новый: ')
                                    t = input()
                                    print('Успешная смена ингридиента')
                                case '3':
                                    print('Выбранный ингридиент' + l + 'Введите новый: ')
                                    l = input()
                                    print('Успешная смена ингридиента')
                                case '4':
                                    print('Выбранный ингридиент' + ll + 'Введите новый: ')
                                    ll = input()
                                    print('Успешная смена ингридиента')
                                case '5':
                                    print('Выбранный ингридиент' + ch + 'Введите новый: ')
                                    ch = input()
                                    print('Успешная смена ингридиента')
                        case '4':
                            main()
                        case default:
                            print ("Такой возможности нет")



def reg():
    global username 
    username = input("Логин: ")
    password = input("Пасворд: ")
    sql.execute(f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}' and balance_users = '{balance}' ")
    

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (NULL,?,?,?)", (username, password, balance))
        db.commit()
        print('Вы успешно зарегистрировались')
        login()
    else:
        print('Такой пользователь уже существует')
        for i in sql.execute('SELECT * FROM users'):
            print(i)

def login():
    global username
    username = input("Логин: ")
    password = input("Пасворд: ")
    #sql_update_balance = sql.execute(f"Update users set balance_users = '{balance}' where username = '{username}'")
    a = sql.execute(f"SELECT username, password  FROM users WHERE username = '{username}' AND password = '{password}'")
    global id 
    
    
    db.commit() 
    if not sql.fetchone():
        print("Нет такой записи")
        for i in sql.execute('SELECT * FROM users'):
            print(i)
        reg()
    else:
        chars = "(),"
        id = sql.execute(f"SELECT Id_users FROM users where username = '{username}'")
        id = sql.fetchone()[0]
        #id = str.translate({ord(i): None for i in '(),'})
        roleUser = "Пользователь"
        dish()
    


def regAdm():
    login_admin = input("Логин: ")
    password_admin = input("Пасворд: ")
    sql.execute(f"SELECT login_admin, password_admin FROM admins WHERE login_admin = '{login_admin}' AND password_admin = '{password_admin}'")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO admins VALUES (NULL,?,?)", (login_admin, password_admin))
        db.commit()
        print('Вы успешно зарегистрировались')
        loginAdm()
    else:
        print('Такой админ уже существует')
        for i in sql.execute('SELECT * FROM admins'):
            print(i)

def loginAdm():
    login_admin = input("Логин: ")
    password_admin = input("Пасворд: ")
    a = sql.execute(f"SELECT login_admin, password_admin FROM admins WHERE login_admin = '{login_admin}' AND password_admin = '{password_admin}'")
    db.commit() 
    if not sql.fetchone():
        print("Нет такой записи")
        for i in sql.execute('SELECT * FROM admins'):
            print(i)
        regAdm()
    else:
        roleUser = "Админ"
        admin()
    

def main():    
    print(''' Кем хочешь быть?
    1. Покупателем
    2. Админом''')
    role = (input())
    if (role == "1"):
        print(''' Что хочешь сделать?
                1. Войти
                2. Зарегистрироваться''')
        do = input()
        if(do == "1"):
            login()
        elif(do == "2"):
            reg()
    elif (role == "2"):
        print(''' Что хочешь сделать?
                1. Войти
                2. Зарегистрироваться''')
        do = input()
        if(do == "1"):
            loginAdm()
        elif(do == "2"):
            regAdm()
    
main()








