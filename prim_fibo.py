def prime(p):
    sum = 0
    for i in range(1,p+1):
        if p%i == 0:
            sum = sum + 1
    if sum == 2:
        return 1
    else:
        return 0


def fibo(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fibo(x-2)+fibo(x-1)



l = int(input('Enter the lower range: '))
u = int(input('Enter the upper range: '))
print("\nThe fibonacci series which are primes are....\n\n")
j = 1
while(fibo(j)<=u):
    if fibo(j)>=l and fibo(j)<=u and prime(fibo(j)):
        print("\t", fibo(j), end=' ')
    j = j+1