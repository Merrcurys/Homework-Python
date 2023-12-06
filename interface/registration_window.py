from classes.user import User
from classes.employee import Employee
from interface.employee_window import interface_staff
from interface.user_window import interface_user
from interface.colors_print import *
import os


def interface_registration():
    (lambda: os.system('cls'))()
    out_blue(
        "--------------------------------ПОЧТА НЕРОССИИ--------------------------------")
    print("1. Войти\n2. Зарегестрироваться\n3. Выйти")
    while True:
        answer = input("Введите номер команды: ")
        match answer:
            case "1":
                print("Введите логин и пароль:")
                login = input("Логин: ")
                password = input("Пароль: ")
                object = User()
                user_id = object.loggin(login, password)
                if user_id:
                    if user_id[0][1]:
                        interface_staff(Employee(), user_id[0][0])
                    else:
                        interface_user(object, user_id[0][0])
                else:
                    out_red("Попробуйте еще раз, логин или пароль не верный.")
            case "2":
                print("Введите логин и пароль:")
                login = input("Логин: ")
                password = input("Пароль: ")
                unique_key = input(
                    "Введите ключ (если не знаете - пропустите): ")
                if unique_key == "112233":
                    object = Employee()
                    user = object.create_account(login, password, 1)
                else:
                    object = User()
                    user = object.create_account(login, password, 0)
            case "3":
                break
            case _:
                out_red("Такой команды нету!")
