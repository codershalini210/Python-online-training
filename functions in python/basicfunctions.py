# function with no parameter no return
# def greet():
#     print("Welcome to functions")
# greet()
# greet()

# function with parameter and return
# def square(number):
#     return number*number
# n = int(input("Enter no "))
# s = square(n)
# print(f"square of {n} is {s}")

# function with list as parameter
def total(numbers):
    t = 0 
    for n in numbers:
        t=t+n
    return t
nos = [12,43,12,44]
list_total = total(nos)
print(f"sum of {nos} is {list_total}")