print("Введите кол-во программистов:")
number = int(input())
n = number % 10
nu = number % 100
if 11 <= nu <= 14 or n == 0 or n >= 5:
    print("{} программистов".format(number))
elif n == 2 or n == 3 or n == 4:
    print("{} программиста".format(number))
elif n == 1:
    print("{} программист".format(number))





