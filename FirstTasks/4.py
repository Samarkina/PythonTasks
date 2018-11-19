print("Введите, сколько рекоммендовано спать")
a = int(input())  # rec
print("Введите, сколько НЕ рекоммендовано спать")
b = int(input()) # dont
print("Введите, сколько спит сейчас")
h = int(input()) # now

if h <= b and h >= a:
    print("Это нормально")
elif h < a:
    print("Недосып")
elif h > b:
    print("Пересып")
