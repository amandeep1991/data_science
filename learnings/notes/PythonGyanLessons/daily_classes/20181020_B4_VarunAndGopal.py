# NEXT (Gopal, Varun): Strings
# NEXT (Anmol, ): callable

# Task #1: Create a calculator supporting +,-,/,* and ** operators from command line (Command Line Arguments).
# Command
# python calculator.py 2 + 3
# # output on console
# 2+3=5
#
# # Command
# python calculator.py 2 ** 3
# # output on console
# 2**3=8
#


a = 10


def x(input):
    print("dkfjdkfjdkjdkfdjfkdjfkdj")
    if input > 5:
        return False
    return True


print(callable(x))
print(callable(a))


# a()

def call_callable(abdjkjfkd, i):
    return abdjkjfkd(i)


def call_callable(abdjkjfkd, i):
    if not callable(abdjkjfkd):
        print('Make sure your 1st parameter is a function')
    else:
        return abdjkjfkd(i)


print(call_callable(a, 7))
print(call_callable(x, 7))
print(x(7))

chr(97)
chr(65)

ord('a')

"aman" > "BBBBBBBBBBBBBBBBBBBBBBB"

my_dict = dict(name="Sahil", age=26, country="India")
print(list(my_dict))
print(list(my_dict.items()))

list(1)

ll = list(range(100, 111))

ll[0] = 99999

tt = tuple(ll)
tt[0] = 100

list(enumerate(ll))

for ddddd, value in enumerate(ll):
    print(ddddd, " : ", value)

a, b, c, d = (1, 2, 3, 4)

ord('A') < ord("B")

ss = "Amandeep"
ss[1:4]
ss[0:4]
ss[:4]
ss[4:8]
ss[4:]
ss = "Amandeep is a good boy"
ss[4:]
ss[4:8]

int('a')
ord('a')

ages = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


adults = filter(myFunc, ages)
for x in adults:
    print(x)

ii = iter(adults)
next(ii)

max(1, 2, 3)
max(1, 2, 3, "A", 'a', "B", "b")
max("A", 'a', "B", "b")
min("A", 'a', "B", "b")

print(min("Amandeep", "Sahil", "Rajat"))

print(pow(4, 3, 5))
(5*64)/100

print("Amandeep","Amandeep","Amandeep","Amandeep","Amandeep","Amandeep", sep='', end='#')
print("Amandeep","Amandeep","Amandeep","Amandeep","Amandeep","Amandeep", sep='', end='#')
print("Amandeep","Amandeep","Amandeep","Amandeep","Amandeep","Amandeep", sep='', end='#')
print('Hello')

type(1)

student_id = [1, 2, 3, 4]
names = ['Aman', 'Sahil', 'Rajat']
address = ['Gurgaon', 'Faridabad', 'NOida', 'Delhi']
list(zip(student_id, names, address))

list(zip(student_id, names, address, "123456"))

list(zip([1,2,3,4],['Aman'],'Sahil','Rajat','Shiv'))