#--------------------------------------------
#   Name: Steven Xu
#   ID: 1663052
#   CMPUT 274
#
#   Weekly Exercise 3: Word Frequency
#-------------------------------------------- 
# FREQ TEMPLATE: ADD YOUR INFORMATION TO ABOVE


import sys
import os

def demo_command_line():
    try:
        print(sys.argv[0])
        filename = sys.argv[1]
        print(filename)
    except FileNotFoundError:
        return("Too many arguments. Usage: python3 freq.py <input file name>")

    return(filename)

filename = str(sys.argv[1])

def freq():
    f = open(sys.argv[1],"r")
    words = f.readlines().split()
    frequency = {}
        
    for word in words:
        frequency[word] = frequency.get(word,0) + 1
        
    a = sorted(frequency.items(), reverse = False)
    frequency = dict(a)    
    
    name = list(frequency)
    num = list(frequency.values())

    filename = filename + '.out'
    outfile = open(filename,"w")
    
    for i in range(0,len(num)):
        fre = round(num[i]/sum(num), 3)
        fre = str(fre)
        info = (name[i],num[i],fre)
        outfile.write(info)
        outfile.write(./)
    outfile.close()

    f.close()

if __name__ == '__main__':
    demo_command_line()
    freq()

    pass

