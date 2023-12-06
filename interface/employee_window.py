from interface.colors_print import *
import os


def interface_staff(object, user_id):
    (lambda: os.system('cls'))()
    out_blue(
        "--------------------------------ПОЧТА НЕРОССИИ--------------------------------")
    out_blue(
        "--------------------------------КАБИНЕТ СОТРУДНИКА----------------------------")
    print("1. Изменить свои данные")
    print("2. Изменить данные пользователя")
    print("3. Отследить посылки")
    print("4. Создать посылку")
    print("5. Изменить статус посылки")
    print("6. Удалить аккаунт с данными")
    print("7. Выйти")
    #TODO: удалить посылку
    while True:
        answer = input("Введите номер команды: ")
        match answer:
            case "1":
                object.update_employee_info(
                    [input("Введите имя: "),
                     input("Введите отчество: "),
                     input("Введите фамилию: "),
                     user_id])
            case "2":  # TODO: сделать изменение данных пользователя без затрагивания его п.к.
                object.update_user_info(
                    [input("Введите имя: "),
                     input("Введите отчество: "),
                     input("Введите фамилию: "),
                     input("Введите адресс: "),
                     input("Введите ID аккаунта: ")])
            case "3":
                packages = object.check_parcels()
                if packages:
                    for package in packages:
                        if package[1] == "Доставлено":
                            out_green(f"Посылка: {package[0]} - {package[1]}")
                        else:
                            print(f"Посылка: {package[0]} - {package[1]}")
                else:
                    out_red("У вас нету отправленных посылок.")
            case "4":
                try:
                    package = object.create_parcels(
                        [input("Введите что в посылке: "),
                         int(input("Введите вес: ")),
                         input("Введите габариты: "),
                         int(input("Введите ID отправитля: ")),
                         int(input("Введите ID получателя: ")),
                         "Отправлена"])
                except (ValueError):
                    out_red("Вы ввели неправильное значение, попробуйте еще раз!")
            case "5":
                try:
                    object.cnahge_parcels(
                        [input("Введите новый статус посылки: "), int(input("Введите ID посылки: "))])
                except (ValueError):
                    out_red("Вы ввели неправильное значение, попробуйте еще раз!")
            case "6":
                # TODO: удалить акк
                pass
            case "7":
                (lambda: os.system('cls'))()
                out_blue(
                    "--------------------------------ПОЧТА НЕРОССИИ--------------------------------")
                print("1. Войти\n2. Зарегестрироваться\n3. Выйти")
                break
            case _:
                out_red("Такой команды нету!")
