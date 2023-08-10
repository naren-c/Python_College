student_marks = []
n = 0
count = 0
print("Enter the marks of each student for a given subject(to stop enter a negative number) ")

#input value of marks
while (n>=0):
    n = int(input())
    if n>=0:
        student_marks.append(n)    
print(student_marks)

print("The highest marks scored in the subject is",max(student_marks))

#counting number of maximum marks by comparing and incrementing value of count
max_marks = max(student_marks)
for n in student_marks:
    if n == max_marks:
        count+=1
print("The number of students who have scored highest marks",count)

#counting second highest marks
new_list =[] #creating a new list
for n in student_marks:
    if n != max_marks:
        new_list.append(n) #new list without highest marks
max_marks2 = max(new_list)
print("The second highest marks is",max_marks2 )

fail_marks = int(input("The fail marks is ")) #input failed marks

pass_list = [] #creating new list for pass students
for n in student_marks:
    if n>fail_marks:
        pass_list.append(n)
print("The marks of students who have passed are",pass_list)
