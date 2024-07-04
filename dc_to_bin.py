lim = int(input("Enter a decimal number: "))
d = lim
s = 0
b = 1
while d > 0:
    x = d % 2
    s = s + (x * b)
    d = d // 2
    b = b * 10
print("The binary of the number " + str(lim) + " is = ", s)

