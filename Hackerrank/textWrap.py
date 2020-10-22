string = input()
max_width = int(input())

def wrap(string, max_width):
    return '\n'.join([string[_:_+max_width] for _ in range(0,len(string),max_width)])

result = wrap(string, max_width)
print(result)


# Alternative solution that also works

#for i in range(0,len(s),w):
#    print(s[:w])
#    s = s[w:]
#    if len(s) < w:
#        print(s)
#        break

