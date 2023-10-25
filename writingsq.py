import sqlite3

sqliteConnection = sqlite3.connect('SQLite_Python.db')
cursor = sqliteConnection.cursor()
sqlite_insert_query = """INSERT INTO """
count = cursor.execute(sqlite_insert_query)
sqliteConnection.commit()
