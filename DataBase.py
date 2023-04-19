import sqlite3
from sqlite3 import Error


def create_conection():
    try:
        sqlite = sqlite3.connect('Base_news.db')

        return sqlite

    except Error as error:
        print("Ошибка при подключении к sqlite", error)




def create_table(sqlite):
    sqlite.cursor()
    sqlite.execute("CREATE TABLE IF NOT EXISTS Vkontakte(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                   "number_group integer, number_post integer, date text, data text,"
                   "theme text, url text)")
    sqlite.commit()
    if sqlite:
        sqlite.close()
        print("Соединение с SQLite закрыто")

create_conection()
create_table(create_conection())


