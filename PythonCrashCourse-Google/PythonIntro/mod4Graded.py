# Question 1
# The format_address function separates out parts of the address string into new strings: 
# house_number and street_name, and returns: "house number X on street named Y". 
# The format of the input string is: numeric house number, followed by the street name which may contain numbers, 
# but never by themselves, and could be several words long. 
# For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

def format_address(address_string):
    # Declare variables
    house_number = ""
    street_name = ""
    # Separate the address string into parts
    address_parts = address_string.split(" ")
    # Traverse through the address parts
    for i in range(len(address_parts)):
        if address_parts[i].isdigit():
            house_number = address_parts[i]
        else:
            street_name += address_parts[i] + " "

    return "house number {} on street named {}".format(str(house_number), street_name.rstrip())

print("Question 1:")
print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
print()

# Question 2
# The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
# Can you write this function in just one line?

def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper()))

print("Question 2:")
print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
print()

# Question 3
# A professor with two assistants, Jamie and Drew, wants an attendance list of the students, 
# in the order that they arrived in the classroom. Drew was the first one to note which students arrived, 
# and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, 
# who needs to combine them into one, in the order of each student's arrival. 
# Jamie emailed a follow-up, saying that her list is in reverse order. 
# Complete the steps to combine them into one list as follows: the contents of Drew's list, 
# followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
    list1.reverse()
    return list2 + list1


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print("Question 3:")
print(combine_lists(Jamies_list, Drews_list))
print()

# Question 6
# Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, 
# with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, 
# but Rory's list has more current information about the number of guests. Fill in the blanks to combine both dictionaries into one, 
# with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, 
# if a name is included in both dictionaries. Then print the resulting dictionary.

def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed only once, and the value from guests1 taking precedence
    #guests1.update(guests2)
    guests2.update(guests1)
    return guests2


Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print("Question 6:")
print(combine_guests(Rorys_guests, Taylors_guests))
print()

# Question 7
# Use a dictionary to count the frequency of letters in the input string. 
# Only letters should be counted, not blank spaces, numbers, or punctuation. 
# Upper case should be considered the same as lower case. 
# For example, count_letters("This is a sentence.") should 
# return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letters(text):
    result = {}
    # Go through each letter in the text
    for letter in text:
        # Check if the letter needs to be counted or not
        if letter not in result.keys():
            if letter.isalpha():
                letter = letter.lower()
                result[letter] = 1
        else:
            result[letter] += 1
    return result
        # Add or increment the value in the dictionary
        #else:
        #    result[letter] = letter
        #return result
        
print("Question 7:")
print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
print()


# Question 8
animal = "Hippopotamus"
print("Question 8:")
print(animal[3:6])
print(animal[-5])
print(animal[10:])
print()

#Question 9
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print("Question 9:")
print(colors)
print()

# Question 10
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print("Question 10:")
print(host_addresses.keys())
