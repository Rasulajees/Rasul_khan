# Loan Eligibility:

"""def calculate_debt_to_income_ratio(income,Loan_amount):
    return income/Loan_amount

def check_credit_score(credit_score):
    min_credit_score = 650

    return credit_score >= min_credit_score

def eveluate_loan_eligibility(income,loan_amount,credit_score):
    debt_to_income_threshold= 0.40  #deft-to-income ratio threshold

#calcularte debt-to-income ratio
    dti_ratio = calculate_debt_to_income_ratio(income,loan_amount)

#check if the dobt-to-income is below thr thresholds and credit score is sufficient
 
    if dti_ratio < debt_to_income_threshold and check_credit_score(credit_score):
        return "Eligible"
    else:
        return "Not Eligible"
income = float(input("Enter your income amount:"))  # monthly in income amount

loan_amount = float(input("Enter your loan amount:")) # monthly loan payment in Rupees

credit_score = float(input("Enter your credit score:")) # credit score

eligibility_score = eveluate_loan_eligibility(income, loan_amount, credit_score)

print(f"Loan Eligibillity status: {eligibility_score}")

"""

def evaluate_loan_eligibility(income, loan_amount, credit_score):
    dti_threshold=0.40
    min_credit_score=650
    dti_ratio=loan_amount/income
    
    if dti_ratio < dti_threshold and credit_score and min_credit_score:
        return"Eligible"
    else:
        return "Not Eligible"

income=float(input("Enter your salary:"))
loan_amount=float(input("Enter your loan amount:"))
credit_score=float(input("Enter your credit score:"))

print(evaluate_loan_eligibility(income,loan_amount,credit_score))