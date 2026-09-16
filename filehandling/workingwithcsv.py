# import csv 
# rows =[
#     ["id","name","age"],
#     [101,"Alex",14],
#     [102,"Alexa",15],
#     [103,"sam",13],
#     [104,"john",11],
# ]
# with open("./data/students.csv","w",newline="") as f :
#     writer = csv.writer(f)
#     writer.writerows(rows)
# print("data added to students.csv")
# .............................
import csv
with open("./data/students.csv","r",newline="") as f :
    reader =csv.DictReader(f)
    for row in reader:
        # print(row)
        msg = f"{row['id']}, {row['name']}, {row['age']}"
        print(msg,"\n")