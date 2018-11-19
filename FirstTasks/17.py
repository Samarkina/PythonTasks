a = int(input())
b = int(input())

sum = 0
amount = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        amount += 1
        sum += i

print(sum/amount)

