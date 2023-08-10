cap_list = ['Kholi','Dhoni','Rohit S',]
team_list = ['RCB', 'CSK', 'MI']
x = list(zip(cap_list,team_list)) #zip function to merge to lists
print("Team captain with their IPL teams ",x)


#zip(*list_name) to separate the student name and score as two elements in a list
score = [("Akash", 85), ("Arind", 80), ("Asha",95), ('Bhavana',90), ('Bhavik',87)]
y = list(zip(*score)) 
print("List displaying only student names is ",y[0])
