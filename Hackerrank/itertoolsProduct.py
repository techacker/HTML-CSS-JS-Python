from itertools import product

# If we imported itertools directly, the following commented lines will work.
#import itertools

#print(list(itertools.product([1,2,3],repeat = 2)))
#print(list(itertools.product([1, 2, 3],[3,4])))
#A = [[1,2,3],[3,4,5]]
#B = [[1,2,3],[3,4,5],[7,8]]
#print(list(itertools.product(*A)))
#print(list(itertools.product(*B)))

#C = [1,2]
#D = [3,4]
#print(list(itertools.product(C,D)))


E = list(map(int, input().split()))
F = list(map(int, input().split()))

# Since we imported product from itertools, we can use product directly
G = list(product(E, F))
# Using * before a list name, it print the list values in a single line.
print(*G)
