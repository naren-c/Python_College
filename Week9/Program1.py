"""
Write a program to sort a given list of dictionary in ascending
order of Matches played by the players
"""

ipl = [{'RCB': 'Kohli', 'Matches': 116, 'Runs': 1000}, {'CSK': 'MSD', 'Matches': 120, 'Runs': 994},
     {'MI': 'Rahul', 'Matches': 100, 'Runs': 1150}]

b = sorted(ipl,key=lambda x:x['Matches'])
print(b)



