str = input("Enter a string: ")
ford = str.casefold()
rev = reversed(ford)
if list(ford) == list(rev):
    print("String is a palindrome")
else:
    print("String is not a palindrome")