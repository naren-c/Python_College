s='Respected sir,\n I am here by enlisting all the programming languages we teach\n Problem solving using python\n object oriented programming with C++\n java and jee \nR programming \nThanking You \nTeam Programming Languages '

t = s.split("\n") #converting into list, each element split at \n
str = ""
#capitalizes first letter of each line
for i in range(len(t)):
    if(i != 0 and i != len(t)-1 and i != len(t)-2):
        x = t[i].lstrip()
        str = str + "   " + x.capitalize() + '\n'
    else:
        str = str + t[i].capitalize() + '\n'
print(str)



mac_list = ['00','11','23','45','67','70']
print(':'.join(mac_list)) #function to join the list



friend = [' ram',' sita',' raj',' joy',' joe']
greetings = [] #creating a new list
for i in friend:
    greetings.append('Happy festival' + i) #adding new elements to the new list
print(greetings)



srn = "PE01 PE02 PE03 PE04 PE05 PE06 PE07 PE08 PE09 PE10"
print("The SRN before replacing is",srn)
#replacing PE to PESU for first three elements
print("The SRN after replaing with PESU is",srn.replace("PE","PESU",3))

x = input("Input the SRN number to be found ")
n = srn.find(x) #using funtion find to find the particular snr
if n > 0:
    print("The SRN is found in location",n)
else:
    print("The SRN is not found")

