#Use Directory  C:\Users\axschouw\OneDrive - coaccess.com\Ex_Files_Python_Automation\Exercise Files

#Read a file, File IO
    #provide the file name and how you want to interact with that file
f = open('inputFile.txt', 'r') #'r' to read
#count = 0
#print(f.read())

#iterate through the file and count each line
for line in f:
    #split the line at the whitespace
    line_split = line.split()
    #see if the 'P' is the 3rd element in the line
    if line_split[2] == 'P':
        print(line)

    
    #Count line by line#   
    # print(str(count) + line)
    # count = count + 1

#close the file
f.close()
