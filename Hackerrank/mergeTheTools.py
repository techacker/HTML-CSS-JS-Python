string = input()
k = int(input())

while string:
    s = string[0:k]
    print(s)
    seen = ''
    for c in s:
        if c not in seen:
            seen += c
    print(seen)
    string = string[k:]




