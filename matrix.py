# list1 = input("Enter the elements of first list: ").split()
# list2 = input("Enter the elements of the second list: ").split()
# list1 = [int(elements) for elements in list1]
# list2 = [int(elements) for elements in list2]
# matrix = [list1, list2]
# for rows in matrix:
#    print(rows)

import numpy as np


def user_input():
    input_user = input("Enter the elements of the list: ").split()
    return [int(elements) for elements in input_user]


list1 = user_input()
list2 = user_input()
list3 = user_input()
list4 = user_input()

matrix1 = [list1, list2]
matrix2 = [list3, list4]

if len(matrix1) != len(matrix2):
    print("Matrix multiplication is incompatible")
else:
    print("Matrix multiplication is compatible")
    result = [[0, 0], [0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    for rows in result:
        print(rows)

print("\nUsing numpy")
result1 = np.dot(matrix1, matrix2)
for rows1 in result1:
    print(rows1)
