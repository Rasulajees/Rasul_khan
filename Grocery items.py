import numpy as np
grocery_list =["Apples","Bananas","Milk","Eggs","Bread"]

#Accessing elements:

print("First item:",grocery_list[0]) #Apples
print("Last item:",grocery_list[-1]) #Bread

#updating an items:
grocery_list[2]=" Cow Milk"
print("updating list:",grocery_list)

#Adding an item:
grocery_list.append("Butter")
print("List after adding an item:",grocery_list)

#Removing an item:
grocery_list.remove("Bananas")
print("List after removing an item:",grocery_list)

#Looping through the list:
print("Grocery iterms:")
for item in grocery_list:
    print("-",item)
    