str = input()

prevChar = str[0]
amount = 0
for i in range(1, len(str)):
    amount += 1
    if str[i] != prevChar:
        print("{}{}".format(prevChar, amount), end='')
        amount = 0
    prevChar = str[i]

amount += 1
print("{}{}".format(prevChar, amount), end='')
