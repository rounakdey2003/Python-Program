#dict = {["Name": "Rounak"; "A"; "B"],["Age": 18; 15; 17]}

#print(dict["Name"])
#print('\n')
#print(dict["Age"])


#fruits = {'banana':3,'apple':2, 'mango':1, 'kiwi':5}
#fruits_list = [[fruit]*quantity for fruit, quantity in fruits.items()]
#print(fruits_list)


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


#lim = int(input("Enter the max limit for which the item will be printed: "))

#item_list = { ' banana '
#%%
