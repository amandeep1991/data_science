# https://docs.python.org/3.1/library/re.html

import re

# '|' is equivalent to OR
# we put r in front of a string, it is called a raw string which means we can include
# the special characters like backslash without clashing the default python string behaviour
print(re.search(r"(hello|india|what)", "hello world").group(0))

print(re.search("(hi)", "which").group(0))
print(re.search("(hi)", "which") is None)

# \b matches the beginning or end of a word
print(re.search("\b(hi)\b", "which") is None)

# If we are going to use a pattern multiple times, we can create a pattern object using re.compile method
# square bracket indicates a range of characters
# * means 0 or more occurrence of this pattern
# {1} exactly one occurrence of the pattern
pattern = re.compile('[A-Z]{1}[a-z]*')

message = '''
Amandeep from India is a very good boy
He love to explore Machine Learning use-cases'''
# findall method returns all the matching substrings:
print(pattern.findall(message))