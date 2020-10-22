# Matrix Script : Regex and Parsing - Hard Practice Problem
'''
# Neo has a complex matrix script. The matrix script is a  X  grid of strings. 
# It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

# To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. 
# Neo reads the column from top to bottom and starts reading from the leftmost column.
# If there are symbols or spaces between two alphanumeric characters of the decoded script, 
# then Neo replaces them with a single space '' for better readability.
# Neo feels that there is no need to use 'if' conditions for decoding.
# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
''' 
import re

# Print the text in triple quotes to explain what this program is.
print(__doc__)

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

#print(matrix)
letters = ''
text = r'(?<=\w)([^\w]+)(?=\w)'

for z in zip(*matrix):
    letters += ''.join(z)

print(re.sub(text, " ", letters))
# re.sub - Substitutes the given pattern with the new string, in this case it is ' '.
