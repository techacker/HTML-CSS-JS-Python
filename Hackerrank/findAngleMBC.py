import math

AB = int(input())
BC = int(input())
# Evaluate the hypotenuse
AC = math.hypot(AB,BC)
# Evaluate the angle MBC
angle = round(math.degrees(math.acos(BC/AC)))
# Chr(176) is unicode for degree
print(str(angle) + chr(176))
