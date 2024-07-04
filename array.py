print("\nIndices of Max element\n")
import numpy as np

#array = np.arange(12).reshape(3, 4)
list1 = [0, 1, 2, 11]
list2 = [4, 9, 6, 3]
list3 = [8, 5, 10, 7]

array = np.array([list1, list2, list3])
print("INPUT ARRAY : \n", array)
print("\nMax element : ", np.argmax(array))
print("\nIndices of Max element : ", np.argmax(array, axis=0))
print("\nIndices of Max element : ", np.argmax(array, axis=1))

print("\nMapping of the array\n")
import pandas as pd

df = pd.DataFrame([[0, 1, 2, 11], [4, 9, 6, 3], [8, 5, 10, 7]])
map = df.applymap(lambda x: len(str(x)))
print("\nMap: \n", map)

print("\nAdding 5 to each element in the matrix\n")
for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j]+=5
print(array)

print("Adding 5 to the element of the matrix using applymap\n")
def add_5_ele(element):
    return element+5
def add_5_mat(matrix):
    return matrix.applymap(add_5_ele)


list1 = [0, 1, 2, 11]
list2 = [4, 9, 6, 3]
list3 = [8, 5, 10, 7]

array = np.array([list1, list2, list3])
print("INPUT ARRAY : \n", array)

df = pd.DataFrame(array)

result = add_5_mat(df)
print("\nOutput array: \n", result)

print("\n Using apply function\n")

sqrt = df.apply(np.sqrt)
print("Square root: \n", sqrt)

sum = df.apply(np.sum, axis=0)
sum2 = df.apply(np.sum, axis=1)
print("\nSum for axis 0 (column): \n", sum)
print("\nSum for axis 1 (row): \n", sum2)
