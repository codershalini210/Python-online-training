import sqlite3
conn = sqlite3.connect("app.db")
ch = ''
cur = conn.cursor()
while(ch!='E'):
    ch = input('''
    press: \n 1: for insert new record \n 2: for select data
    \n3 for update \n 4 for delete \n E for exit''')
    if(ch=="1"):
        # insert case here
        query= "insert into course(title) values(?)"
        coursename = input("Enter course name to insert")
        cur.execute(query,(coursename,))
        print("Course Added")
        conn.commit()
    elif(ch=="2"):
        # select case here
        query = "select * from course"
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows :
            print(row)

    elif(ch=="3"):
        #update case 
        query= "update course set title=? where id = ?"
        id = input("Enter course id where you want to update")
        coursename = input("Enter new value for course title")
        cur.execute(query,(coursename,id))
        print("Course updated ")
        conn.commit()
    elif(ch=="4"):
        # Delete case
        
        query= "delete from  course  where id = ?"
        id = input("Enter course id which you want to delete")
        # coursename = input("Enter new value for course title")
        cur.execute(query,(id,))
        print("Course deleted ")
        conn.commit()
    else:
        ch='E'
conn.close()
