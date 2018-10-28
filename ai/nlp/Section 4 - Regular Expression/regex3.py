# Introduction to Python Regular Expressions

# Importing Libraries
import re

pattern1 = "I love Avengers" #I love Justice League

print(re.sub(r"Avengers","Justice League",pattern1)) # sub does global search

pattern1 = "I love Avengers Avengers Avengers" #I love Justice League Justice League Justice League
print(re.sub(r"Avengers","Justice League",pattern1)) # sub does global search


print(re.sub(r"[a-z]","0", pattern1)) # caps not replaced
print(re.sub(r"[a-z]","0",pattern1,flags=re.I)) # all replaced
count = 2
print(re.sub(r"[a-z]","0", pattern1, count, flags=re.I)) # count no of elements got replaced