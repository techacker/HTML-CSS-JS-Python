#
#Find all words that end in "s" and print them together separated by an underscore.
#Sample Input 1:
#First ladies rule the State and state the rule: ladies first
#Sample Output 1:
#ladies_ladies


text = input().split()
length = len(text)
word = []

if length == 1:
    print(text[0].lower())
else:
    word.append(text[0])
    for i in range(1, length):
        word.append(text[i].title())
    print(''.join(word))
    
