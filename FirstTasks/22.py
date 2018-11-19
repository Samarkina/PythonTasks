str = input().split(' ')
str.sort()
prev = str[0]
printed = []
for i in range(1, len(str)):
    if str[i] == prev and str[i] not in printed:
        print(str[i], end=' ')
        printed.append(str[i])
    prev = str[i]

