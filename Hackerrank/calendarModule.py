# Task
# You are given a date. Your task is to find what the day is on that date.
# Input Format
# A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

import calendar


s = input().split()
m = int(s[0])
d = int(s[1])
y = int(s[2])

day = calendar.weekday(y,m,d)

weekday = calendar.day_name.__getitem__(day)

print(weekday.upper())
