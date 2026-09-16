# with open("demo.txt","r") as f:
#     # content = f.read()    # read methods stores entire file content as a string
#     for line in f:
#         print(line) 
#     # print(content)  
import csv
with open("salescsv.csv","r") as file:
    reader =csv.DictReader(file)
    for row in reader:
        print(row)