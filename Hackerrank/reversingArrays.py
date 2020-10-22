# Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

N = int(input())
#arr = input().split()
arr = list(map(int, input().rstrip().split()))

# Print the array in reverse using one of the following methods:

# 1. Using 'Array reversal with [::-1]
print(' '.join(map(str, arr[::-1])))

# 2. Using 'reverse' method
#arr.reverse()
#print(' '.join(map(str, arr[::])))

# 3. Using 'reversed() method
#result = list(reversed(arr))
#print(' '.join(map(str, result[::])))