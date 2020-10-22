'''
# Day 20: Bubble Sorting Algorithm
Given an array, 'a', of size 'n' distinct elements, sort the array in ascending order using the Bubble Sort algorithm. 
Once sorted, print the following 3 lines:
Array is sorted in numSwaps swaps.
where 'numSwaps' is the number of swaps that took place.
First Element: firstElement
where 'firstElement' is the first element in the sorted array.
Last Element: lastElement
where 'lastElement' is the last element in the sorted array.
'''

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

tmp = 0
numSwaps = 0
unsorted = True

while unsorted:
    for i in range(n - 1):
        if a[i] > a[i+1]:
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp
            numSwaps += 1
            break
        if i == n-2:
            unsorted = False

print(f'Array is sorted in {numSwaps} swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])
