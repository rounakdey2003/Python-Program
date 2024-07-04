x = int(input("Enter the exponential value: "))
list_1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
mul_list = map(lambda n: pow(n,x), list_1)
print(list(mul_list))
