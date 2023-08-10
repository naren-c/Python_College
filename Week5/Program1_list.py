food=['pani puri','dosa','bhel puri',
     'masala dosa','dahi puri','rava dosa','pizza topings','pizza mania']

#creating new lists to store pizza, puri, dosa food types
l_pizza = []
l_puri = []
l_dosa = []

for i in food:
    if i.startswith("pizza"):
        l_pizza.append(i)
    elif i.endswith("puri"):
        l_puri.append(i)
    elif i.endswith("dosa"):
        l_dosa.append(i)
        
print("List which starts with pizza is",l_pizza)
print("List which ends with puri is",l_puri)
print("List which ends with dosa is",l_dosa)
