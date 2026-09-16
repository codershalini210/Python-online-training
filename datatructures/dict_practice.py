students = [
    {"name":"John","Marks":85},
    {"name":"Ron","Marks":42},
    {"name":"Sam","Marks":26},
    {"name":"Maria","Marks":95},
    {"name":"Mathew","Marks":75},
]

# for student in students:
    
#     if(student["Marks"]>40):
#         print(f" name : {student['name']}, result : Pass , marks : {student['Marks']}")

passlist=[]
faillist=[] 
for student in students:
    if(student["Marks"]>40):
        # passlist.append(student)
        passlist.append(f" {student['name']} : {student['Marks']}")
    else:
        # faillist.append(student)
        faillist.append(f" {student['name']}  : {student['Marks']}")
print("All students ",students)
print("pass students ",passlist)
print("Failed students",faillist)
print(f"total students ={len(students)} pass students = {len(passlist)} fail students ={len(faillist)}")