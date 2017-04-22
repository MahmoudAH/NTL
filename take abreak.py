import time
import webbrowser

counter=0
print("the program started on"+time.ctime())
 while counter<3:
    #    time.sleep(2*60*60)

    time.sleep(2)
    webbrowser.open("https://www.youtube.com/watch?v=5aDzqnQ2Jm4")
    counter+=1
    #to stop executeion retart IDIE or use"ctrl + c"