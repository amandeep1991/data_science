# Introduction to Python Regular Expressions

# Importing the libraries
import re

sentence1 = "Welcome to the year 2018"
sentence2 = "Just ~%* ++++--- arrived at @Jack's place. #fun"
sentence3 = "I                  love                u"

sentence1_modified = re.sub(r'\d','',sentence1) # Removed all digits

sentence2_modified = re.sub(r'[@#\.\']','',sentence2) # [] used to group different characters [. here is full stop & not any character]

sentence2_modified = re.sub(r'\w',' ',sentence2) # w - selects characters
sentence2_modified = re.sub(r'\W',' ',sentence2) # W - opposite of w

sentence2_modified = re.sub(r'\s+',' ',sentence2_modified) # s - single space

sentence2_modified = re.sub(r"\s+[a-zA-Z]\s+",' ',sentence2_modified) # single character don't mean anything (like Jack's)

sentence3_modified = re.sub(r'\s+',' ',sentence3)


