# print hello 5 no of times
# for i in range(0,5):
#     print("hello ",end="--")

# take marks of student in 3 subject and show total 
# total = 0
# for i in range(0,3):
#     marks = int(input(f"Enter marks of subject  {i+1}  : "))
#     total = total+marks
# print(f"total marks {total}")
# print(f"avg marks  {total/3}")


# present_students = ["a","b","c","f"]
# for st in present_students:
#     print(st, " Present")

# print multiplication table of 7 
# for i in range(7,71,7):
#     print(i,end=" ")
# print factorial of 5 
f = 1
for i in range(5,0,-1):   #5.4,3,2,1
    f=f*i            
    if(i!=1):
        print(f"{i} * ",end="")
    else:
        print(f"{i}",end="")
print(" = ",f)

# name="John"
# for ch in name:
#     print(ch)