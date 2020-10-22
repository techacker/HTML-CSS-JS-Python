from collections import Counter
'''
Task
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay x amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.

Input Format

The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the 'shoe size' desired by the customer and x, the price of the shoe.

'''

# collections.Counter()
# A counter is a container that stores elements as dictionary keys, 
# and their counts are stored as dictionary values.

#myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
#print(Counter(myList))
#print(Counter(myList).items())
#print(Counter(myList).keys())
#print(Counter(myList).values())


X = int(input())        # X is number of shoes

shoes = Counter(map(int, input().split()))
# itertools.Counter() helps capture the input as a dictionary with shoe size and its asking price.

N = int(input())        # N is number of customers
money = 0

# Since 'shoes' is already a dictionary, it is easy to cycle through it.
for _ in range(N):
    size, price = map(int, input().split())
    if shoes[size]:
        money += price
        shoes[size] -= 1
        # DEBUG: print(shoes)

print(money)

