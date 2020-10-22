from itertools import permutations

# Examples of itertools.permutations method
#print(permutations([1,2,3]))
#rint(list(permutations([1, 2, 3])))
#print(list(permutations([1, 2, 3],2)))
#print(list(permutations('abc',3)))

# Task
# You are given a string S.
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

S, k = input().split()
combs = list(permutations(sorted(S),int(k)))

for i in range(len(combs)):
    print(''.join(combs[i]))
