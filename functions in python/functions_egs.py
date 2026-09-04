# def factorial(n):
#     f = 1
#     for i in range(n,0,-1):
#         f=f*i
#     return f
# n1 = int(input("Enter no "))
# f = factorial(n1)
# print(F"factorial of {n1} is {f}")

def table_of_n(n):
    for i in range(1,11):
        print(n*i,end=" ")
v = input("Enter any no ")
if(v!=""):
    number = float(v)
    table_of_n(number)
else:
    print("invalid input")


