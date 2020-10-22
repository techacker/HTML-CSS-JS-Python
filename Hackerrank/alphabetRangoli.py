# You are given an integer, N. 
# Your task is to print an alphabet rangoli of size N. 
# (Rangoli is a form of Indian folk art based on creation of patterns.)
#
# Example : size 5
#
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

import string
# To be able to quickly create a list of alphabets.

# Function that actually creates the design.
def print_rangoli(size):
    alpha = string.ascii_lowercase
    printList = []

    for i in range(size):
        tmp = '-'.join(alpha[i:size])
        printList.append((tmp[::-1] + tmp[1:]).center(4*size - 3, '-'))
    print('\n'.join(printList[:0:-1] + printList))


n = int(input())
print_rangoli(n)
