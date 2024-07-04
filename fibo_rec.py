def fibo(lim):
    if lim == 1:
        return 1
    elif lim == 2:
        return 1
    else:
        return fibo(lim - 1) + fibo(lim - 2)


lim = int(input('Enter the nth term = '))
print('The fibonacci series is = ', end='')
for i in range(1, lim + 1):
    print(fibo(i), end=', ')
print('\b\b')
