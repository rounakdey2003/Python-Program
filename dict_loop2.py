fruits = {'banana':3,'apple':2, 'mango':1, 'kiwi':5}
fruits_list = [[fruit]*quantity for fruit, quantity in fruits.items()]
print(fruits_list)
