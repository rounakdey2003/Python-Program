str = input("Enter the name: ")
word = str.split()
name = ""
for i in range(len(word)-1):
    str = word[i]
    name = name + (str[0].upper()+'.')
name = name + word[-1].title()
print(name)