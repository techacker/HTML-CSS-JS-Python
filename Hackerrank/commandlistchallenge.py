print('The program performs the given function on a list in a recursive manner.')
print('First enter an "Integer" to tell how many functions you would like to do.')
print('Then enter the command with appropriate values.')
print()
print('Enter an integer.')
N = int(input())
z = []

def operation(inst, item, ind):
    if inst == 'append':
        z.append(item)
        return z
    elif inst == 'insert':
        z.insert(ind, item)
        return z
    elif inst == 'remove':
        if item in z:
            z.remove(item)
        return z
    elif inst == 'sort':
        z.sort()
        return z
    elif inst == 'pop':
        z.pop(-1)
        return z
    elif inst == 'reverse':
        z.reverse()
        return z
    elif inst == 'print':
        print(z)
        #continue
    
print("Now enter a command in format: 'list_operation number number'")

for i in range(N):
    commands = input().split(sep=" ")
    if len(commands) == 1:
        inst = commands[0]
        ind = None
        item = None
    elif len(commands) == 2:
        inst = commands[0]
        ind = None
        item = int(commands[1])
    elif len(commands) == 3:
        inst = commands[0]
        ind = int(commands[1])
        item = int(commands[2])
    
    operation(inst, item, ind)


