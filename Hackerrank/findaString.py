# Find how many times a given 'search string' is found in the input string.

string = input()
search_string = input()
count = 0
for i in range(len(string)+1):
    if string[i:i+len(search_string)] == search_string:
        count += 1

print(count)
