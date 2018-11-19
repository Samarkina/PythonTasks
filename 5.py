# Monthly interest rate= (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

balance = float(input("balance - the outstanding balance on the credit card: "))
AnnualInterestRate = float(input("annualInterestRate - annual interest rate as a decimal: "))

r = AnnualInterestRate / 12.0
payment = 0
begBalance = balance

while balance > 0:
    for i in range(12):
        ub = balance - payment
        interest = r * ub
        balance = ub + interest
    if balance > 0:
        payment += 10
        balance = begBalance
    elif balance <= 0:
        break
print("Lowest Payment: {}".format(round(payment, 2)))


# 5000
# 0.18


