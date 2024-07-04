lim = int(input("Enter a decimal number: "))
opt = input("Enter the operation ( bin, oct, hex ): ")
d = lim
s = 0
b = 1
if opt == 'bin':
    bin()
elif opt == 'oct':
    oct()
elif opt == 'hex':
    hex()
else:
    print("You have chosen wrong operation")


def bin():
    while d > 0:
        x = d % 2
        s = s + (x * b)
        d = d // 2
        b = b * 10
    print("The binary of the number " + str(lim) + " is = ", s)


def oct():
    while d > 0:
        x = d % 8
        s = s + (x * b)
        d = d // 8
        b = b * 10
    print("The octal of the number " + str(lim) + " is = ", s)


def hex():
    while d > 0:
        x = d % 16
        s = s + (x * b)
        d = d // 16
        b = b * 10
    print("The hexadec of the number " + str(lim) + " is = ", s)
