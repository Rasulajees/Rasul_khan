#A
import numpy as np
"""nums=np.array([5,15,20,0,8])
print(np.any(nums>10)) #True(At least one is greater than 10)
print(np.all(nums>10)) #False(Not all are greater than 10)

#Find indice where numbers are greater than 10
indices = np.where(nums>10)
print(indices) 
"""
#B) Finding the number of hot days(above 30 C)in a week
temperature=np.array([28,31,27,33,29,35,31,39])
#condition: Days with temperature above 30 C
hot_days=np.sum(temperature<30)
# Counting hot days
num_hot_days=np.sum(hot_days)
print("Number of hot days:",num_hot_days) #output:4
