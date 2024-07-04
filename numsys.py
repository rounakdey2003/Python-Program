lim = int(input("Decimal -> "))
opt = input("Operation -> ")

def bin():

    d = lim
    s = 0
    b = 1
        
    while d > 0:
        x = d % 2
        s = s + (x * b)
        d = d // 2
        b = b * 10
    print("Binary " + "'" + str(lim) + "'" + " = ", s)

def oct():

    d = lim
    s = 0
    b = 1

    while d > 0:
        x = d % 8
        s = s + (x * b)
        d = d // 8
        b = b * 10
    print("Octal " + "'" + str(lim) + "'" + " = ", s)

def hex():

    d = lim
    s = 0
    b = 1

    while d > 0:
        x = d % 16
        s = s + (x * b)
        d = d // 16
        b = b * 10
        if x > 9:
            g = chr(x + 55)
    print("Hexadecimal " + "'" + str(lim) + "'" + " = ", str(s), str(g))

if opt == 'b':
    bin()
elif opt == 'o':
    oct()
elif opt == 'h':
    hex()
else:
    print("Wrong operation !!")