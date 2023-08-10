import random

#setting limit of Bradycardia, Trachycardia and counter as 0
brady_cardia = 0 
tachy_cardia = 0
c = 0

heart_rate=[] #creating empty list

#getting 8 random values of heart rate between 50 and 120
while(c<8):
    i = random.randint(50,120)
    heart_rate.append(i)
    c=c+1
print("The heart rate at intervals of 3 hours for 24 hours is",heart_rate)

for i in heart_rate:
    if i>50 and i<65:
        brady_cardia+=1 #incrementing count of Bradycardia
        print("Heart rate",i,"is Bradycardia")
    elif i>100:
        tachy_cardia+=1 #incrementing count of Trachycardia
        print("Heart rate",i,"is Tachycardia")
    else:
        print("Heart rate",i,"is Normal")

if (brady_cardia or tachy_cardia)>3:
    print("Risk because count of Bradycardia or Tachycardia is greater than 3")

#printing maximum and minimum heart rate
print("The maximum heart rate is",max(heart_rate))
print("The minimum heart rate is",min(heart_rate))

