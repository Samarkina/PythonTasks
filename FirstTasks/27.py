n = int(input())

matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)

dir = ["right", "down", "left", "top"]
k = 0
i = 0
j = 0
direction = dir[k]
elem = 1
niDown = n
njRight = n
niTop = 0
njLeft = -1

def changeDirection(k):
    k += 1
    if k > 3:
        k = 0
    return dir[k], k

while elem <= n * n:
    matrix[i][j] = elem
    elem += 1
    if direction == "right":
        j += 1
        if j == njRight: #border
            j -= 1
            i += 1
            njRight -= 1
            direction, k = changeDirection(k)
    elif direction == "down":
        i += 1
        if i == niDown: #border
            i -= 1
            j -= 1
            niDown -= 1
            direction, k = changeDirection(k)
    elif direction == "left":
        j -= 1
        if j == njLeft: #border
            j += 1
            i -= 1
            njLeft += 1
            direction, k = changeDirection(k)
    elif direction == "top":
        i -= 1
        if i == niTop: #border
            i += 1
            j += 1
            niTop += 1
            direction, k = changeDirection(k)

#print
for str in matrix:
    for elem in str:
        print(elem, end='\t')
    print()