lim = int(input('Enter the maximum limit: '))
i = 0
j = 0
for i in range(1, lim + 1):
    for k in range(lim, i, -1):
        print(" ", end=' ')
    for j in range(1, i + 1):
        print(i, end=' ')
    print('\n')