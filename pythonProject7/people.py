import sqlite3


def createTablePeople():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        create_table_query = '''CREATE TABLE IF NOT EXISTS People (
                                    PhoneNumber INTEGER NOT NULL,
                                    NamePeople TEXT NOT NULL,
                                    Surname TEXT NOT NULL,
                                    Address TEXT NOT NULL,
                                    HistoryBook INTEGER 
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

def insertManyPeople(listPeopl):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        insert_data_query = '''INSERT INTO People ( PhoneNumber , NamePeople, Surname, Address)
                               VALUES (?, ?, ?, ?);'''
        cursor.executemany(insert_data_query, listPeopl)
        sqlite_connection.commit()
        print("Записей успешно добавлено:", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")

def updateWherePhoneNumber (PhoneNumber,NamePeople):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()

        sqlite_update_query = "UPDATE People SET PhoneNumber=? WHERE NamePeople=?"
        cursor.execute(sqlite_update_query, (PhoneNumber,NamePeople))
        sqlite_connection.commit()

        cursor.close()
        print("Запись", NamePeople, "успешно изменена.")
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def updateWherenName (NamePeople,PhoneNumber):
        try:
            sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
            cursor = sqlite_connection.cursor()

            sqlite_update_query = "UPDATE People SET NamePeople=? WHERE PhoneNumber =?"
            cursor.execute(sqlite_update_query, (NamePeople, PhoneNumber))
            sqlite_connection.commit()

            cursor.close()
            print("Запись", PhoneNumber, "успешно изменена.")
        except sqlite3.Error as error:
            print("При работе с базой данных возникла ошибка:", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()


def updateWherenSurname(Surname,PhoneNumber):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()

        sqlite_update_query = "UPDATE People SET Surname=? WHERE  PhoneNumber=?"
        cursor.execute(sqlite_update_query, (Surname,PhoneNumber))
        sqlite_connection.commit()

        cursor.close()
        print("Запись", PhoneNumber, "успешно изменена.")
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def updateWherenAddress(Address,PhoneNumber):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()

        sqlite_update_query = "UPDATE People SET Address=? WHERE  PhoneNumber=?"
        cursor.execute(sqlite_update_query, (Address, PhoneNumber))
        sqlite_connection.commit()

        cursor.close()
        print("Запись", PhoneNumber, "успешно изменена.")
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def selectName(name):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")
        print()

        sqlite_select_query = "SELECT * FROM People WHERE  NamePeople = ?;"
        cursor.execute(sqlite_select_query, (name,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")

def selectSurname(Surname):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")
        print()

        sqlite_select_query = "SELECT * FROM People WHERE  Surname = ?;"
        cursor.execute(sqlite_select_query, (Surname,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")

def selectAddress(Address):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")
        print()

        sqlite_select_query = "SELECT * FROM People WHERE  Address = ?;"
        cursor.execute(sqlite_select_query, (Address,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")
def deleteWherePhoneNumber(PhoneNumber):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()

        sqlite_delete_query = "DELETE FROM People WHERE PhoneNumber=?"
        cursor.execute(sqlite_delete_query, (PhoneNumber,))
        sqlite_connection.commit()

        cursor.close()
        print("Запись", PhoneNumber, "успешно удалена.")
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

Listt=[(375298063656,"yaroslav","vdovin","s.Podrechnay,h.15"),
            (375338083257,"Apalinariy","Solomonovich","s.Evrey_street,h.16")]

createTablePeople()
insertManyPeople(Listt)

