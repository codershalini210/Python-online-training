# # create table students(sid int,name text,email text,courseid)
# import sqlite3
# conn = sqlite3.connect("app.db")
# conn.execute("Pragma foreign_keys=ON;")
# sql = '''
# create table studentsnew (sid integer primary key autoincrement,
# name text,
# email text,
# courseid integer,
# foreign key (courseid) references course(id))'''
# conn.execute(sql)
# print("table created")
# conn.commit()
# conn.close()

import sqlite3
conn = sqlite3.connect("app.db")

cur = conn.cursor()
query = "insert into studentsnew(name,email,courseid) values(?,?,?)"
cur.execute(query,('Alex','Alex@gmail.com',101))
conn.commit()
query = "select * from studentsnew"
cur.execute(query)
rows =cur.fetchall()
for row in rows:
    print(row)


conn.close()
print("record inserted")