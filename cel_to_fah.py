def cel(temp):
    cel = (temp - 32) * (5 / 9)
    print('Temperature of  ' + str(temp) + "'F" + '  is  ' + str(cel) + "'C")


def fah(temp):
    fah = (9 / 5) * temp + 32
    print('Temperature of  ' + str(temp) + "'C" + '  is  ' + str(fah) + "'F")


temp = int(input('Enter the temperature in Celsius or Fahrenheit: '))
deg = input('Enter the degree which you want to convert from (F,C): ')

if deg == 'C' or deg == 'c':
    cel(temp)
elif deg == 'F' or deg == 'f':
    fah(temp)
else:
    print('You have chosen a wrong operator!')
