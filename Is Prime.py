def is_prime(low, up):
    for i in range(low, up + 1):
        sum = False
        for j in range(low, i + 1):
            if i%j == False:
                sum = sum + 1
        if sum == 2:
            print(i, end=", ")

low = int(input("Enter the minumum limit: "))
up = int(input("Enter the minimum limit: "))
print(is_prime(low, up))
