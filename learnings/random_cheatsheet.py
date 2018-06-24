import random
import numpy as np

## Generate random numbers list [integer] - unique
numLow = 10
numHigh = 90
random.sample(range(1, 100), 3)
data = range(numLow, numHigh)
random.shuffle(data)

## Generate random numbers list [integer] – duplicates allowed – choice with replace=True
np.random.choice(10, 10, replace=True)
np.random.choice(10, 100, replace=False)
[random.choice(range(10)) for i in range(10)]

# Generate integers between any two given number
print([random.randint(1,1001) for x in range(10)])
# randrange(beg, end, step) # step (to skip numbers in range while selecting) but still not sure
random.randrange(20, 50, 3)

# Generate float between any two given number
random.uniform(1.0, 9.9)
random.uniform(1, 9)

#Generate float number between 0 and 1
random.random()

# Attach a random object a particular seed value
random.seed(7)
first_random_value = random.random()
random.seed(7)
second_random_value = random.random()
"True" if first_random_value == second_random_value else "False"


# generate 1 random number from a container
random.choice([1,2,3,4,5,6])
random.choice((1,2,3,4,5,6))
# Not work for set [TypeError: 'set' object does not support indexing]
# random.choice({1,2,3,4,5,6})
random.choice({1:"Value_1",2:"Value_2",3:"Value_3",4:"Value_4",5:"Value_5"}) # returning value
# Throwing error
string_keyed_dictionaries = {"Key_1":"Value_1","Key_2":"Value_2","Key_3":"Value_3","Key_4":"Value_4","Key_5":"Value_5"}
#random.choice(string_keyed_dictionaries)
random.choice(string_keyed_dictionaries.keys())
random.choice(list(string_keyed_dictionaries.keys()))
# random.choice(string_keyed_dictionaries.items()) # dict_items object doesn't support indexing
random.choice(list(string_keyed_dictionaries.items()))


#Shuffle the entire list in random order
ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(ordered_list)
print(ordered_list)