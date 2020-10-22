# Introduction to Sets
# A set is an unordered collection of elements without duplicate entries.
# When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

'''
print(set())
# returns set()
print(set('ANURAG'))
# returns {'R', 'N', 'A', 'G', 'U'}
print(set([1,2,3,4,3,2,1,2,3,2,1]))
# returns {1, 2, 3, 4}
print(set(set(['A','N','U','R','A','G','B','A','N','S','A','L'])))
# returns {'L', 'S', 'B', 'R', 'N', 'A', 'G', 'U'}
print(set({'Name': 'Anurag','Profession': 'Engineer'}))
# returns {'Profession', 'Name'}
print(set(enumerate(['H','a','c','k','e','r','r','a','n','k'])))
# returns {(3, 'k'), (4, 'e'), (5, 'r'), (6, 'r'), (7, 'a'), (8, 'n'), (9, 'k'), (0, 'H'), (1, 'a'), (2, 'c')}
'''

# Task
# Now, let's use our knowledge of sets and help Mickey.
# Ms. Gabriel Williams is a botany professor at District College. 
# One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

def average(array):
    heights = set(array)
    count = len(heights)
    average = sum(heights) / count
    return average


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
