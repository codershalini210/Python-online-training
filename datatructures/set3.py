# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# print(set1 & set2)   #intersection
# print(set1 | set2) #union

#set n that contain all students
all_students={'a','b','c','d','e','f'}
#students passed in all subjects in set 1
pass_students={'a','b','c'}
# set of students passed in 1 subject
one_subjects = {'f'} 
print(all_students -pass_students)
# print name of students that failed in all the subjects
print(all_students -pass_students-one_subjects)
