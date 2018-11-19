str = input().split(' ')
if len(str) == 1:
    print(str[0])
else:
    for i in range(len(str)):
        if i == 0:
            prev = int(str[-1])
        else:
            prev = int(str[i - 1])
        if i == (len(str) - 1):
            next = int(str[0])
        else:
            next = int(str[i + 1])
        print(prev + next, end=' ')


