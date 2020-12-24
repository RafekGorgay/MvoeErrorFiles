import os
from os import listdir
from os.path import isfile, join, isdir
import shutil

# setting the Original and destination from the user
original = input("Please enter the location of error files : ")
target = input("Please enter the location of current billing month : ")

# identify file list
filelist = []

# adding folders to a List
foldersList = [name for name in listdir(original) if isdir(join(original, name))]
# Calculate the number of folders
numberOfFolders = len(foldersList)

for i in foldersList:

    # go inside each states folder for both destination and source
    ErrorFilesFolder = original + '\\' + i + "\\" + "Unzip_Error"
    tagetFolder = target + '\\' + i
    
    # Printing the state that is accessed
    print(i)

    # Coping the files into the destination
    try:
        filesList = [f for f in listdir(ErrorFilesFolder) if isfile(join(ErrorFilesFolder, f))]
        numberOfFiles = len(filesList)
        print ("Number of files that will be copied: ",numberOfFiles)
        
        # copying all files
        for i in filesList:
            shutil.copy(os.path.join(ErrorFilesFolder, i ),tagetFolder)
    except FileNotFoundError:
        print("Unzip_Error Folder does not exist")
    
    # resetting the filelist and delete the Unzio_Error folder
    filelist = 0
    shutil.rmtree(ErrorFilesFolder)