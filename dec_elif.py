lim = int(input("Enter a decimal number: "))
opt = input("Enter the operation ( bin, oct, hex ): ")
d = lim
s = 0
b = 1
if opt == 'bin':
    while d > 0:
        x = d % 2
        s = s + (x * b)
        d = d // 2
        b = b * 10
    print("The binary of the number " + str(lim) + " is = ", s)
elif opt == 'oct':
    while d > 0:
        x = d % 8
        s = s + (x * b)
        d = d // 8
        b = b * 10
    print("The octal of the number " + str(lim) + " is = ", s)
elif opt == 'hex':
    while d > 0:
        x = d % 16
        s = s + (x * b)
        d = d // 16
        b = b * 10
        if x > 9:
            g = chr(x + 55)
    print("The hexadecimal of the number " + str(lim) + " is = ", str(s), str(g))
else:
    print("You have chosen wrong operation")