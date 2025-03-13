#Example 1:
#----------------------SLICING CONCEPT:----------------------------------
import numpy as np

#Cinema seat numbers(1D array)
"""seats=np.array([1,2,3,4,5,6,7,8,9,10])

#selecting first 5 seats
first_half=seats[:5]
print("First half seats:",first_half)  #[1,2,3,4,5]

#selecting alternate seats (odd-numbered seats)
alternate_seats=seats[::2]
print("Alternate seats:",alternate_seats) #[1,3,5,7,9]
"""
#Example 2:
#Temperature Records:
#Temperature readings for 7 days (monday to Sunday):
"""
temperature=np.array([28,31,27,33,29,35,31])
          #Index no:([ 0, 1, 2, 3, 4, 5, 6])

#Extracting temperature for first 2 days (Monday to tuesday):
first_two_days=temperature[0:2]
print("First two days temperature:",first_two_days) #output:[28,31]

#Extracting mid-week temperatures (wednesday to friday):
mid_week_temps=temperature[2:5]
print("Mid-week temperatures:",mid_week_temps) #output:[31,27,33]

#Extracting tempertatures for week end days (Saturday, Sunday):
weekend_temps=temperature[-2:7]
print("Weekend Temperature:",weekend_temps) #output:[35,31]
"""
#Example 3:
#football playes status:
#goals secored in 10 matches:

goals=np.array([2,3,2,0,3,1,0,2,1,3])
    #Index no:([0,1,2,3,4,5,6,7,8,9])
#First 5 matches performence:
first_five_matches=goals[0:5]
print("First five matches goals:",first_five_matches) #output:[2,3,2,0,3]

#Last 5 matches performence:
last_five_matches=goals[5:11]
print("Last five matches goals:",last_five_matches) #output:[1,0,2,1,3]

#Team Status:
if np.sum(goals)>=3:
    print("The team is performing well")   
elif np.sum(goals)==1:
    print("The team needs to work hard")
elif np.sum(goals)==2:
    print("The team is doing great")
elif np.sum(goals)==0:
    print("The team is not performing well")
else:
    print("The team needs to improve")

#Example 4:
#Extracting sections of an image:
#Image resolution: 4x4 pixels