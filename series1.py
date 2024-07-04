import math

lim = int(input('Enter maximum limit: '))
i = 0
add = 0
for i in range(1, lim + 1):
    add = add + math.pow(i, 2)
    print(i, '^ 2', end='')
    print(end=' +  ')
print('\b\b\b=', add, end='')
