import sqlite3 as sq
from data.db_handler import create_data
from interface.colors_print import *


class Registration:
    def __init__(self):
        create_data()
        self.conn = sq.connect("./data/database.db")
        self.cursor = self.conn.cursor()

    def loggin(self, login, password):
        self.cursor.execute(
            """
            Select ID_Account, If_Staff
            FROM Accounts
            WHERE Login = ? AND Password = ?
            """, (login, password))
        user = [user for user in self.cursor]
        return user

    def __if_login(self, login):
        self.cursor.execute(
            """
            Select Login
            FROM Accounts
            WHERE Login = ?
            """, (login,))
        return self.cursor

    def create_account(self, login, password, if_staff):
        if not [user for user in self.__if_login(login)]:
            self.cursor.execute(
                """
                INSERT INTO Accounts
                (Login, Password, If_Staff)
                VALUES (?,?, ?)
                """, (login, password, if_staff))
            print("Вы зарегестрировались.")
            self.conn.commit()
        else:
            out_red("Вы уже зарегестрированы!")
