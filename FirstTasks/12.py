number = input()
dec = pow(10, len(number) - 1)

sumLeft = 0
sumRight = 0
for i in range(len(number)):
    elem = int(int(number) // dec % 10)
    if i < len(number) // 2:
        sumLeft += elem
    else:
        sumRight += elem
    dec /= 10

if sumLeft == sumRight:
    print("Счастливый")
else:
    print("Обычный")