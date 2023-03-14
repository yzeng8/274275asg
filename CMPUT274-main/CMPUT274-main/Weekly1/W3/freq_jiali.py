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

def validate_file_input():

    for t in sys . argv :
        print (" |{}| ". format (t))
    
    ### check argument list too few
    if len(sys.argv) <= 1:
        print ("Too few arguments. Usage: python3 freq.py <input file name>")
        sys.exit()

    ### check argument list too many
    if len(sys.argv) >= 3:
        print ("Too many arguments. Usage: python3 freq.py <input file name>")
        sys.exit()
         
    ### check file existence
    filename = sys.argv[1]
    bExists = os.path.exists(filename);
    if bExists == False:
        print("\nError........" + filename + "...No files to parse.........................\n\n")
        sys.exit();

    return filename


def freq(filename_source):
    file_source = open(filename_source,"r", encoding = 'utf-8')
    words = file_source.read().split()
    file_source.close()
    
    frequency = {}
        
    for word in words:
        frequency[word] = frequency.setdefault(word,[])
        value = [words.count(word), round(words.count(word)/len(words), 3)]
        frequency[word] = value
    
    filename_destination = filename_source + '.out'
    file_destination = open(filename_destination,"w", encoding = 'utf-8')
    
    for key_value in sorted(frequency.keys()):
        file_destination.write( format(key_value)+" "+ format(frequency[key_value][0])+ " "+format(frequency[key_value][1]) + "\n")
    
    file_destination.close()


if __name__ == '__main__':
    filename_local = validate_file_input()
    freq(filename_local)
    pass

