import math
print("Введите a")
a = int(input())
print("Введите b")
b = int(input())
print("Введите c")
c = int(input())
p = (a + b + c) / 2
print(math.sqrt(p * (p - a) * (p - b) * (p - c)))