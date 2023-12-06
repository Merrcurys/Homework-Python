import sqlite3 as sq
from classes.registration import Registration


class User(Registration):
    def __init__(self):
        Registration.__init__(self)

    def update_user_info(self, data):
        id_client = self.__if_clients(data[-1])
        if id_client:
            self.cursor.execute(
                """
            UPDATE Clients
            SET FirstName = ?, SecondName = ?, Surname = ?, Address = ?
            WHERE Account_ID = ?
            """, (data))
        else:
            self.cursor.execute(
                """
                INSERT INTO Clients
                (FirstName, SecondName, Surname, Address, Account_ID)
                VALUES (?,?,?,?,?)
                """, (data))
        print("Ваши данные обновлены.")
        self.conn.commit()

    def __if_clients(self, id_account):
        self.cursor.execute(
            """
            Select ID_Client
            FROM Clients
            WHERE Account_ID = ?
            """, (id_account,))
        return [id for id in self.cursor]

    def check_parcels(self, id_account):
        id_client = self.__if_clients(id_account)
        if id_client:
            id_client = id_client[0][0]
        else:
            id_client = -1
        self.cursor.execute(
            f"Select Name, Status FROM Package WHERE Recipient_ID = {id_client} OR Sender_ID = {id_client}")

        return [package for package in self.cursor]
