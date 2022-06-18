import sqlite3
import io

conn = sqlite3.connect('duma.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS duma(
   id INT PRIMARY KEY,
   name TEXT,
   text TEXT,
   text_length INTEGER,
   text_w_length INTEGER,
   positive_prob REAL,
   negative_prob REAL,
   positive	TEXT,
   performances INTEGER,
   year INTEGER);
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


with open('/Users/romanchepenko/Desktop/diplom/duma_analysis/data/corpus/newCSV_1994.csv','r') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(int(i), i['name'], i['speach'], i['text_length'], i['text_w_length'], i['positive_prob'], i['negative_prob'], i['positive'], i['performances']) for i in dr]

cur.executemany("INSERT INTO duma (id, name, speach, text_length, text_w_length, positive_prob, negative_prob, positive, performances, year) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1994);", to_db)
con.commit()
con.close()
