import os #operating system
import shutil #standard utilities

source = input("Enter the source folder name: ")
destination = input("Enter the destination folder name: ")

#folder2/file2.txt
source = source + "/"
destination = destination + "/"

listOfFiles = os.listdir(source)
for i in listOfFiles:
    shutil.copy((source+i), destination)
