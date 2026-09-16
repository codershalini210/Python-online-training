# with open("./data/first.txt","w") as f:
#     f.write("now executing this code once again \n this is demo")
# print("file written successfully") 
# --------------------
# with open("./data/first.txt","r") as f:
#     content = f.read()     #read method reads whole content as once
#     print(content) 
# ............................
# with open("./data/first.txt","r") as f:
#     for line in f.readlines():   #read file line by line and gives you a list of lines
#         print(line)
#         print("-----------")
with open("./data/first.txt",'a') as f :
    for i in range(0,4):
        name = input("Enter name ")
        f.write(f"welcome {name} \n")
print("All names are added to the file ")

