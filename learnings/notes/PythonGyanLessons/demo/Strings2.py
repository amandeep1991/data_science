# strr = "123"
#
# print("Aman", end='')
# print("Shiv")
# print("Shiv")
# print("Aman", end='')
# print("Shiv")
# print("Aman","Shiv","Aman","Shiv","Aman")
# print("Aman",1,"Aman","Shiv","Aman")
#
# print("Aman","Shiv","Aman","Shiv","Aman", sep=',')
# print("Aman","Shiv","Aman","Shiv","Aman", sep='.')
# print("Aman","Shiv","Aman","Shiv","Aman", sep='#')
#
#
# a,b = 10,20
# print(a,b)
# b,a = a,b
# print(a,b)
#
#
# # AmanShiv
# # Shiv
# # AmanShiv
#
#
# "Aman is a".isspace()
# " ".isspace()
# " \t".isspace()
# " \n".isspace()
# " \na".isspace()
# " \na".isalphanum()
# " \na".isalnum()
# " 1a".isalnum()
# "1a".isalnum()
# "1a".isalpha()
# "a".isalpha()
# "1".isalpha()
# "1".isdigit()
# "a1".isdigit()
# # and = 10
# # or = 10
# "1a".isidentifier()
# "_a".isidentifier()
# "_1a".isidentifier()
# "_1a".isidentifier()
# "@_1a".isidentifier()
# "abc".islower()
# "1abc".islower()
# "@1abc".islower()
# "@1abcD".islower()
# "@1abcD".isupper()
# "@1ABCD".isupper()
#
#
# s = "welcome to python"
# s.endswith("thon")
# s.startswith("good")
# s.find("come")
# s.find("become")
# s.rfind("o")
# s.count("ot")
#
# s = s.capitalize()
#
# s = "string in python"
#
# s1 = s.capitalize()
# s1
#
# s2 = s.title()
# s2
#
# s = "This Is Test"
# s3 = s.lower()
# s3
#
# s4 = s.upper()
# s4
#
# s5 = s.swapcase()
# s5
#
# s6 = s.replace("Is", "Was")
# s6
#
# def utility():
#     if strr.isdigit():
#         ii = int(strr)
#     elif strr.isspace():
#         ii = None
#     else:
#         ii = "DefaultValue"
#
#     return ii
#
# type(utility())
#
# b = "a b c"
# b = b.replace(" ", "#")
# b.replace(" ", "")
#
# b = "bbbbbbbbbbbbbbba b c dfd dvd ddd dvd"
# b = "bbc dfd dvd ddd dvd"
# index = b.find(" ")
# b[:index]+b[index+1:]
#
# import math
# math.ceil(1.11)
# math.floor(2.29856)
# math.copysign(1, -9)
# math.copysign(-1, 9)
# math.fabs(-9)
#
#
# index_for_first_space = b.index(" ")
# index_of_character_after_first_space = index_for_first_space+1
# b[:index_for_first_space] + b[index_of_character_after_first_space:]
#
#
#
# def validate_password(password):
#     if password.find("Vinod"):
#         return False
#     else:
#         return True
#
#
# validate_password("vinod") # why it is returning False (even when find is case-sensitive) ??
#
# print("HelloWorld")
#
# my_string = "Hello world!"
# print(my_string[3:7:2])
# my_string = "Hello world!"
# my_string[3:7:2]
# reversed(my_string)
# list(reversed(my_string))
# "".join(list(reversed(my_string)))
# "$".join(list(reversed(my_string)))
# list(reversed(my_string))
# print(1,2,3,4)
# print(1,2,3,4, sep="")
# print(list(reversed(my_string)), sep="")
# "Aman is not a good boy but Shiv is".split(' ')
# "Aman is not a good boy. Shiv is very good boy.".split('.')
# "Aman is not a good boy. Shiv is very good boy.".split('.')
# "Aman is not a good boy. Shiv is very good boy.".split('.')
# all_sentences = "Aman is not a good boy. Shiv is very good boy."
# all_sentences.split('.')
# len(all_sentences.split('.'))
# all_sentences = "Aman is not a good boy. Shiv is very good boy."
# len(all_sentences.split('.'))
# all_sentences.split('.')
# all_sentences.split('. ')
# all_sentences.split('.')
# all_sentences
# all_sentences.split('. ')
#
# my_paragraph = "Aman is not a good boy.Shiv is very good boy. But Shiv doesn't study hard. Ideally he should study as well, being good is not enough. God, please give him some motivation to study"
#
# ll = []
# ll.append("Aman is not a good boy.")
# ll.append("Shiv is very good boy.")
# ll.append("But Shiv doesn't study hard.")
# ll.append("Ideally he should study as well, being good is not enough.")
# ll.append("God, please give him some motivation to study.")


my_list = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,2,1,1,1,1,1,1,1,1,3]
for index, element in enumerate(my_list):
    # print(index, element)
    if element==1:
        # print("###",index, element)
        # del my_list[index]
        my_list.remove(element)

while 1 in my_list: my_list.remove(1)
print(my_list)

my_list = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,2,1,1,1,1,1,1,1,1,3]
[i for i in my_list if i!=1]

my_list = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,2,1,1,1,1,1,1,1,1,3]
list(filter(lambda x:x!=1, my_list))


def venkat(var1):
    return var1**2

def venkat_true_or_false(var1):
    return None

print(list(map(venkat, [1,2,3,4,5])))
print(list(filter(venkat_true_or_false, [1,2,3,4,5])))

ff = float("3.5")+7.8
ff

print(float("3.500"))
print(float(3))
print(float("3.501"))

v = input("Enter your name")
print("Welcome", v, "!")

list1 = ["apple1", "banana1", "cherry1"]
# iter1 = iter(list1)
list2 = ["apple2", "banana2", "cherry2"]
iter2 = iter(list2)


for i in list1:
    print(i, '-', next(iter2))

for i,j in zip(list1, list2):
    print(i, '-', j)

for i in range(len(list1)):
    print(list1[i], '-', list2[i])


for i in zip([1,2,3,4],[1,2,3,4],['Aman','Sahil','Rajat','Shiv']):
    print(i)
    print(type(i))

