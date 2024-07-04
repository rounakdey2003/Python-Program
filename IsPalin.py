def ispalindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
        return True


str = input('Enter the string: ')

if ispalindrome(str) == True:
    print('Palindrome')
else:
    print('Not Palindrome')