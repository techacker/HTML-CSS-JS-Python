# Question 3
# Complete the function digits(n) that returns how many digits the number has. 
# For example: 25 has 2 digits and 144 has 3 digits. 
# Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.

def digits(n):
    count = 0
    if n == 0:
        return count+1
    while (n//10 >= 1):
        count += 1
        n = n//10
    return count+1
	
#print(digits(25))   # Should print 2
#print(digits(144))  # Should print 3
#print(digits(1000)) # Should print 4
#print(digits(0))    # Should print 1

# Question 4
# This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). 
# Fill in the blanks so that calling multiplication_table(1, 3) will print out:
# 1 2 3
# 2 4 6
# 3 6 9

def multiplication_table(start, stop):
	for x in range(1, stop+1):
		for y in range(1, stop+1):
			print(str(x*y), end=" ")
		print()

#multiplication_table(1, 3)
# Should print the multiplication table shown above

# Question 5
# The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.

def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x += 1
	return return_string

#print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
#print(counter(2, 1)) # Should be "Counting down: 2,1"
#print(counter(5, 5)) # Should be "Counting up: 5"

# Question 10
def votes(params):
	for vote in params:
	    print("Possible option:" + vote)

#votes(['yes', 'no', 'maybe'])