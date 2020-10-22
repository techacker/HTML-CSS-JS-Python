s = input()

### Workable solution but it is not the best solution.
"""
flag = False
for i in range(len(s)):
    if s[i].isalnum():
        flag = True
print(flag)

flag = False
for i in range(len(s)):
    if s[i].isalpha():
        flag = True
print(flag)

flag = False
for i in range(len(s)):
    if s[i].isdigit():
        flag = True
print(flag)

flag = False
for i in range(len(s)):
    if s[i].islower():
        flag = True
print(flag)

flag = False
for i in range(len(s)):
    if s[i].isupper():
        flag = True
print(flag)
"""

# Alternative better solution
# any() function iterates through all characters in the given string

print(any(i.isalnum() for i in s), 'Great')         # Added 'Great' for an example.
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))