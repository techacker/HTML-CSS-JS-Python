# Given a 6 X 6 2D Array, A:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in to be a subset of values with indices falling in this pattern in 's graphical representation:
# a b c
#  d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
# Task
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

import math
arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

C = []

for i in range(4):
    for j in range(4):
        total = sum(arr[i][j:j+3]) + int(arr[i+1][j+1]) + sum(arr[i+2][j:j+3])
        C.append(total)

print(max(C))
