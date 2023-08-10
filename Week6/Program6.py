#set Stu_marks
Stu_marks={'PECS001': {'phy': 79, 'chem': 90, 'mat': 84, 'Bio': 87},
           'PECS015': {'phy': 59, 'chem': 76, 'mat': 74, 'Bio': 66},
           'PECS065': {'phy': 89, 'chem': 58, 'mat': 94, 'Bio': 81},
           'PECS035': {'phy': 71, 'chem': 91, 'mat': 81, 'Bio': 86},
           'PECS038': {'phy': 75, 'chem': 98, 'mat': 75, 'Bio': 84}}

print("detailed marks \n",Stu_marks,"\n")
Score_card = {} #create a dictionary

#compute total and percentage for each student and add to Score_card
for srn,marks in Stu_marks.items():
        d = dict()
        d['total'] = sum(marks.values())
        d['percent'] = d['total']/4
        Score_card[srn] = d
      
print(Score_card)

