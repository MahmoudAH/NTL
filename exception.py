def main():
 try:
    readfile=open("hello444.txt", "r")
    for line in readfile:
        print(
            line
        )
    readfile.close()
 except IOError:

    print("file not found")
 else:
     print("seccessful file reading")
 print("no problem")
if __name__ == '__main__':main()
