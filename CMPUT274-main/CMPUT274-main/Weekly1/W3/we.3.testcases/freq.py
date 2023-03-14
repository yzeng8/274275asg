#--------------------------------------------
#   Name: Steven Xu
#   ID: 1663052
#   CMPUT 274
#
#   Weekly Exercise 3: Word Frequency
#-------------------------------------------- 
# FREQ TEMPLATE: ADD YOUR INFORMATION TO ABOVE


import sys

def validate():    
    filename = sys.argv[1]

    for t in sys . argv :
        print (" |{}| ". format(t))
    
    ### check argument list too few
    if len(sys.argv) == 1:
        print ("Too few arguments. Usage: python3 freq.py <input file name>")
        sys.exit()

    ### check argument list too many
    if len(sys.argv) >= 3:
        print ("Too many arguments. Usage: python3 freq.py <input file name>")
        sys.exit()
         
    return filename


def freq(source):
    fsource = open(source,"r")
    words = fsource.read().split()
    fsource.close()
    
    frequency = {}
        
    for word in words:
        frequency[word] = frequency.setdefault(word,[])
        value = [words.count(word), round(words.count(word)/len(words), 3)]
        frequency[word] = value
    
    fileoutname = source + '.out'
    fileout = open(fileoutname ,"w")
    
    for key_value in sorted(frequency.keys()):
        fileout.write( format(key_value)+" "+ format(frequency[key_value][0])+ " "+format(frequency[key_value][1]) + "\n")
    
    fileout.close()


if __name__ == '__main__':
    fileinput = validate()
    freq(fileinput)
    pass
