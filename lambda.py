def filters(a):
    result = filter(lambda x: x > 33, a)
    print('The result is = ', end='')
    print(list(result))


def maps(a):
    result = map(lambda x: pow(x, x), a)
    print('The result is = ', end='')
    print(list(result))


def reduce(a):
    from functools import reduce

    result = reduce(lambda x, y: x * y, a)
    print('The result is = ', end='')
    print(result)


a = []
n = int(input("Enter the sequences: "))
for i in range(0, n):
    lists = int(input())
    a.append(lists)

fun = input('Enter the function: ')

if fun == 'f':
    filters(a)

elif fun == 'm':
    maps(a)

elif fun == 'r':
    reduce(a)

else:
    print('Wrong Operater')

