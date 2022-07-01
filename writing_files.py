#open and read a file
from os import linesep

#Use Directory  C:\Users\axschouw\OneDrive - coaccess.com\Ex_Files_Python_Automation\Exercise Files

##File IO basics writing files##

f = open('inputFile.txt','r') #'r' to read
#specify file name to write
passFile = open('PassFile.txt','w') #'w' to write
failFile = open('FailFile.txt','w')

#iterate through the file and count each line
for line in f:
    #split the line at the whitespace
    line_split = line.split()
    #see if the 'P' is the 3rd element in the line
    if line_split[2] == 'P':
        #write function
        passFile.write(line)
    #write to FailFile if 3rd element is a 'F'
    else:
        failFile.write(line)
#close the file
f.close()
passFile.close()
failFile.close()