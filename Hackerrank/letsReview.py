# Given a string, S, of length N that is indexed from 0 to N-1.
# Print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line.

T = int(input())        # The number of test cases.
words = []

# Iterate over T to received number of strings and store then in words list.
for _ in range(T):
    S = input()            # String input
    words.append(S)

# Iterate over words list.
for word in words:
    evenletters = ""
    oddletters = ""
    for i in range(len(word)):
        if i == 0 or i % 2 == 0:
            evenletters = evenletters + word[i]
        else:
            oddletters = oddletters + word[i]
    print(evenletters + ' ' + oddletters)
