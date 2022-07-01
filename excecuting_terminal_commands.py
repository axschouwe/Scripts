#C:\Users\axschouw\OneDrive - coaccess.com\Ex_Files_Python_Automation\Exercise Files>

#to implement automating terminal commands using subprocess library, allows python script to interact with the command line interface, subprocess contains many functions that can run terminal commands.

import subprocess
import sys

#iterate through the script 5 times
for i in range (0,5):
    #check-call function, runs an executable in terminal and waits for the process to finish before continuing our script
    # the first element sys.executable - runs an executable, second element is our cmd line argument
    subprocess.check_call([sys.executable, 'example.py'])