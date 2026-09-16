import sqlite3
conn = sqlite3.connect("app.db")
# conn.execute('''
# create table demo(id integer primary key, name text)   #query to createa a new table
# ''')
# conn.execute('insert into demo(id,name) values(?,?)',(101,"a"))  #query to insert new record
# conn.commit()
rows = conn.execute('select id,name from demo').fetchall()
print(rows)