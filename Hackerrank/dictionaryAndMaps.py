# Day 8: Dictionaries and Maps
# Task
# Given 'n' names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
# You will then be given an unknown number of names to query your phone book for. 
# For each 'name' queried, print the associated entry from your phone book on a new line in the form name = phoneNumber
# if an entry for 'name' is not found, print 'Not found' instead.

# Input Format

# The first line contains an integer, 'n', denoting the number of entries in the phone book.
# Each of the 'n' subsequent lines describes an entry in the form of 2 space-separated values on a single line. 
# The first value is a friend's name, and the second value is an 8-digit phone number.
# 
# After the 'n' lines of phone book entries, there are an unknown number of lines of queries. 
# Each line (query) contains a 'name' to look up, and you must continue reading lines until there is no more input.

n = int(input())
phonebook = {}
query = []

# Create Phonebook
# Using for loop...a lengthy way
#for _ in range(n):
#    nameandNum = list(map(str, input().split()))
#    phonebook.update({nameandNum[0]: nameandNum[1]})
# Shorter method:
nameandNum = [map(str, input().split()) for _ in range(n)]
phonebook = {k: v for k, v in nameandNum}

while True:
    search = input()
    if search == '':
        break
    else:
        query.append(search)

for name in query:
    if name in phonebook:
        print(name +'='+ phonebook[name])
    else:
        print('Not found')
