sum = 0
sumPow = 0
p = True
while (sum != 0 or p):
    p = False
    elem = int(input())
    sum += elem
    # print(sum)
    sumPow += elem * elem

print(sumPow)

'''
1
-3
5
-6
-10
13
4
-8
'''