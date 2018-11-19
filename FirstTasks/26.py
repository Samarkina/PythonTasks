str = input()
numbers = []
while str != "end":
    numbers.append(str.split(' '))
    str = input()
    
if len(numbers) == 1:
    print(int(numbers[0][0]) * 4)
else:
    sum = []
    for i in range(len(numbers)):
        sum.append([])
        for j in range(len(numbers[0])):
            if i == len(numbers) - 1:
                i2 = -1
            else:
                i2 = i
            if j == len(numbers[0]) - 1:
                j2 = -1
            else:
                j2 = j
            sum[i].append(int(numbers[i2 - 1][j]) + int(numbers[i2 + 1][j]) + int(numbers[i][j2 - 1]) + int(numbers[i][j2 + 1]))

    for str in sum:
        for elem in str:
            print(elem, end=' ')
        print()