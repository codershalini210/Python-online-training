# x=10 #global 
def hello():
    x=10  #local
    print("x from hello ", x)

hello()
print("x outside any fuction ",x) #no error in global case
# above line give an err : name 'x' is not defined when x is local 