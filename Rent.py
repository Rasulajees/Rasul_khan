#House rent document

print("House Rent Document")

#Barrower details:
name=input("Enter your name:")
age=input("Enter your age:")
barrower_salary =input("Enter your barrower salary:")
govt_proof=input("Enter yourgovt proof:")
no_persons=input("Enter no.persons:")

# House details:
house_number=int(42)
street=("abc street")
city=("Pondy")
state=("poducherry state")
zip_code=("605105")
count_of_month=int(input("Enter count of month:"))
Advance_amount=int(75000)
Monthly_rent=int(3000)

a=int(input("advance_amount:"))

b=int(3000)

c=int(2)
d=a-b*c
if a-b*c==d:
    print(d)
else:
    print("Payment is due")