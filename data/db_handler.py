import sqlite3 as sq


# создает таблицы, если они еще не созданы.
def create_data():
    with sq.connect("./data/database.db") as con:
        cur = con.cursor()

        cur.execute(  # ! таблица акков
            """
            CREATE TABLE IF NOT EXISTS Accounts (
            ID_Account   INTEGER       PRIMARY KEY AUTOINCREMENT,
            Login        VARCHAR(30)   UNIQUE  NOT NULL,
            Password     VARCHAR(30)           NOT NULL,
            If_Staff     INTEGER               NOT NULL)
            """)

        cur.execute(  # ! таблица персонала
            """
            CREATE TABLE IF NOT EXISTS Staff (
            ID_Staff     INTEGER       PRIMARY    KEY AUTOINCREMENT,
            FirstName    VARCHAR(50)              NOT NULL,
            SecondName   VARCHAR(50)              NOT NULL,
            Surname      VARCHAR(50)              NOT NULL,
            Account_ID   INTEGER       UNIQUE     NOT NULL,
            FOREIGN KEY  (Account_ID)  REFERENCES Accounts(ID_Account))
            """)

        cur.execute(  # ! таблица клиентов
            """
            CREATE TABLE IF NOT EXISTS Clients (
            ID_Client    INTEGER       PRIMARY    KEY AUTOINCREMENT,
            FirstName    VARCHAR(50)              NOT NULL,
            SecondName   VARCHAR(50)              NOT NULL,
            Surname      VARCHAR(50)              NOT NULL,
            Address      TEXT                     NOT NULL,
            Account_ID   INTEGER       UNIQUE     NOT NULL,
            FOREIGN KEY  (Account_ID)  REFERENCES Accounts(ID_Account))
            """)

        cur.execute(  # ! таблица посылок
            """
            CREATE TABLE  IF NOT EXISTS   Package (
            ID_Package    INTEGER         PRIMARY KEY AUTOINCREMENT,
            Name          VARCHAR(50)       NOT NULL,
            Weight        INTEGER         NOT NULL,
            Demension     TEXT            NOT NULL,
            Status        VARCHAR(50)     NOT NULL,
            Sender_ID     INTEGER         NOT NULL,
            Recipient_ID  INTEGER         NOT NULL,
            FOREIGN KEY   (Sender_ID)     REFERENCES Clients(ID_Client),
            FOREIGN KEY   (Recipient_ID)  REFERENCES Clients(ID_Client))
            """)
