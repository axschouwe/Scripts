import sys

def passwrd(file):

    string = ""
    count = 0
  

    for char in file:
        string += char
        
        upper = ""
        upper += string[:2]
        upper = upper.upper()
        
 
        for char in string:
            count += 1
            
            if char == "h" or char == "H":
                string = string.replace(char, "@")
            elif char == " ":
                string = string.replace(char, "")
            elif char == "A" or char == "a":
                string = string.replace(char, str(4))
            elif char == "E" or char == "e":
                string = string.replace(char, str(3))
            elif char == "T" or char == "t":
                string = string.replace(char, "+")
            elif char == "I" or char == "i": 
                string = string.replace(char, ":")
            elif char == "o" or char == "O": 
                string = string.replace(char, "*")  
            elif char == "U" or char == "u": 
                string = string.replace(char, "!")
         
        print(upper + str(count / 3.14) + (string))


def main():
    file = sys.argv[1]
    with open(file) as open_file:
    
       passwrd(open_file)
    
    

if __name__ == '__main__':
    main()
