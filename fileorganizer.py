import os 
import shutil

folderpath= input("Enter the name of the folder to be sorted: ")

#Creatiing a list of all the items in the folder
listofFiles= os.listdir(folderpath)

for i in listofFiles:
    name, ext= os.path.splitext(i)

    #Creating a list to store all the extension types (: - selects all)
    ext= ext[1:]

    #If we encounter a folder - continue
    if ext== "":
        continue
    
    #Checking if the directory already exists
    if os.path.exists(folderpath+"/"+ext):
        shutil.move(folderpath+"/"+i,folderpath+"/"+ext+"/"+i)
    #When the directory isn't created yet
    else:
        os.makedirs(folderpath+"/"+ext)
        shutil.move(folderpath+"/"+i, folderpath+"/"+ext+"/"+i)