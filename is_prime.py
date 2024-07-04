def is_prime(i):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        return 1
    else:
        return 0


l = int(input('\nEnter the lower limit: '))
u = int(input('\nEnter the upper limit: '))
print('\nThe prime number between ', l,' and ', u,' are....')
for i in range(l,u+1):
    if is_prime(i):
        print(i, end=" ")
