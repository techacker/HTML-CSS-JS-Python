n = input()
swapped = []


for words in n:
    for i in range(len(words)):
        if words[i] == words[i].lower():
            swapped.append(words[i].upper())
        else:
            swapped.append(words[i].lower())
    
            
print(''.join(swapped))
