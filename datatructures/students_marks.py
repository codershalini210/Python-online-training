students = {
    "Oliver": 78,
    "Amelia": 85,
    "George": 72,
    "Isla": 91,
    "Harry": 83,
    "Emily": 88,
    "Arthur": 67,
    "Sophie": 95
}
# Display all student names.
print(list(students.keys()))   
print("-----------------")
# Display all marks.
print(list(students.values()))
# Display each student's name along with their marks.
for s,m in students.items():
    print("Name ",s," marks :", m)
# Calculate the total marks.
totalMarks = 0
s = sum(list(students.values()))
print("s is ",s)

for v in students.values():
    totalMarks= totalMarks+ v
print("Total marks", totalMarks)
# Calculate the average marks.
avgmarks = totalMarks/len(students)
print("avg marks ",avgmarks)
# Count the number of students who scored 80 or more.
count80=0
for v in students.values():
    if(v>=80):
        count80= count80+1
print("no of students who scored 80 or more ", count80)
# Add a new student with their marks.
students["ABC"] = 45
# Update the marks of an existing student.
students["Harry"]=92
# Remove one student from the dictionary.
del students["Amelia"]
# Check whether a given student exists in the dictionary.
print("Amelia" in students)
print(students)