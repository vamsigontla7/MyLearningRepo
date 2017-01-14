import os

def renameFiles() :
    # 1. Get all file names from a folder
    file_list = os.listdir("C:\Python27\exercise\prank")
    print file_list

    curr_dir = os.getcwd()
    print ("Current working directory is ::: "+curr_dir)
    os.chdir("C:\Python27\exercise\prank");
        
    # 2. For each file, rename the file
    for file_name in file_list :
        print("Old Name ::: "+file_name)
        print("New Name ::: "+file_name.translate(None, "0123456789()"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
renameFiles()
exit
