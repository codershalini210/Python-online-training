# range -> commonly used with a for loop , when you want repeat some thing
# certain no of times
# range(5)-> 0,1,2,3,4  start from 0 and ends before 5
# range(2,7)->starts from 2 and ends before 7
# for i in range(5):
#     print(i)
# -----------------------
# for i in range(1,6):
#     print(i)
# -------------------------------
# write a program to print nos from 10-20
# for i in range(10,21):
#     print(i)
# --------------------
# range(1,10,2)  ->start with 1 , ends before 10 , 
# increase value by 2 in every step
# for i in range(1,10,2):
#     print(i)
# for i in range(10,0,-1):
#     print(i)
#  print all the multiples of 5 from 5 to 50 // 5,10,15....50
# for i in range(5,51,5):
#     print(i,end=" ")
#print all the even no between 40-50 using range with step 2
for i in range(40,51,2):
    print(i,end=" ")