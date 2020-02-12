import random
 
##enter students names
students = []
studentsCopy = []
print (students)
 
##print out number of studnets
print (len(students))
 
number_of_groups = 8
 
students_per_group = 3
 
group1 = []
group2 = []
group3 = []
group4 = []
group5 = []
group6 = []
group7 = []
group8 = []
 
 
step = 1

##break down students into groups of 3
for step in studentsCopy:
    ##print (step)
    addStudent = random.choice(students)
    if len(group1) < 3:
        group1.append(addStudent)
        students.remove(addStudent)
    elif len(group2) < 3:
            group2.append(addStudent)
            students.remove(addStudent)
    elif len(group3) < 3:
            group3.append(addStudent)
            students.remove(addStudent)
    elif len(group4) < 3:
            group4.append(addStudent)
            students.remove(addStudent)
    elif len(group5) < 3:
            group5.append(addStudent)
            students.remove(addStudent)
    elif len(group6) < 3:
            group6.append(addStudent)
            students.remove(addStudent)
    elif len(group7) < 3:
            group7.append(addStudent)
            students.remove(addStudent)
    else:
        if len(group8) < 3:
            group8.append(addStudent)
            students.remove(addStudent)
       
##print out the groups  
print (group1)
print (group2)
print (group3)
print (group4)
print (group5)
print (group6)
print (group7)
print (group8)
 
##print out the student list again
print (students)