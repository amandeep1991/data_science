# Notice the r before the string. Since the slashes are special characters, prefixing the string with a r will escape the whole string.

import string

Location = r'C:\Users\david\notebooks\update\births1880.txt'

string.ascii_letters
string.ascii_lowercase
string.ascii_uppercase
string.digits
string.hexdigits
string.punctuation
string.printable
string.octdigits
string.capwords("my name is aman-deep")  #'My Name Is Aman-deep'
string.capwords("my name is aman-deep", sep='-')  #'My name is aman-Deep'
string.capwords("my name is aman.sdkjfkd djfkjd ") # 'My Name Is Aman.sdkjfkd Djfkjd' [as default value of sep is None]
string.capwords("my name is aman.sdkjfkd djfkjd ", sep=' ') # 'My Name Is Aman.sdkjfkd Djfkjd '
string.capwords("my name is aman", sep='\n') # 'My name is aman'

