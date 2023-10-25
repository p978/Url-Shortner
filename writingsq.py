import sqlite3
def write(code):
    sqliteConnection = sqlite3.connect('urls.db')
    cursor = sqliteConnection.cursor()
    count = cursor.execute("INSERT INTO urls (key) VALUES(?)", (code,))
    sqliteConnection.commit()
