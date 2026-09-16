nums = [1,2,3,4,5]
# square = []
# for n in nums:
#     square.append(n*n)
square = [n*n for n in nums]
evennos = [n for n in nums if n%2 == 0 ]   # % is a mod operator that give you remainder 
print("Square list ", square)
print("Even no ",evennos)
# you need to create a list for cubes of numbers 
# and 
cubes = [n*n*n for n in nums]
oddnos = [n for n in nums if n%2!=0]
# list of odd nos from the given list
print("cubes ",cubes)
print("odd nos ", oddnos)