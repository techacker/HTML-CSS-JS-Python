# Day 10: Binary Numbers
# 
# Task
# Given a base-10 integer, n, convert it to binary(base-2). 
# Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

#****** The definition of "CONSECUTIVE 1's" is misinterpreted at the site.**********************

n = int(input())
binary = bin(n).split('b')[1]

count = 0
for i in range(len(binary)+1):
    if binary[i:i+2] == '11':
        count += 1

print(count)
