a = int(input())
b = int(input())
c = int(input())
d = int(input())
dict = {}
top = []
left = []
for i in range(b - a + 1):
    left.append(a + i)
    dict[a + i] = {}
    for j in range(d - c + 1):
        if i == 0:
            top.append(c + j)
        dict[a + i][c + j] = (a + i) * (c + j)

print(end='\t')
for i in top:
    print(i, end='\t')
print(end='\n')

k = 0
for i in range(b - a + 1):
    print(left[k], end='\t')
    k += 1
    for j in range(d - c + 1):
        print(dict[a + i][c + j], end='\t')
    print(end='\n')
