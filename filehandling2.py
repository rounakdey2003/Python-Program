def func1():
  f=open("fcont.txt","w")
  name=input("Enter name:")
  rollno=int(input("Enter roll number:"))
  marks=int(input("Enter number:"))
  f.close()
 

def func2():
  f=open("fcont.txt","r")
  for text in f.readlines():
    print(text)
  f.close()

func1()
func2()

# Create a new file
def func1():

  f=open("fcont.txt","w")
  name=input("Enter name: ")
  f.write(name)
  rollno=int(input("Enter roll number: "))
  f.write(str(rollno))
  marks=int(input("Enter marks: "))
  f.write(str(marks))
  f.close()
 
# Copy contents of the above file to another file 
def func2():

    # To open the first file in read mode
    f1 = open("fcont.txt", "r")

    # To open the second file in write mode
    f2 = open("sample.txt", "w")

    # For loop to traverse through the file
    for line in f1:

	      # Writing the content of the first
	      # file to the second file
	
    	  # Using upper() function to
	      # capitalize the letters
	      f2.write(line.upper())
    f1.close()
    f2.close()

# Print contents of the copied file 
def func3():
    f1=open("fcont.txt","r")
    for line in f1:
        print(line,end="\n")


#main function

func1()
func2()
func3()

# open both files
with open('fcont.txt','r') as firstfile, open('second.txt','w') as secondfile:
	
    # read content from first file
    for line in firstfile:
			
			  # write content to second file
        print(line)
        secondfile.write(line)

