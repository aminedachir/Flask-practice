nombre = 600851475143
j = nombre
i = 2
while i <= j :
    if ( j % i == 0):
        j = int(j/i)
    else:
        i = i + 1
print("Le plus grand facteur premier de ", nombre, " est ", i)


a = '9008'
i=3
while (i>=0):
    print(a[2:3:4])
    i = i-1