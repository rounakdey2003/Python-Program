a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
str = input('Enter the operator: ')
arr = list(str)
c = arr[0]
result = 0
if c == '+':
    result = a + b
elif c == '-':
    result = a - b
elif c == '*':
    result = a * b
elif c == '/':
    result = a / b
else:
    print('You have chosen a wrong operator')
print("The result is = ", result)

#%%
