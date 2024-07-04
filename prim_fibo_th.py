def prime(p):
    flag = 0
    for i in range(2, p):
        if p % i == 0:
            flag = 1
            break
    if flag == 0:
        return 1
    else:
        return 0


def fibo(f):
    if f == 1:
        return 1
    elif f == 2:
        return 1
    else:
        return fibo(f-1)+fibo(f-2)


l = int(input('Enter the lower value: '))
u = int(input('Enter the upper value: '))
j = 1    
for i in range(l, u + 1):
    if (fibo(j) == i and prime(i)):
            print('\t',i,j, end=" ")
    j = j+1
    