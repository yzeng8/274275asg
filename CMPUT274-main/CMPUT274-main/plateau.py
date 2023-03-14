# Good luck! Write your solution below.
words = input('').split()
a = 1
b = []
b.append(a)
p = {}
if len(words) == 1:
    print(a)
else:
    for i in range(1,len(words)): 
        if words[i] == words[i-1]:
            p[words[i]] = p.setdefault(words[i],1)+1
            b.append(max(list(p.values())))
        else:
            p[words[i]] =1
    print(max(b))