import random


def biased_rolls(prob_list, s, n): 
    random.seed(s) # make seed of this random s
    result = [] # create an empty list for later
    
    for x in range(n): # A for loop for n times
        toss = random.random() # random float number from [0,1)

        for i in range(0,len(prob_list)): # index all the possibility in the pro_list
            totalpossibility = sum(prob_list[0:i+1]) # sum of all the possiblity in the prob_list have occured
        
            if toss <= totalpossibility: # when the random number is less than the sum above, add it to the result list above
                a = i+1
                result.append(a)
                break
            
    return result
    pass

def draw_histogram(m, rolls, width):
    
    ##create an empty dictionary..
    frequency_raw = {}
    
    ### print the title
    print('Frequency Histogram: ' + str(m) + '-sided Die') # Print the name of the histogram
    
    ### get the item and value into dictionary
    for item_value in range(1, m+1):
        frequency_raw[item_value] = rolls.count(item_value)
    
    ###get the max frequency
    max_frequency = max(frequency_raw.values())
    
    ##### display
    for key_value in frequency_raw:
        #print("key: "+str(key_value))
        ### get the scalar per count
        frequency_raw[key_value] = round(frequency_raw[key_value] * width / max_frequency )
    
        print(str(key_value)+'.'+'#' * frequency_raw[key_value]  + '-' * round(width - frequency_raw[key_value]))
    pass


if __name__ == "__main__":
    rolls = biased_rolls()
    print(rolls)
    draw_histogram()
    pass
    