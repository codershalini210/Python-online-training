class Course:
    def __init__(self,title,capacity,enrolled):
        self.title  = title 
        self.capacity = capacity
        self.enrolled = enrolled
    def remaining_places(self):
        return self.capacity - self.enrolled
    def summary(self):
        return f"title: {self.title} , enrolled:{self.enrolled} ,capacity: {self.capacity}"
c1 = Course('course1',120,60)
c2 = Course('course2',150,120)
c3 = Course('course3',100,100)
msg = c1.summary()
print(msg , "remaning Places ",c1.remaining_places())
msg = c2.summary()
print(msg,"remaning Places ",c2.remaining_places())
msg = c3.summary()
print(msg,"remaning Places ",c3.remaining_places())
