num = int(input("Enter a number: "))
dummy = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if dummy == rev:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
