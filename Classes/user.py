import sqlite3 as sq
from classes.registration import Registration


class User(Registration):
    def __init__(self):
        Registration.__init__(self)

    def update_user_info(self, data): #TODO: разобраться с тем что реплейс меняет п.к из-за чего ломает в.к.
        self.cursor.execute(
            """
            REPLACE INTO Clients
            (FirstName, SecondName, Surname, Address, Account_ID)
            VALUES (?,?,?,?,?)
            """, (data))
        print("Ваши данные обновлены.")
        self.conn.commit()

    def check_parcels(self, id_account):
        self.cursor.execute(
            """
            Select ID_Client
            FROM Clients
            WHERE Account_ID = ?
            """, (id_account,))

        id_client = [id for id in self.cursor][0][0]

        self.cursor.execute(
            f"Select Name, Status FROM Package WHERE Recipient_ID = {id_client} OR Sender_ID = {id_client}")

        return [package for package in self.cursor]
