# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

balance = float(input("balance - the outstanding balance on the credit card: "))
AnnualInterestRate = float(input("annualInterestRate - annual interest rate as a decimal: "))
monthlyPaymentRate = float(input("monthlyPaymentRate - minimum monthly payment rate as a decimal: "))

r = AnnualInterestRate / 12.0

for i in range(12):
    p = monthlyPaymentRate * balance
    ub = balance - p
    interest = r * ub
    balance = ub + interest

print("Remaining balance: {}".format(round(balance, 2)))


# 5000
# 0.18
# 0.02