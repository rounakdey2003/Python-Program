def num(a, b):
    if a > b:
        sub = lambda a, b: a - b
        print("The subtraction of the two numbers are = ",sub(a, b))
        
    else:
        print('First number is less than the second number so it cannot subtracted so')
        add = lambda a, b: a + b
        print("The addition of the two numbers are is = ",add(a, b))

a = int(input('Enter the first number = '))
b = int(input('Enter the second number = '))
print('\n')
print(num(a, b))
        
