import math

a = input()
b = input()
c = input()

D = float(b)*float(b) - 4 * float(a) * float(c)

if float(D) == 0:
    x = (0 - float(b))/(2*float(a))
    print(x)

if float(D) > 0:
    if float(a) != 0:
        koren_1 = (float(b)*(-1) + math.sqrt(float(D)))/(2*float(a))
        koren_2 = (float(b)*(-1) - math.sqrt(float(D)))/(2*float(a))
        print(koren_1, koren_2)
