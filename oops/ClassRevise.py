class Course:
    def __init__(self,title,duration,status):
        self.title = title
        self.duration = duration 
        self.status = status
    def summary(self):
        return f"{self.title} , duration : {self.duration} , status:{self.duration}"
c1 = Course("Data Science", "30","Running")
c2 = Course("Machine Learning", "45","Planned")
print(c1.summary())
print(c2.summary())