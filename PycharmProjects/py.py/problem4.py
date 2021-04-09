i = 100
a = 100
b = a*i
while (100<=i<1000):
    while (100<=a<1000):
        print(a*i)
        a = a+1
        if (b[0:len(b)] == b[len(b):0] ):
            print(b)
        if a < 1000:
            a = 100
            break
    print(a*i)
    i = i+1
    if (b[0:len(b)] == b[len(b):0]):
        print(b)
    if i<1000:
        break