lim = int(input("Enter maximum number: "))
for i in range(1, lim + 1):
    for l in range(lim, i, -1):
        print(" ", end=' ')
    for j in range(1, i + 1):
        print(i, end=' ')
    for k in range(i - 1, 0, -1):
        print(i, end=" ")
    print('\n')