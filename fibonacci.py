lim = int(input("Enter the maximum range: "))
n1 = 0
n2 = 1
print(n1, n2, end=" ")
s = n1 + n2
for i in range(1, lim + 1):
    n2 = n1
    n1 = s
    s = n1 + n2
    print(s, end=" ")
