import os
def file():
    # 1-get name files
    file_list = os.listdir(r"C:\Users\Mahmoud\Desktop\udacity\prank\prank")
    print(file_list)
    path=os.getcwd()
    print("path ="+path)
    os.chdir(r"C:\Users\Mahmoud\Desktop\udacity\prank\prank")
    # 2-for each and rename
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None, "0123456789"))
    os.chdir(path)
file()
