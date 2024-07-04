f = open("a.txt", 'a+')
print(f.closed)
print("Name of the file is",f.name)
f.close()
print(f.closed)

f = open("a.txt", 'ab+')
print(f.closed)
print("Name of the file is",f.name)
f.close()
print(f.closed)

f = open("a.txt", 'w')
line1 = 'Welcome to python.mykvs.in'
f.write(line1)
line2="\nRegularly visit python.mykvs.in"
f.write(line2)
f.close()
f = open("a.txt", 'r')
text = f.read()
print(text)
f.close()



f = open("a.txt", 'r+')
line1 ='Welcome to python.mykvs.in'
f.write(line1)
line2='\nRegular visit python.mykvs.in' 
f.write(line2)
text = f.readline()
print(text)
text = f.readline()
print(text)
f.close()

f = open("a.txt", 'w+')
line1 ='Welcome to python.mykvs.in'
f.write(line1)
line2='\nRegular visit python.mykvs.in' 
f.write(line2)
text = f.readline()
print(text)
text = f.readline()
print(text)
f.close()

f = open("a.txt", 'w')
line1 = 'Welcome to python.mykvs.in'
f.write(line1)
line2="\nRegular visit python.mykvs.in"
f.write(line2)
f.close()
f = open("a.txt", 'r')
text = f.readlines(1)
print(text)
text=f.readlines(1)
print(text)
f.close()

f = open("a.txt", 'w')
line1 = 'Welcome to python.mykvs.in'
f.write(line1)
line2="\nRegular visit python.mykvs.in"
f.write(line2)
f = open("a.txt", 'r')
text = f.readlines(1)
print(text)
text=f.readlines(1)
print(text)
f.close()

f = open("a.txt", 'w')
line1 = 'Welcome to python.mykvs.in'
f.write(line1)
line2="\nRegularly visit python.mykvs.in"
f.write(line2)
line3='\nMy name is XYZ'
f.write(line3)
f.close()
f = open("a.txt", 'r')
for text in f.readlines():
  print(text)
f.close()

f = open("a.txt", 'r+')
line1 = 'Welcome to python.mykvs.in'
f.write(line1)
line2="\nRegularly visit python.mykvs.in"
f.write(line2)
line3='\nMy name is XYZ'
f.write(line3)
for text in f.readlines():
  print(text)
f.close()

f = open("a.txt", 'w')
line1 = 'Welcome to python.mykvs.in'
f.write(line1)
line2="\nRegularly visit python.mykvs.in"
f.write(line2)
f.close()
f = open("a.txt", 'r')
for text in f.readlines():
  for word in text.split( ):
    print(word) 
f.close()

f = open("a.txt", 'w')
line = 'Welcome to python.mykvs.inRegularly visit python.mykvs.in'
f.write(line)
f.close()
f = open("a.txt", 'a+')
f.write("thanks")
f.close()
f = open("a.txt", 'r')
text = f.read()
print(text)
f.close()

f = open("a.txt", 'w')
line = 'Welcome to python.mykvs.in\nRegularly visit python.mykvs.in'
f.write(line)
f.close()
f = open("a.txt", 'rb+')
print(f.tell())
print(f.read(7)) # read seven characters
print(f.tell())
print(f.read())
print(f.tell())
f.seek(9,0) # moves to 9 position from begining
print(f.read(5))
f.seek(4, 1) # moves to 4 position from current location
print(f.read(5))    
f.seek(-5, 2) # Go to the 5th byte before the end
print(f.read(5))
f.close()

import sys
a = sys.stdin.readline()
sys.stdout.write(a)
a = sys.stdin.read(5)#entered 10 characters.a contains 5 characters.
#The remaining characters are waiting to be read.
sys.stdout.write(a)
b = sys.stdin.read(5)
sys.stdout.write(b)
sys.stderr.write(" custom error message")

import os
print(os.getcwd())
os.mkdir("newdir")
os.chdir("newdir")
print(os.getcwd())