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

def palin(p):
    rev = 0
    num = p
    while p != 0:
        rem = p % 10
        rev = rev * 10 + rem
        p = p // 10
    if num == rev:
        return 1
    else:
        return 0


low = int(input('Enter the lower range: '))
up = int(input('Enter the upper range: '))

for i in range(low,up+1):
    if prime(i) == 1 and palin(i) == 1:
        print(i, end=" ")