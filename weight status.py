#calculating weight and height:
# Using combined return values:
#BMI= Body Mass Index:

"""def calculate_bmi(weight, height):
    bmi=weight/(height**2)

    if bmi<18.5:
        category="Underweight"
    elif 18.5<=bmi<24.9:
        category="Normal weight"
    elif 25<=bmi<29.9:
        category="Over weight"
    else:
        category="obese"

    return bmi,category
weight= float(input("Enter your weight:")) #in kilograms
height= float(input("Enter your height:")) #in meters

bmi,category=calculate_bmi(weight,height)

print(F"BMI:{bmi:.2f},category:{category}")
"""

#Using separate return values:
def calculate_bmi(weight,height):
    return weight/(height**2)

def determine_category(bmi):
    if bmi<18.5:
        return "Underweight"
    elif 18.5<=bmi<24.9:
        return "Normal weight"
    elif 25<=bmi<29.9:
        return "Over weight"
    else:
        return "obese"

weight=float(input("Enter the weight:"))
height=float(input("Enter the height:"))
bmi=calculate_bmi(weight,height) #calculate the bmi
category= determine_category(bmi) #deterniment bmi category

print(f"BMI: {bmi:.2f}")
print(f"category: {category}")
