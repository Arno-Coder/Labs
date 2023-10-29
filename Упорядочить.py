a = input()
b = input()
c = input()

if int(a) >= int(b) and int(a) >= int(c):
    if int(b) >= int(c):
        print(int(c), int(b), int(a))
    else:
        print(int(b), int(c), int(a))

elif int(a) <= int(b) and int(a) <= int(c):
    if int(b) >= int(c):
        print(int(a), int(c), int(b))
    else:
        print(int(a), int(b), int(c))

else:
    print(int(b), int(a), int(c))