def main():
    print("Введите число")
    number = int(input())
    sum = 0
    while(number <= 100):
        if number >= 10:
            print(number)
        print("Введите число")
        number = int(input())

main()