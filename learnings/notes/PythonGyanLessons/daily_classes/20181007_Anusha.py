# Task #1:
# Make a function which would take three inputs, one is line and 2nd is word to be replaced and 3rd would be word which should be used to replace the given word (just replace 1st occurrence)
# Input Example:
#       my_line = "My name is 'Amandeep'! "
#       word_to_be_replaced = "Amandeep"
#       word_used_to_replace_given_word = "Anusha"

# Hints:
def function_name(parameter_1, parameter_2, parameter_3):
    # logic
    print("Output...")

def concatenation_sample(x,y):
    '''
    dfkjdfkdjfdk
    :param x: djfkdjfkdj
    :param y: djfdkfjd
    :return:
    '''
    print(x+y)

concatenation_sample("A","B")


my_line = "My name is 'Amandeep'! "

my_line = 'My name is "Amandeep"! '

my_line = str('My name is "Amandeep"! ')

str(1)
str(1.0)

my_line[0]
my_line[0]='K'

my_line = my_line[:12] + 'Anusha' + my_line[20:]

my_str = "0123456789"
my_str[8:]

str1 = "welcome"
str2 = "welcome"
id(str1) == id(str2) #immutability can be tested by id function

str1 = "welcome"
str2 = "Welcome"
id(str1) == id(str2)

id(1)

"Aman"+"deep"
"Aman"*"deep" #Error
"Aman"+3 #Error
"Aman"*3

my_str = "0123456789"
my_str[9:]
my_str[len(my_str)-1:]
my_str[-1]
my_str[4:7]


"Amandeep" not in my_line
"Amandeep" in my_line

ord('a')
ord('A')
chr(97)

print("a"!="1", end="")
print("a"> "1", end="")
print("a"< "1", end="")
print("a"<="1", end="")
print("a"<="1", end="")
print("a"=="1", end="")
print("a"!="1", end="")

s = "hello"
for i in s:
    print(i, end="")

print(s)

my_name = "AM_123"
my_name = "AM123"
my_name = "AM"
my_name.isalnum()

my_name = "12_AM_123"
my_name = "AM"
my_name.isalpha()
my_name = "12123"
my_name.isdigit()

my_name = "12_AM_123"
my_name = "_AM_123"
my_name = "AM_123"
my_name.isidentifier()

"str".isidentifier()
"and".isidentifier()
"len".isidentifier()

# and = 1
# len = 1
# str = 1

my_name = "am_123"
my_name.islower()

my_name = "AM_123"
my_name.isupper()

my_name = " "
my_name.isspace()

my_line = "Sahil is a very very very good boy"
s1 = "boy"
s2 = "Sahil"
s3 = "very"
s4 = "very"
s5 = "very"
my_line.endswith(s1)
my_line.startswith(s2)
my_line.count(s3)
my_line.find(s4)
my_line[11:]
my_line.rfind(s5)
my_line[21:]

