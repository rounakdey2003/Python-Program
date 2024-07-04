low = int(input("Enter lower limit: "))
up = int(input("Enter upper limit: "))
print("\tArmstrong numbers are: ")
for i in range(low, up):
    s = 0
    n = i
    while n > 0:
        d = n % 10
        s = s + (d ** 3)
        n = n // 10
    if s == i:
        print(s, end=", ")
print("\b\b", end="")
