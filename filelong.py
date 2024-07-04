#filelong function
def filelong(f):
          max_length = 0
          max_len_line = ''
          file = open(f,"a")
          for line in file:
              if(len(line) > max_length):
                  max_length = len(line)
                  max_len_line = line
          print(max_len_line)

#file function
def main():
          f=open("test.txt","w")
          l1="Python is a good Programming lanhuage"
          l2="My name is Kalpajit"
          l3="I study in Class 12"
          f.write(l1)
          f.write(l2)
          f.write(l3)
          f.close()
          print("file function working ....")
          filelong(f)

if __name__=='__main__':
          main()

