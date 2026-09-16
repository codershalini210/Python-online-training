salaries =[25000,65200,45201,35210,456321]
marks =[45,78,98,52,63,47,25,84]
ages=[]
def findavg(data):
    if(len(data)==0):
        return " no data in list"
    else:
        total = sum(data)
        avg = total/len(data)
        return f"avg is {avg}"
print("Avg of salaries ", findavg(salaries))
print("avg of marks",findavg(marks))
print("avg of age ",findavg(ages))