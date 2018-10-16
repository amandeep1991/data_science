
def my_function(x):
    if x>10:
        return True
    else:
        return False

def reverse_of_my_function(x):
    return not my_function(x)

x = 10
callable(reverse_of_my_function)
callable(x)

list(filter(reverse_of_my_function, [10,20,9,30]))

max(filter(reverse_of_my_function, [10,20,9,30]))
min(filter(reverse_of_my_function, [10,20,9,30]))

ord("A")
chr(97)

10**2
pow(10,2)

for i in filter(reverse_of_my_function, [10,20,9,30]):
    print(i)


list(map(my_function, [10,20,9,30]))


def find_length(args):
    return len(args)

import os
os.getcwd()

print("123", file=open("abc.txt", "a"))

list(map(find_length, ["Venkat", "Amandeep", "sahil"]))

iter_v = iter(["Amandeep", "Sahil", "Venkat"])
next(iter_v)

for i in iter_v:
    print(i)

counter = 0
iter_v = iter(["Amandeep", "Sahil", "Venkat"])
while counter<4:
    counter+=1
    print(next(iter_v))

list(range(1,20,2))



tt = (1,2,3,4)
tt = list(tt)
tt[1]=9

my_string = "Amamdeep"
# my_string[3]='n'

def replace_character(my_string, index, new_character):
    return my_string[:index] + new_character + my_string[(index + 1):]

replace_character(my_string, 3, 'n')


my_line = "Sahil is a very intelligent boy"

def replace_word_in_line(line, index_of_word_to_be_replaced, new_word):
    word_arr = line.split(" ")
    word_arr[index_of_word_to_be_replaced] = new_word
    return " ".join(word_arr)

replace_word_in_line(my_line, 5, "man")


my_concatenated_string = ""
word_arr = my_line.split(" ")
word_arr[5] = "man"
for i in word_arr:
    my_concatenated_string += i + ' '


"Aman"+"deep"
"Aman"*"deep"
"Aman"+3
"Aman"*3

my_name = "Amandeep"
my_string = my_name
my_string[1:4]

"intelligent" in my_line

"intelligent1" not in my_line

"a">"1"
print(ord("a"))
print(ord("1"))

print("a"!="1", end="")
print("a"> "1", end="")
print("a"< "1", end="")
print("a"<="1", end="")
print("a"<="1", end="")
print("a"=="1", end="")
print("a"!="1", end="")

print("a"!="1", end="\n")
print("a"> "1", end="\n")
print("a"< "1", end="\n")
print("a"<="1", end="\n")
print("a"<="1", end="\n")
print("a"=="1", end="\n")
print("a"!="1", end="\n")

print("aman"+"deep")
print("Aman"+1)
print("Aman" + str(1))

print("Aman",1)
print("Aman",1, sep="")
print("Aman",1, sep="#")

print("a"!="1", "a"> "1", "a"< "1", "a"<="1", "a"<="1", "a"=="1", "a"!="1", sep="-")

print("a"!="1", "a"> "1", "a"< "1", "a"<="1", "a"<="1", "a"=="1", "a"!="1", sep="\n")

for word in word_arr:
    print(word, end="-")

len(my_name)
max(my_name)


# my_name = "12_AM_123"
my_name = " "

my_name.isalnum()
my_name.isalpha()
my_name.isdigit()
my_name.isidentifier()
my_name.islower()
my_name.isupper()
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




my_line = "sahil is A very very very good boy"
my_line.capitalize()
my_line.lower()
my_line.upper()
my_line.title()
my_line.swapcase()
my_line.replace("very", "good")

df = -3


from math import *

x = 10.5
x1 = 5
y = -11
ceil(x)
copysign(x, y)

fabs(y)

factorial(x1)

floor(x)

my_number = 1234
expected_number = 4321 #%

100/6
fmod(100, 6) # 100%6
16*6

m,e = frexp(2.718281828459) # Pending

m*2**e

fsum([1,2,3,4,5,6,7,8,9])

