#Real world concept:1
while True:
    print("\n Company name")
    print("\n XYZ Solutions")
    print("\n Performance Appraisal")
    print("Please Enter Employee Name:\n")
    employee1= "Rasul khan"
    employee2= "vijay"
    employee3= "Renesh"
    employees= input()
    print("Please Enter Employee's Achieved:\n")
    employee_achived= int(input())

    if employees == "Rasul khan" and employee_achived > 50000:
        print("Well Done Mr. Rasul khan - You got Increment amount Rs. 10000")

    elif employees == "Vijay" and employee_achived > 40000:
        print("Well Done Vicky - You got Increment amount Rs. 8000")

    elif employees == "Renesh" and employee_achived > 30000:
        print("Well Done Mr. Maddy - You got Increment amount Rs. 6000")
        
    else:
        print("Better Luck Next Time ")
        break
