### Write a program that calculates the proportion of students who received grade A.
#A five-point rating system with grades A, B, C, D, F is used.
#
#Input format:
#A string with students' marks separated by space. At least one mark will be present.
#
#Output format:
#A fractional number with exactly two decimal places.
#
#To format the decimal places use the round(number, places) function.

grades = input().split()

count = 0
print(grades)
for i in range(len(grades)):
    if grades[i] == 'A':
        count += 1

try:
    rating = count / len(grades)
except ZeroDivisionError:
    rating = 0

print(round(rating, 2))
