def arm(a, b):
    for i in range(a, b + 1):
        s = 0
        n = i
        while n > 0:
            d = n % 10
            s = s + (d ** 3)
            n = n // 10
        if s == i:
            print(s, end=", ")
    print("\b\b", end="")
    return a, b


def step():
    print('''Step 1: Creating a "module_name.py" file, having one or more functions suitable for the purpose. 
    The function or set of functions in that "module_name.py" file will be called a module''')
    print("\n\tConclution: Any python file can be used as a module")
    print('''\n\nStep 2: import the name of the module in the new python program.
    Use the function within that module by using "module_name.function_name()''')
