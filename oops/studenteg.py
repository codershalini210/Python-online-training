# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def report(self):
#         print(f"{self.name} : {self.score}")
#     def is_promoted(self):
#         return self.score>=80
# students = [
#     Student('A',36),
#     Student('b',85),
#     Student('C',74)
# ]
# for s in students:
#     s.report()
#     if s.is_promoted():
#         print("Promoted ")
# create a class with the cars 
# that should have attr like carname ,company, iselectric
# create a method to show details like carname and company

class Car:
    def __init__(self,carname,company,iselectric):
        self.carname = carname
        self.company = company
        self.iselectric = iselectric
    def showdetails(self):
        if(self.iselectric):
            print(f"{self.carname}--{self.company}--  Electric car")
        else:
            print(f"{self.carname}--{self.company}--  non Electric car")
cars = [
    Car('car1','comp1',True),
    Car('car2','comp2',False),
    Car('car3','comp1',True),
    Car('car4','comp2',False)
]

for c in cars:
    c.showdetails()