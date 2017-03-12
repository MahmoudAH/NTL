def main():
   # out=open("hello.txt","w") #to delet old and add new
    out = open("hello.txt", "a") #to add alla elqdem
    out.write('welcome to python\n i wil won \n alla karim')
    out.close()
    readfile=open("hello.txt","r")
    for line in readfile:
        print(
            line
        )
    readfile.close()
if __name__ == '__main__':main()
