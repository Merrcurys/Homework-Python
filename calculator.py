import math
"""

ПРАКТИЧЕСКАЯ РАБОТА №1 «Инженерный калькулятор»
                   МПТ

"""
print("ИНЖЕНЕРНЫЙ КАЛЬКУЛЯТОР")
print("Меню команд:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Квадратный корень")
print("7. Факториал")
print("8. Синус")
print("9. Косинус")
print("10. Тангенс")

while True:
    try:
        command = int(input("Введите номер команды: "))  # ввод номера команды
        # Ввод одно или двух чисел
        if command in [1, 2, 3, 4, 5]:
            num_1 = float(input("Введите первое число: "))
            num_2 = float(input("Введите второе число: "))
        elif command in [6, 7, 8, 9, 10]:
            num_1 = float(input("Введите число: "))
        else:
            # проверка на существование команды
            print("Такой команды не существует, введите номерк команды еще раз.")
            continue
    except ValueError:
        # проверка на тип данных
        print("Неправильный введеный тип данных, попробуйте еще раз и введите число.")
        continue

    result = ""  # переменная с результатом

    match command:  # выполняем команду
        case 1:
            result = num_1 + num_2
        case 2:
            result = num_1 - num_2
        case 3:
            result = num_1 * num_2
        case 4:
            try:
                result = num_1 / num_2
            except ZeroDivisionError:  # проверка на ноль в знаменателе
                print("Делить на ноль нельзя, попробуйте еще раз.")
                continue
        case 5:
            result = num_1 ** num_2
        case 6:
            result = num_1 ** 0.5
        case 7:
            result = math.factorial(int(num_1))
        case 8:
            result = math.sin(num_1)
        case 9:
            result = math.cos(num_1)
        case 10:
            result = math.tan(num_1)

    print(f"Результат: {result}")  # вывод результата
    break
