x = int(input())
h = int(input())
m = int(input())
go_to_sleep = h*60 + m
timer = x + go_to_sleep
print("{} часов".format(timer//60))
print("{} минут".format(timer%60))
