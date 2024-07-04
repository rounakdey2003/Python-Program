a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
str = input('Enter the operator: ')
arr = list(str)
c = arr[0]
if c == '+':
    result = lambda a, b: a + b
elif c == '-':
    result = lambda a, b: a - b
elif c == '*':
    result = lambda a, b: a * b
elif c == '/':
    result = lambda a, b: a / b
else:
    print('You have chosen a wrong operator')
print("The result is = ", result(a, b))
#%%