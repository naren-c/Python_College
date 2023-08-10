"""
If a person leaves his house at 6:52 am and runs 1 mile at an easy pace
(8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at
easy pace again, what time do the person get home for breakfast?
"""
#defining the time the person left home
start_timehour = 6
start_timeminute = 52

#converting hours and minutes into seconds
easy_pace = 8*60+15
tempo_pace = 7*60+12

#total running time in seconds
time_inseconds = easy_pace*2 + tempo_pace*3

#total running time in minutes
minutes = time_inseconds//60

#remaining time in seconds
seconds = time_inseconds%60

end_minutes = start_timeminute + minutes #calculating total minutes
end_timehour = start_timehour + end_minutes//60 
end_minutes = end_minutes%60

str1="The person will be home at "+str(end_timehour)+':'+str(end_minutes)+':'+str(seconds)+' AM'
print(str1)
