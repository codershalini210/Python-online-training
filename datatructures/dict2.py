students ={"a":52,"b":21,"c":14,"d":85,"e":45}
# print names of students whose marks are greater than 50
for name,marks in students.items():
    if(marks>=50):
        print(name)