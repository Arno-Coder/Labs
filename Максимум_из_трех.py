first = input()
second = input()
third = input()

if int(first) > int(second):
    if int(first) > int(third):
        print(first)
    else:
        print(third)

elif int(first) < int(second):
    if int(second) > int(third):
        print(second)
    else:
        print(third)

else:
    print(third)
