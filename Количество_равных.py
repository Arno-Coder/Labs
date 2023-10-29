a = input()
b = input()
c = input()

if int(a) == int(b) and int(b) == int(c) and int(a) == int(c):
    print(3)
elif int(a) == int(b) or int(b) == int(c) or int(a) == int(c):
    print(2)
else:
    print(0)

