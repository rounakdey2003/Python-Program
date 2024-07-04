lim = int(input("Enter the maximum limit: "))
for i in range(1, lim + 1):
    for j in range(1, lim + 1):

        print(str(i*j) + "\t", end=" ")
    print("\n")
