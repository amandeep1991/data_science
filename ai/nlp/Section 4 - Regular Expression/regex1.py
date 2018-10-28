# Introduction to Python Regular Expressions

# Importing Libraries
import re

pattern1 = "abcd"
pattern1 = "9876 efg 98"
pattern1 = "a"

print("Occurences of any character: ",re.match(r".+",pattern1))
print("Occurences of A_Za-z: ",re.search(r"[a-z]+",pattern1))
print("Occurences of ab*: ",re.search(r"ab?",pattern1))

if re.match(r"[a-z]+",pattern1) != None:
    print("Match!")
else:
    print("No Match!")

sentence = "I was born in the year 1991"
re.sub(r"\d","", sentence) # substitute digit by empty string ""

sentence += "18 89"
re.sub(r"\d","#", sentence)

re.match(r".*", sentence) # match the complete  sentence
re.match(r"\d", sentence) # Returns None means no match
re.match(r"\d*", sentence) # return match with empty string
re.match(r"\d+", sentence) # Returns None
re.match(r"[a-zA-Z]+", sentence) # Match 'I' because this is first occurence matching pattern (space not included)

pattern = r"ab?" # b is 0 or 1 prefixed by a
sentence = "a"
re.match(pattern, sentence)


sentence = "1991 was the year when I was born"
re.match(r"[a-zA-Z]+", sentence) # None as it starts with the first character

# Better solution is search
re.search(r"[a-zA-Z]+", sentence) # Search - global search

# start (^) (match)
re.match(r"^1991", sentence)

# ends with ($) (search)
re.search(r"born$", sentence)
