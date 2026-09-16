# class Student:
#     def __init__(self,name,score):
#         # print("constructor called")    
#         self.name = name 
#         self.score = score
#     def hellostudent(self):
#         print("hello ", self.name ," you got ", self.score," Marks")
# s1 = Student('ben',88)
# s2 = Student('Sam',45) 
# s1.hellostudent()
# s2.hellostudent()
# s3 = Student('Ron',96)
# s3.hellostudent()
#exercise
# Create a Python class called Employee that stores an employee's name and salary.

# Create a constructor __init__() to initialize name and salary.
# Create a method called showdetails() that prints:
# Employee name
# Employee salary
# Create three employee objects with the following details:
# Jack, 35000
# Emily, 42000
# Oliver, 28000
# Call showdetails() for each employee.
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def showdetails(self):
#         print("name : ",self.name ," Salary : ",self.salary)
# e1 = Employee("Jack",35000)
# e2 = Employee("Emily", 42000)
# e3 = Employee("Oliver",28000)
# e1.showdetails()
# e2.showdetails()
# e3.showdetails()

# Create a Python class called BankAccount to represent a simple bank account. The class should
#  store the account holder's name and account balance. It should contain two methods:

# deposit() – adds the given amount to the account balance.
# withdraw() – subtracts the given amount from the account balance if sufficient funds are available. Otherwise, display a message indicating that the balance is insufficient.

# Create an object of the class and demonstrate depositing and withdrawing money from the account.
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self,amt):
#         self.balance = self.balance +amt
#         print(f"Amount Deposited Successfully in account of {self.name} new balance: ",self.balance)
#     def withdraw(self,amt):   
#         if(amt<=self.balance):
#             self.balance = self.balance-amt
#             print(f"Amount Withdraw Successfully from {self.name} new balance: ",self.balance)
#         else:
#             print("Insufficent amount in acc")
# acc1 = BankAccount('a',50000)
# acc2=BankAccount('b',65200)
# acc1.deposit(1000)
# acc2.deposit(450)
# acc1.withdraw(65201)
# acc2.withdraw(4521)
# create a book class , that take bookname,ISBN, AUTHOR name in constructor,
# and a method show bookdetails which display this information

class Book:
    def __init__(self,bookname,ISBN,author):
        self.bookname = bookname
        self.isbn = ISBN
        self.author = author
    def bookdetails(self):
        print("title: ", self.bookname, " Author :",self.author, "ISBN : ",self.isbn)
books=[]
choice = 'y'
while(choice=='y'):
    bookname = input("Enter bookname")
    author = input("Enter author")
    isbn = input("Enter isbn")
    books.append(Book(bookname,isbn,author))
    choice = input("do you want to continue y/n")

for b in books:
    b.bookdetails()
# books = [ Book('book1','author1',4552125),
#          Book('book2','author2',112225),
#           Book('book3','author3',2232125),
#            Book('book4','author4',3452125) ]
# for b  in books:
#     b.bookdetails()