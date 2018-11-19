lst = input().split(' ')
x = int(input())
notPrinted = True
for i in range(len(lst)):
    if int(lst[i]) == x:
        print(i, end=' ')
        notPrinted = False

if notPrinted:
    print("Отсутствует")