str = input().lower()
amount = 0
for char in str:
    if char == 'c' or char == 'g':
        amount += 1
print(amount / len(str) * 100)
