import sqlite3

conn = sqlite3.connect(r'/.db')
cur = conn.cursor()

cur.execute("SELECT * FROM duma;")
one_result = cur.fetchall()
print(one_result)
print(len(one_result))
