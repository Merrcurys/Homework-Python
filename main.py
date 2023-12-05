from Classes.user import User
from Classes.employee import Employee
import os



def main():
    while True:
        print(
            "--------------------------------ПОЧТА НЕРОССИИ--------------------------------")
        print("1. Войти\n2. Зарегестрироваться\n3. Выйти")
        answer = int(input("Введите номер команды: "))
        match answer:
            case 1:
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
                    print("Попробуйте еще раз, логин или пароль не правильный.")
            case 2:
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
            case 3:
                break
            case _:
                print("Такой команды нету!")
        # (lambda: os.system('cls'))()


def interface_user(object, user_id):
    while True:
        print(
            "--------------------------------ПОЧТА НЕРОССИИ--------------------------------")
        print(
            "--------------------------------ВАШ КАБИНЕТ-----------------------------------")
        print("1. Изменить свои данные\n2. Отследить посылки\n3. Выйти")
        answer = int(input("Введите номер команды: "))
        match answer:
            case 1:
                object.update_user_info(
                    [input("Введите имя: "),
                     input("Введите отчество: "),
                     input("Введите фамилию: "),
                     input("Введите адресс: "),
                     user_id])
            case 2:
                packages = object.check_parcels(user_id)
                if packages:
                    for package in packages:
                        print(f"Посылка: {package[0]} - {package[1]}")
                else:
                    print("У вас нету отправленных посылок.")
            case 3:
                break
            case _:
                print("Такой команды нету!")


def interface_staff(object, user_id):
    while True:
        print(
            "--------------------------------ПОЧТА НЕРОССИИ--------------------------------")
        print(
            "--------------------------------КАБИНЕТ СОТРУДНИКА-----------------------------")
        print("1. Изменить свои данные\n2. Создать посылку\n3. Выйти")
        answer = int(input("Введите номер команды: "))
        match answer:
            case 1:
                object.update_user_info(
                    [input("Введите имя: "),
                     input("Введите отчество: "),
                     input("Введите фамилию: "),
                     user_id])
            case 2:
                package = object.create_parcels(
                    [input("Введите что в посылке: "),
                     int(input("Введите вес: ")),
                     input("Введите габариты: "),
                     int(input("Введите ID отправитля: ")),
                     int(input("Введите ID получателя: ")),
                     "Отправлена"])
            case 3:
                break
            case _:
                print("Такой команды нету!")


if __name__ == '__main__':
    main()
