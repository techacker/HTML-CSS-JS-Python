def skip_elements(elements):
	# Initialize variables
    new_list = []
	# Iterate through the list

    for i in range(0, len(elements), 2):
        #print(elements[i])
        # Does this element belong in the resulting list?
        if elements[i] not in new_list:
            new_list.append(elements[i])
			# Add this element to the resulting list
    
    return new_list

#print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
#print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
#print(skip_elements([])) # Should be []

# Using enumerate method to iterate over list
def skipping_elements(elements):
    new_list = []
    for i, element in enumerate(elements):
        if i % 2 == 0:
            new_list.append(element)
    return new_list

#print(skipping_elements(["a", "b", "c", "d", "e", "f", "g"]))
#print(skipping_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']