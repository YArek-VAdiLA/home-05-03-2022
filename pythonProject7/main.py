import sqlite3
#В том задании, что мы делали на прошлом занятии, и которое было на дом, нужно написать функции:
#1. Добавление книг для конкретного читателя
#2. Вывод книг, которые брал читатель(посетитель библиотеки), вместе с данными читателя соответственно
def printPeople(record):
    print()
    print("номер т:", record[0])
    print("имя:", record[1])
    print("фамилия:", record[2])
    print("адрес", record[3])
    print("история",record[4])
    print()

#def JoinBook(PhoneNumber,HistoryBook):
 #   try:
 #      sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
  #      cursor = sqlite_connection.cursor()
   #     print("База данных создана и подключена к SQLite.")
    #    print()
#
 #       sqlite_update_query = "UPDATE People SET PhoneNumber=?,HistoryBook=?"
  #      cursor.execute(sqlite_update_query, (PhoneNumber,HistoryBook))
   #     sqlite_connection.commit()
#
 #       cursor.close()
  #      print("книга добавлена в баззу")
   # except sqlite3.Error as error:
    #    print("При работе с базой данных возникла ошибка:", error)
#    finally:
 #       if sqlite_connection:
  #          sqlite_connection.close()
   #         print("Соединение с SQLite закрыто.")

#print(JoinBook(375298063656,2))

def createTable():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        create_table_query = '''CREATE TABLE IF NOT EXISTS histor (
                                    id INTEGER PRIMARY KEY,
                                    id_book INTEGER
                                    PhoneNumber_people INTEGER
                                    

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


def JoinBook(PhoneNumber):
        try:
            sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
            cursor = sqlite_connection.cursor()
            print("База данных создана и подключена к SQLite.")
            print()

            sqlite_select_query = "SELECT NamePeople,PhoneNumber,Surname,name,author FROM histor  JOIN People ON People.PhoneNumber = PhoneNumber_people JOIN book ON book.id = histor.id_book  WHERE PhoneNumber = ?;"
            cursor.execute(sqlite_select_query, (PhoneNumber,))
            records = cursor.fetchall()
            cursor.close()
            return records
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

        insert_data_query = '''INSERT INTO histor ( id,id_book,PhoneNumber)
                               VALUES (?, ?, ?);'''
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

listik=[(1,12,375338083257),
        (2,3,375298063656)]
#createTable()
print(JoinBook(375338083257))
#print(insertManyPeople(listik))

