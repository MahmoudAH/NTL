import re
def main():
     readfile=open("hello.txt","r")
     for line in readfile:
         if re.search("(b|a)a",line):

          print(line)


     readfile.close()
if __name__ == '__main__':main()
