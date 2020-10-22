import cmath
# Python's cmath module provides access to the mathematical functions for complex numbers.
# print(cmath.phase(-1.0))
# print(cmath.phase(complex(-1.0,0.0)))
# print(cmath.phase(abs(complex(-1.0, 0.0))))
# print(cmath.sqrt(16))
# print(abs(-1.0))

'''
Task:
You are given a complex z. Your task is to convert it to polar coordinates.
'''

z = complex(input())
print(f'{abs(z):.3f}')
print(f'{cmath.phase(z):.3f}')
