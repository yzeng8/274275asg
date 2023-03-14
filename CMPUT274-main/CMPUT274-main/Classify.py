Count = 0
word = ""
while word != "Exit":
    word = input("Word:")
    if word == 'the':
        Count = Count + 1 
    elif word == 'The':
        Count = Count + 1
    print(Count)
       
