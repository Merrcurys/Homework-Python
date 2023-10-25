import time
import random
import json


def print_output(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()


def display_clear():
    print("\033[H\033[2J")


def get_monster():
    name_monsters = ["Ларри", "Дензи", "Янс", "Крозя", "Ася", "Анс", "Керун"]

    monsters = [
        {"name": random.choice(name_monsters), "health": 2, "damage": 10},
        {"name": random.choice(name_monsters), "health": 2, "damage": 15},
        {"name": random.choice(name_monsters), "health": 2, "damage": 20},
    ]

    return random.choice(monsters)


weapons = {"меч": {"удар": 10, "защита": 25},
           "коса": {"удар": 25, "защита": 10},
           "кусаригама": {"удар": 35, "защита": 5},
           "катана": {"удар": 15, "защита": 45}}

player = {"health": 250}
reg = False
encountered_monsters = set()


def get_weapon():
    print_output("Выберите оружие: ")
    for num, weapon in enumerate(weapons):
        print_output(
            f"{num + 1}. {weapon} (удар: {weapons[weapon]['удар']}; защита: {weapons[weapon]['защита']})")
    print_output("Я выберу:")
    while True:
        try:
            player_weapon = weapons[input().lower()]
            player["damage"] = player_weapon["удар"]
            player["protection"] = player_weapon["защита"]
            break
        except KeyError:
            print_output("Введите \"название\" оружия. Попробуйте снова.")
    print_output(f"Отличный выбор!")
    time.sleep(1)


def fight():
    display_clear()
    monster = get_monster()
    encountered_monsters.add(monster['name'])
    player_hp, monster_hp = player['health'], monster['health']
    print_output(f"Вы повстречали {monster['name']}")

    while monster_hp > 0 and player_hp > 0:
        print_output(f"Здоровье {monster['name']} - {monster_hp}")
        print_output(f"Урон {monster['name']} - {monster['damage']}")
        print()
        print_output(f"Здоровье {player['name']} - {player_hp}")
        print()
        print_output(f"Ход {player['name']}:")
        print_output(f"1. Зашита - {player['protection']}")
        print_output(f"2. Удар - {player['damage']}")

        while True:
            choice = input()
            if choice == "1":
                player_hp += player['protection']
                break
            elif choice == "2":
                monster_hp -= player['damage']
                break
            else:
                print("Введите число команды!")
        if monster_hp <= 0:
            break

        display_clear()
        print_output(f"Здоровье {monster['name']} - {monster_hp}")
        print_output(f"Урон {monster['name']} - {monster['damage']}")
        print()
        print_output(f"Здоровье {player['name']} - {player_hp}")
        print()
        print_output(f"Ход {monster['name']}:")
        print_output(
            f"{monster['name']} нанес вашему здоровью {monster['damage']}")
        player_hp -= monster['damage']
        time.sleep(4)
        display_clear()

    display_clear()
    if player_hp > monster_hp:
        print(f"{player['name']} вы победили!")
    else:
        print("Вы потерпели поражение")


def main():
    global player, reg, encountered_monsters

    print_output("- О вы проснулись! Помнишь свое имя?")
    print_output("Введите имя вашего персонажа:")
    player_name = input().capitalize()
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for player_statistica in data["save"]:
            if player_statistica["name"] == player_name:
                print_output("Рад, что ты вернулся!")
                reg = True
                player = player_statistica
                player["monster"] = set(player["monster"])
                encountered_monsters |= set(player["monster"])
                break
    if not reg:
        player["name"] = player_name
        print_output(
            f"- Отлично, {player_name}. Хватай оружие и помогай! На нас напали!")
        get_weapon()
    display_clear()
    while True:
        print_output("Готовы к бою? (сразиться/отдохнуть)")
        action = input().lower()
        if action == "сразиться":
            fight()
        elif action == "отдохнуть":
            print_output(
                "- Мы пока продержим осаду без тебя, но мы будем ждать тебя!")
            if encountered_monsters:
                print_output("Твоя статистика:")
                print_output(
                    f"Встреченные монстры: {', '.join(encountered_monsters)}")
            if not reg:
                print_output(
                    f"Хотите сохранить вашего персонажа? (введите \"да\" или любую клавишу если \"нет\")")
                if input().lower() == "да":
                    with open("data.json", "r", encoding="utf-8") as file:
                        data = json.load(file)
                        player["monster"] = list(encountered_monsters)
                        data["save"].append(player)
                    with open("data.json", "w", encoding="utf-8") as file:
                        json.dump(data, file, ensure_ascii=False)
                    print_output("Ваши данные были сохранены.")
            else:
                print_output(
                    f"Сохранить вашего персонажа или удалить? (введите \"удалить\" или любую клавишу если \"сохранить\")")
                if input().lower() != "удалить":
                    with open("data.json", "r", encoding="utf-8") as file:
                        data = json.load(file)
                        for player_elem in data["save"]:
                            if player_elem["name"] == player["name"]:
                                player_elem["monster"] = list(
                                    encountered_monsters | set(player_elem["monster"]))
                                print_output("Ваши данные были сохранены.")
                                break
                else:
                    for player_elem in data["save"]:
                        if player_elem["name"] == player["name"]:
                            data["save"].remove(player_elem)
                            print_output("Ваши данные были удалены.")
                            break
                with open("data.json", "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False)
            break
        else:
            print_output(
                "Неверная команда. Попробуйте ввести: (сразиться/отдохнуть)")


if __name__ == "__main__":
    main()
