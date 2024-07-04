import math

lim = int(input('Enter the maximum limit: '))
i = 0
j = 0
add = 0
for i in range(1, lim + 1):
    j = i
    add += math.pow(i, j)
    print(i, '^', j, end='')
    print(end=' +  ')
print('\b\b\b=', add, end='')



