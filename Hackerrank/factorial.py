# Write a factorial function that takes a positive integer, N as a parameter and prints the result N! of (N factorial).
# An example of recursive call on a function itself.

N = int(input())

def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n-1)
    return result 

print(factorial(N))
