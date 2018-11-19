s = input()
vowels = ['a', 'e', 'i', 'o', 'u']
count = len([each for each in s if each in vowels])
print("Number of vowels: {}".format(count))