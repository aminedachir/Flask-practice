c = 0 ; d =0
for a in range(1000):
    if a%3 == 0:
        d = d + a
    elif a%5 == 0:
        c = c + a
print (c+d)
