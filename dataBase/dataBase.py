import sqlite3

connection = sqlite3.connect("isim.db")
c = connection.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(250212, '2017-10-33', 'python',10)")
    connection.commit()

def read_db():
    c.execute("SELECT * FROM stuffToPlot")
    for raw in c.fetchall():
        print (raw)

create_table()
data_entry()
read_db()
c.close()
connection.close()
