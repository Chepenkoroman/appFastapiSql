import sqlite3

conn = sqlite3.connect(r'/Users/romanchepenko/Desktop/gitPython/appFastapiSql/pythonApp/duma.db')
cur = conn.cursor()

cur.execute("SELECT * FROM duma;")
one_result = cur.fetchall()
#print(one_result)
print(len(one_result))
