
dict = {}

dict[0] = {"Name": "Rahul", "Roll": 22, "Result": 88}
dict[1] = {"Name": "Rahul", "Roll": 22, "Result": 88}
dict[2] = {"Name": "Rahul", "Roll": 22, "Result": 88}
dict[3] = {"Name": "Rahul", "Roll": 22, "Result": 88}
dict[4] = {"Name": "Rahul", "Roll": 22, "Result": 88}

for y in range(0,5):   
    for x in dict:
        print(x,":", dict[y][x])
    




# Creating an empty dict
myDict = dict()

# Creating a list
valList = ['1', '2', '3']

# Iterating the elements in list
for val in valList:
	for ele in range(int(val), int(val) + 2):
		myDict.setdefault(ele, []).append(val)

print(myDict)



# Importing defaultdict
from collections import defaultdict

lst = [('Geeks', 1), ('For', 2), ('Geeks', 3)]
orDict = defaultdict(list)

# iterating over list of tuples
for key, val in lst:
	orDict[key].append(val)

print(orDict)




# Python program to demonstrate
# Adding Elements to a Array

# importing "array" for array creations
import array as arr

# array with int type
a = arr.array('i', [1, 2, 3])


print ("Array before insertion : ", end =" ")
for i in range (0, 3):
	print (a[i], end =" ")
print()

# inserting array using
# insert() function
a.insert(1, 4)

print ("Array after insertion : ", end =" ")
for i in (a):
	print (i, end =" ")
print()

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

print ("Array before insertion : ", end =" ")
for i in range (0, 3):
	print (b[i], end =" ")
print()

# adding an element using append()
b.append(4.4)

print ("Array after insertion : ", end =" ")
for i in (b):
	print (i, end =" ")
print()






# Python program to demonstrate
# Removal of elements in a Array

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 5])

# printing original array
print ("The new created array is : ", end ="")
for i in range (0, 5):
	print (arr[i], end =" ")

print ("\r")

# using pop() to remove element at 2nd position
print ("The popped element is : ", end ="")
print (arr.pop(2))

# printing array after popping
print ("The array after popping is : ", end ="")
for i in range (0, 4):
	print (arr[i], end =" ")

print("\r")

# using remove() to remove 1st occurrence of 1
arr.remove(1)

# printing array after removing
print ("The array after removing is : ", end ="")
for i in range (0, 3):
	print (arr[i], end =" ")




