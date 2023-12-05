import sqlite3 as sq
from Classes.registration import Registration


class User(Registration):
    def __init__(self):
        Registration.__init__(self)

    def update_user_info(self, data):
        self.cursor.execute(
            """
            REPLACE INTO Clients
            (FirstName, SecondName, Surname, Address, Account_ID)
            VALUES (?,?,?,?,?)
            """, (data))
        print("Данные клиента обновлены.")
        self.conn.commit()

    def delete_user_info(self, id):
        self.cursor.execute(
            "DELETE FROM Clients WHERE ID_Client = ?", (id,))
        print("Клиента обновлены.")
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
