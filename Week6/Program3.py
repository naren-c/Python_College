srns = ["PECS001","PECS015","PECS065","PECS035","PECS038"] #set srns
#set marks scored by each student in each subject, physics, chemistry, maths and biology
p_marks = [98,99,85,92,79]
c_marks = [91,90,84,98,99]
m_marks = [78,39,60,50,84]
b_marks = [95,59,78,80,89]

#create a new dictionary for student marks and marks
student_marks={} 
marks_det={} 

#for loop used to add marks into marks_det for each student for each subject
for i in range(0,len(srns)):
    marks_det['Physics'] = p_marks[i]
    marks_det['Chemistry'] = c_marks[i]
    marks_det['Maths'] = m_marks[i]
    marks_det['Biology'] = b_marks[i]
    student_marks[srns[i]] = marks_det

print(student_marks)
