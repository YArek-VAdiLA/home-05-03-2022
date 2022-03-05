import sqlite3

def printBooks(record):
    print()
    print("ID:", record[0])
    print("автор:", record[1])
    print("названик:", record[2])
    print("томы:", record[3])
    print()

def createTable():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        create_table_query = '''CREATE TABLE IF NOT EXISTS book (
                                    id INTEGER PRIMARY KEY,
                                    author TEXT NOT NULL,
                                    name TEXT NOT NULL,
                                    volumes INTEGER NOT NULL

                                );'''
        cursor.execute(create_table_query)
        sqlite_connection.commit()
        print("Таблица создана успешно.")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")


def insertManyData(records):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        insert_data_query = '''INSERT INTO book ( id, author, name, volumes)
                               VALUES (?, ?, ?, ?);'''
        cursor.executemany(insert_data_query, records)
        sqlite_connection.commit()
        print("Записей успешно добавлено:", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")


def selectAuthor(author):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")
        print()

        sqlite_select_query = "SELECT * FROM book WHERE  author = ?;"
        cursor.execute(sqlite_select_query, (author,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")


def selectVolumes(volumes):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")
        print()

        sqlite_select_query = "SELECT * FROM book WHERE  volumes = ?;"
        cursor.execute(sqlite_select_query, (volumes,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")

def selectName(name):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")
        print()

        sqlite_select_query = "SELECT * FROM book WHERE  name = ? ;"
        cursor.execute(sqlite_select_query,(name,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")

def selectID(id):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")
        print()

        sqlite_select_query = "SELECT * FROM book WHERE  id = ? ;"
        cursor.execute(sqlite_select_query,(id,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")


spisok = [(1, "jack londan", "A Daughter of the Snows", 2),
          (2, "jack londan", "The Cruise of the Dazzler", 3),
          (3, "jack londan", "The Call of the Wild", 1),
          (4, "jack londan", "The Kempton-Wace Letters", 6),
          (5, "jack londan", "The Sea-Wolf", 3),
          (6, "jack londan", "The Game", 8),
          (7, "jack londan", "White Fang", 4),
          (8, "jack londan", "Before Adam", 6),
          (9, "jack londan", "The Iron Heel", 6),
          (10, "jack londan", "Martin Eden", 9),
          (11, "jack londan", "Burning Daylight", 10),
          (12, "jack londan", "Adventure", 1),
          (13, "jack londan", "The Scarlet Plague", 2),
          (14, "jack londan", "A Son of the Sun", 3),
          (15, "jack londan", " The Abysmal Brute", 7)]

createTable()
insertManyData(spisok)





