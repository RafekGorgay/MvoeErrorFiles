import os
from os import listdir
from os.path import isfile, join, isdir
import shutil


# Function takes the list of files and the destination and copies the list of files int o the destination
def copyFiles (list, destination):
    for i in list:
        shutil.copy(i,destination)


# setting the Original and destination
original = os.getcwd()
target = r'C:\Users\gorraf02\Desktop\Billing\test'



# print the current dir
print(os.getcwd())

foldersName = [name for name in listdir(original) if isdir(join(original, name))]

# calculate how many folders are there
numberOfFiles = len(foldersName)
print (numberOfFiles)


# adding the files names in a list
onlyfiles = [f for f in listdir(original) if isfile(join(original, f))]
print (onlyfiles)

## copyFiles(onlyfiles, target)


