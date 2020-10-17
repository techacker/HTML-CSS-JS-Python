# Question 3
def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n != 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False


#print(is_power_of_two(0))
#print(is_power_of_two(1))
#print(is_power_of_two(8))
#print(is_power_of_two(9))

# Question 4
def sum_divisors(n):
    sum = 0
    i = 1
    # Return the sum of all divisors of n, not including n
    while i < n:
        if n % i == 0:
            sum += i
        i += 1
    return sum

#print(sum_divisors(0))
#print(sum_divisors(3)) # Should sum of 1
#print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
#print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51

#Question 5
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = multiplier * number
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

#multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
#multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
#multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24