import csv, sqlite3


con = sqlite3.connect("duma.db")
cur = con.cursor()
## cur.execute("CREATE TABLE duma (id, name, text, text_length, text_w_length, positive_prob, negative_prob, positive, performances, year);") #Table & column names 
o = 0
with open('/Users/romanchepenko/Desktop/diplom/duma_analysis/data/corpus/newCSV_2022.csv','r') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['name'], i['text'], i['text_length'], i['text_w_length'], i['positive_prob'], i['negative_prob'], i['positive'], i['performances'], '2022') for i in dr]

cur.executemany("INSERT INTO duma (id, name, text, text_length, text_w_length, positive_prob, negative_prob, positive, performances, year) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()
