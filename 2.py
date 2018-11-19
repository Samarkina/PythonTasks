def count(str, substr):
    return 0 if len(str) < len(substr) else str.startswith(substr) + count(str[1:], substr)

s = input()
print("Number of times bob occurs is: {}".format(count(s, "bob")))