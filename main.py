import os
from os import listdir
from os.path import isfile, join
import shutil


# copying the files to the destination
def copyFiles (list, destination):
    for i in list:
        shutil.copy(i,destination)

        
# print the current dir
print(os.getcwd())

# setting the Original and destination
original = r'C:\Users\gorraf02\Desktop\Billing'
target = r'C:\Users\gorraf02\Desktop\Billing\test'

# Print how many files are there
print (len([name for name in os.listdir(os.chdir(original))]))

# adding the files names in a list
onlyfiles = [f for f in listdir(original) if isfile(join(original, f))]
print (onlyfiles)

copyFiles(onlyfiles, target)


