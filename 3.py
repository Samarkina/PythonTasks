s = input()
longest = s[0]
current = s[0]
for elem in s[1:]:
    if elem >= current[-1]:
        current += elem
        if len(current) > len(longest):
            longest = current
    else:
        current = elem
print("Longest substring in alphabetical order is: {}".format(longest))
