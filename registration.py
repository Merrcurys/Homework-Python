import sqlite3 as sq
from db_handler import create_data


class Registration:
    def __init__(self):
        create_data()
        self.conn = sq.connect("database.db")
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
    
    def create_account(self, login, password, if_staff):
        self.cursor.execute(
            """
            Select Login
            FROM Accounts
            WHERE Login = ?
            """, (login,))
        if not [user for user in self.cursor]:
            self.cursor.execute(
                """
                INSERT INTO Accounts
                (Login, Password, If_Staff)
                VALUES (?,?, ?)
                """, (login, password, if_staff))
            print("Клиент добавлен.")
            self.conn.commit()
        else:
            print("Вы уже зарегестрированы!")
