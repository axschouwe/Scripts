import sys

def twentyfour_twelve(time):
    
    first = ""
    second = ""
    time_str = ""
    true_string = ""
    msg = "****NOTE: 00:00 and 24:00 = 12am" 
    print(msg)  
    print("     ")
    for char in time:
        
        time_str += char
       
        for char in time_str:
            
            if char.isdigit():
                true_string += char
            
        first += true_string[0:2]
        second += true_string[2:]

        print(time_str)
        print("-----")

        math = int(first) - 2
       
        if math == 20:
            math = 10
        
            print(str(math) + ":" + str(second))

        elif math == 21:
            math = 11
        
            print(str(math) + ":" + str(second))

     

        elif math != 20 and math != 23:

            math = str(math)
            
            print(str(math[1]) + ":" + (second))

          

               

def main():
    arg_1 = sys.argv[1:]
    (twentyfour_twelve(arg_1))

if __name__ == "__main__":
    main()