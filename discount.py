#Discount:

def check_discount_eligibility(age,is_member):
    if age<18 or is_member:
        return "Eligibility for discount"
    
    else:
        return "not eligible for discount"
    
age = int(input("Enter your age: "))
is_member =input(("Membership status:"))
