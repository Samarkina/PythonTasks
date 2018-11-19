import math
def main():
    print("Тип фигуры")
    figure = input()
    a = int(input())
    if figure == "прямоугольник" or figure == "треугольник":
        b = int(input())
        if figure == "треугольник":
            c = int(input())
            p = (a + b + c) / 2
            return math.sqrt(p * (p - a) * (p - b) * (p - c))
        else:
            return a * b
    return 3.14 * a * a

print(main())