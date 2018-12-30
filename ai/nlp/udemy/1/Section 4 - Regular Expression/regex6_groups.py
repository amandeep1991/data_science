
import re


# Regex Groups using or '|'
###### OR is represented by |
###### You can a group using ()
###### explicit character range using []

# Few patters
r"[A-Za-z]+" # upper or lowercase English alphabet
r"[0-9]" # numbers from 0 to 9
r"[A-Za-z\-\.]+" # upper or lower case English alphabets with - or .
r"(a-z)" # a,- & z
s_c = r"(\s+|,)" # spaces or commas

sentence = ","
re.search(s_c, sentence)