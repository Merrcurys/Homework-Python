import sqlite3 as sq
from registration import Registration


class Employee(Registration):
    def __init__(self):
        Registration.__init__(self)

    def update_employee_info(self, data):
        self.cursor.execute(
            """
            REPLACE INTO Staff
            (FirstName, SecondName, Surname, Account_ID)
            VALUES (?,?,?,?)
            """, (data))
        print("Данные клиента обновлены.")
        self.conn.commit()

    def delete_employee_info(self, id):
        self.cursor.execute(
            "DELETE FROM Clients WHERE ID_Client = ?", (id,))
        print("Клиента обновлены.")
        self.conn.commit()

    def create_parcels(self, data):
        self.cursor.execute(
            """
            INSERT INTO Package
            (Name, Weight, Demension, Sender_ID, Recipient_ID, Status)
            VALUES (?,?,?,?,?,?)
            """, (data))
        self.conn.commit()
        print("добавлено")
