file1 = open('mov1.csv','r') #open file in read mode
d = dict()

#read one line at a time, extract the year of release and movie name and
#write these values to the dictionary
line = file1.readline() 
while line:
    line = line.strip()  
    list1 = line.split(',')  

    if list1[0] not in d: #condition to check repitition
        d[list1[0]]=[]     
    d[list1[0]].insert(0,list1[-1]) #adding values to the dictionary

    line = file1.readline()

print(d)
file1.close()

