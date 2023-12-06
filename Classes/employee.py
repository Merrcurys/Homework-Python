import sqlite3 as sq
from classes.user import User
from interface.colors_print import *


class Employee(User):
    def __init__(self):
        User.__init__(self)

    # TODO: разобраться с тем что реплейс меняет ID из-за чего ломает в.к.
    def update_employee_info(self, data):
        self.cursor.execute(
            """
            REPLACE INTO Staff
            (FirstName, SecondName, Surname, Account_ID)
            VALUES (?,?,?,?)
            """, (data))
        print("Данные сотрудника были обновлены.")
        self.conn.commit()

    def __is_clients(self, id_client):
        self.cursor.execute(
            """
            Select ID_Client
            FROM Clients
            WHERE ID_Client = ?
            """, (id_client,))
        return self.cursor

    def create_parcels(self, data):
        if [client for client in self.__is_clients(data[3])]:
            if [client for client in self.__is_clients(data[4])]:
                self.cursor.execute(
                    """
                    INSERT INTO Package
                    (Name, Weight, Demension, Sender_ID, Recipient_ID, Status)
                    VALUES (?,?,?,?,?,?)
                    """, (data))
                self.conn.commit()
                print("Посылка была отправлена.")
            else:
                out_red(
                    "Получатель не был найден, попросите его занести свои данные.")
        else:
            out_red("Отправитель не был найден, попросите его занести свои данные.")

    def check_parcels(self):
        self.cursor.execute(
            f"Select Name, Status FROM Package")
        return [package for package in self.cursor]

    def cnahge_parcels(self, data):
        self.cursor.execute(
            """
            UPDATE Package
            SET Status = ?
            WHERE ID_Package = ?
            """, (data))
        self.conn.commit()
        print("Статус посылки был обновлен.")
