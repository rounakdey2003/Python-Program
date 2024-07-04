# Initialize the dictionary
fruits = {'banana':3,'apple':2, 'mango':1, 'kiwi':5}

# Create blank list to append to
fruits_list = []

# Create the for loop
for fruit, quantity in fruits.items():
    # Append the list to the main list
    fruits_list.append([fruit]*quantity)

# Print out the final list
print(fruits_list)
