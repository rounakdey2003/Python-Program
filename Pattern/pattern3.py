lim = int(input('Enter the maximum limit: '))
i = 0
j = 0
k = 1
for i in range(1, lim + 1):
    for j in range(1, i + 1):
        print(k, end=" ")
        k += 1
    print('\n')
