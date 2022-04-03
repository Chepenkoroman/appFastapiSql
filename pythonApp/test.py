import sqlite3
import io

conn = sqlite3.connect('duma2020.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS duma(
   id INT PRIMARY KEY,
   speach TEXT);
""")
conn.commit()

i = 0
listi = []

with io.open("/2020.txt", encoding="utf-8") as read_file:
    for line in read_file:
        listik = []
        stroka = " "
        i = i + 1
        stroka += line
        listik.append(i)
        listik.append(stroka)
        cur.execute("INSERT INTO duma VALUES(?, ?);", (i, stroka))
        conn.commit()
