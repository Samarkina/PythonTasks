print("Введите первое число")
first = float(input())
print("Введите второе число")
second = float(input())
print("Введите операцию")
operation = input()

if second == 0 and (operation == "/" or operation == "mod" or operation == "div"):
    print("Деление на 0!")
elif operation == "+":
    print(first + second)
elif operation == "+":
    print(first + second)
elif operation == "-":
    print(first - second)
elif operation == "*":
    print(first * second)
elif operation == "/":
    print(first / second)
elif operation == "mod":
    print(first % second)
elif operation == "pow":
    print(first ** second)
elif operation == "div":
    print(first // second)
else:
    print("Something wrong")
