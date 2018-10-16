# Task#1 - Print odd number from 0 to 100
# Task#2 - Print even number from 0 to 100

print("Hello World")

print(4+5)

print(5 + 5)
print(5 - 5)
# 1
# 2
# 3
# 1.2
# "aMANDEEP"
# True False
company_name = "Royal Bank of Scotland, India"
employee_name = "Amandeep"

company_name = 1

employee_skills = ['Data Science', 'Python', 'Java']
employee_names = ['Amandeep', 'Anmol', 'Harsh']

print(company_name)

print(employee_names[0], "works in ", company_name)
print(employee_names[1], "works in ", company_name)
print(employee_names[2], "works in ", company_name)

ll = [1,2, "Aman", 2.0]

type(employee_name)
type(company_name)
type(employee_skills)
type(employee_names)
type(ll)

print(employee_skills)


b  = True
b and False

True  and False
True  and True
False and False
False and True

True  or False
True  or True
False or False
False or True

del employee_names[0]

import matplotlib.pyplot as plt
import numpy as np
from numpy import array,sum
x = array(range(-100,100))
sum(x)
y = x ** 2
plt.plot(x,y)
plt.show()

not True


a = 11
b = 11
c = 111
d = 11
if a<b:
    print("1")
elif c<b:
    print("2")
elif d<b:
    print("3")
else:
    print("4")
print("5")

#iterable
# 1. String
# 2. List
# 3. Tuple
# 4. Set
# 5. Dict
# 6. Iterator type of objects (range, filter, map)

print(range(10))
print(list(range(-10)))
print(list(range(-10, 10)))
print(list(range(0, 10, 2)))

# for & while
# For Loop Syntax
# for i in <iterable>:
#     print(i)

for s in "amandeep":
    print(s)

for s in employee_names:
    print(s)

for i in range(1,11):
    print(i)

is_process_completed = False
while not is_process_completed:
    # Do some processing and save the response in is_process_completed
    print("Still running!!")