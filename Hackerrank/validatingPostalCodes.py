import re

# 121426 # Here, 1 is an alternating repetitive digit.
# 523563  # Here, NO digit is an alternating repetitive digit.
# 552523  # Here, both 2 and 5 are alternating repetitive digits.

P = input()
regex_integer_in_range = r'[1-9][0-9]{5}$'

# Use Regex lookahead method:
# (?=foo) is a positive lookahead...use site like https://regex101.com/ to get more information.

regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'

# Print True or False if both conditions are satisfied.
print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair,P))<2)
