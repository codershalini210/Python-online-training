# create simple table in db
# import sqlite3
# conn =  sqlite3.connect("app.db")
# conn.execute('''
# create table course(id integer primary key autoincrement,title text)
# ''')
# print("table created")
# conn.commit()
# conn.close()

# ---------------------------
# insert record in table 
# import sqlite3
# conn = sqlite3.connect("app.db")
# query= "insert into course(title) values(?)"
# cur = conn.cursor()
# cur.execute(query,('Python Basics',))
# print("Course Added")
# conn.commit()
# conn.close()

# select data from table
# import sqlite3
# conn = sqlite3.connect("app.db")
# cur = conn.cursor()
# query = " select * from course"
# cur.execute(query)
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# conn.close()


# delete  record  from the table
# import sqlite3
# conn = sqlite3.connect("app.db")
# query= "delete from  course where id = (?)"
# cur = conn.cursor()
# cur.execute(query,(1,))
# print("Course deleted")
# conn.commit()
# conn.close()
 
# update  record  in the table
# import sqlite3
# conn = sqlite3.connect("app.db")
# query= "update  course set title=(?) where id = (?)"
# cur = conn.cursor()
# cur.execute(query,('AWS',4))
# print("Course updated")
# conn.commit()
# conn.close()