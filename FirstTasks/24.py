n = int(input())

mass = n
i = 1
while (mass > 0):
    j = 0
    while ((mass > 0) and j < i):
        print(i, end=' ')
        mass -= 1
        j += 1
    i += 1
