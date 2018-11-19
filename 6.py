# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0

balance = float(input("balance - the outstanding balance on the credit card: "))
AnnualInterestRate = float(input("annualInterestRate - annual interest rate as a decimal: "))

r = AnnualInterestRate / 12.0

payment = 0
begBalance = balance
lowerBound = balance / 12
upperBound = (balance * (1 + r)**12) / 12.0
e = 0.03

while abs(balance) > e:
    payment = (lowerBound + upperBound) / 2
    balance = begBalance
    for i in range(12):
        ub = balance - payment
        interest = r * ub
        balance = ub + interest
    if balance > e:
        lowerBound = payment
    elif balance < -e:
        upperBound = payment
    else:
        break
print("Lowest Payment: {}".format(round(payment, 2)))


# 5000
# 0.18


