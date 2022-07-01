# Users\axschouw\OneDrive - coaccess.com\Ex_Files_Python_Automation\Exercise Files\OrganizeMe

#create a dictionary for subdirectories (contains four basic categories)

import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
    }

    #function that returns a catagory based on the file suffix
        #loops through the dictionaries items and returns the category in which the suffix exists
def pickDirectory(value):
        #logic
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            #conditional statment, if the suffix if found, we should return that category
            if suffix == value:
                return category
    #have pickDirectory function return a MISC directory if the file does not exist in our current dictionary
    return 'MISC'

#testing --returns 'DOCUMENTS' in Terminal                
#print(pickDirectory('.pdf'))

#create a function to loop through every item in the current working directory to get the file type, so we can organize it
#check whats in current working directory with OS library scandir
    #will grab every object in the folder, and further the goal of grabbing the extension
def organizeDirectory():
    #loop through all the files in a directory
    for items in os.scandir():
         
        #have the item skiped if it is a directory
        if items.is_dir():
            continue
        
        #return paths of the files with pathlib import path
        filePath = Path(items)
        #isolate the path suffix and determine what directory is should be organized into .suffix attribute returns the files extension
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        #cast to a path to help file movement
        directoryPath = Path(directory)
        #conditional statement if directory the file maps to does not exist then the script should create a new directory with that name
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        #allows file to be moved into the directory by changing the file path to join with the directory's path
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()

       

