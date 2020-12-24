import os
from os import listdir
from os.path import isfile, join, isdir
import shutil

# Function takes the list of files and the destination and copies the list of files int o the destination
def copyFiles (list, destination):
    for i in list:
        shutil.copy(i,destination)

# setting the Original and destination from the user

original = input("Please enter the location of error files : ")
#target = input("Please enter the location of current billing month : ")

# calculate how many folders are there and savinf them in a list
foldersList = [name for name in listdir(original) if isdir(join(original, name))]
numberOfFolders = len(foldersList)


# adding the files names in a list
filesList = [f for f in listdir(original) if isfile(join(original, f))]
numberOfFiles = len(filesList)



## copyFiles(filesList, target)
