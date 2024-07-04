num = int(input('Enter any number: '))
num1 = num
flag = 0
while not num == 0:
    r = num % 10
    if r == 0:
        flag = 1
        break
    num = num // 10
if flag == 0:
    print('The number ' + str(num1) + ' is not a duck number')
else:
    print('The number ' + str(num1) + ' is a duck number')

