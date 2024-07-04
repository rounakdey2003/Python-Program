num = [22, 45, 25, 89, 98, 32, 68, 84, 91, 87]
print("Numbers before sorting: ")
print(num)

even = list(filter(lambda n: n%2 == 0, num))
print("\nNumbers after sorting (Even): ")
print(even)

odd = list(filter(lambda n: n%2 == 1, num))
print("\nNumbers after sorting (Odd): ")
print(odd)