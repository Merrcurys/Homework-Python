import os
from interface.colors_print import *


def interface_user(object, user_id):
    (lambda: os.system('cls'))()
    out_blue(
        "--------------------------------ПОЧТА НЕРОССИИ--------------------------------")
    out_blue(
        "--------------------------------ВАШ КАБИНЕТ-----------------------------------")
    print("1. Изменить свои данные")
    print("2. Отследить посылки")
    print("3. Выйти")
    while True:
        answer = input("Введите номер команды: ")
        match answer:
            case "1":
                object.update_user_info(
                    [input("Введите имя: "),
                     input("Введите отчество: "),
                     input("Введите фамилию: "),
                     input("Введите адресс: "),
                     user_id])
            case "2":
                packages = object.check_parcels(user_id)
                if packages:
                    for package in packages:
                        if package[1] == "Доставлено":
                            out_green(f"Посылка: {package[0]} - {package[1]}")
                        else:
                            print(f"Посылка: {package[0]} - {package[1]}")
                else:
                    out_red("У вас нету отправленных посылок.")
            case "3":
                (lambda: os.system('cls'))()
                out_blue(
                    "--------------------------------ПОЧТА НЕРОССИИ--------------------------------")
                print("1. Войти\n2. Зарегестрироваться\n3. Выйти")
                break
            case _:
                out_red("Такой команды нету!")
