extreme = {'a': 43, 'b': 1233, 'c': 8, 'd': 1, 'e': 100, 'f': 3400}

minimum = min(extreme.values())
maximum = max(extreme.values())
for key, value in extreme.items():
    if value == minimum:
        minkey = key
    if value == maximum:
        maxkey = key


print('min:', minkey)
print('max:', maxkey)

