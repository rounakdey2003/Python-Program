n = int(input("Enter the row: "))
pascal = []

for i in range(n):
    row_val = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row_val.append(1)
        else:
            row_val.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
    pascal.append(row_val)

# Printing Pascal's Triangle
for row_val in pascal:
    print(" ".join(map(str, row_val)).center(n * 3))
