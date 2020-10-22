from itertools import combinations

S, k = input().split()
letters = []
for i in range(1, int(k) + 1):
    letters += list(combinations(sorted(S),i))

for _ in range(len(letters)):
    print(''.join(letters[_]))
