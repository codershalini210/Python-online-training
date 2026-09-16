class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def speak(self):
        print(" From user class : I am ",self.name)
    def role(self):
        print("From user User: General user")

class Learner(User):
    def __init__(self,name,email,course):
        super().__init__(name,email)
        self.course = course

    def role(self):    #override
        print("from learner class : LEarner ",self.name)
    def progress(self):
        print("From learner class : ",self.name ," is making good progress in ", self.course )

user1 = User('ron','ron@gmail.com')
# user1.role()
Learner1 = Learner('John','John@gmail.com','AI')
# Learner1.role()
# Learner1.speak()
# Learner1.progress()
def introduce(p):
    p.speak()
    p.role()

introduce(user1)
introduce(Learner1)