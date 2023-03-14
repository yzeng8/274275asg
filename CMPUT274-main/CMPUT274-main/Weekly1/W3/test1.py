words = input("Enter:").split()
frequency = {}    
for word in words:
    frequency[word] = frequency.setdefault(word,[])
    value = words.count(word)
    frequency[word] = value
sorted(frequency, reverse = False)
name = list(frequency)
num = list(frequency.values())
percent = []
for i in range(0,len(num)):
    fre = round(num[i]/sum(num), 3)
    for keys in frequency:
        frequency[keys].append(fre)


print(frequency)

