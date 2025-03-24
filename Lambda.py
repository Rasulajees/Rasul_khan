
print("Syntax of Lambda functions:")
print("lambda argument: expression:")
print("Argument-->Input variables (can be multiple, separated by commas:")
print("Expression--> Single line of code that is executed and returned:\n")

add=lambda x,y:x+y
print(add(25,65),"\n")

#Using map function:
numbers=[1,2,3,4,5,6,7,8,9,0]
squared=list(map(lambda x:x**2,numbers))
print(squared,"\n")

#map(function,iterable)
#function --> A function(can br a built-in function, lambda function, or 
            #user-defined function)
#iterable --> A sequence (list, tuple,etc.,)
#converted string into intergers:

numbers=["1", "2", "3", "4", "5"]
converted=list(map(int, numbers))
print(converted,"\n")

list1=[1,2,3,4,5]
list2=[6,7,8,9,0]
summed=list(map(lambda x,y: x+y,list1,list2))
print(summed,"\n")

# small letters into catipal litter:
Words=["hello", "world", "rasul","python","pandas"]
upper_words=list(map(str.upper,Words))
print(upper_words,"\n")

import pandas as pd

data=pd.read_csv('AI & DATA SCIENCE/DATA SETS/netflix_users.csv')
print(data,"\n")


#Using lambda function with applymap:
def categorize_data(value):
    if value < 80.00 :
        return "Low"
    elif 80.00 <= value > 500.00:
        return "Medium"
    else:
        return "High"
    
data['Watch_status']=data['Watch_Time_Hours'].apply(categorize_data)
print(data,"\n")


def new_categorize_data(value):
    if value < 100.00 :
        return "Low viewing"
    elif 100.00 < value > 250.00:
        return "Medium viewing"
    elif 250.00 < value > 500.00:
        return "High viewing" 
    else:
        return "Very high viewing"

data['Watch_Time_Hours']=data['Watch_Time_Hours'].apply(new_categorize_data)
print(data,"\n")

#Using lambda function with apply:

data["Watch_Time_Hours"]=data["Watch_Time_Hours"].apply(lambda x: x - 10 if x > 200 else x)
print(data,"\n")