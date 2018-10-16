dict1 = {'Name': 'Shiv', 'Age': 20, 'Class': 'First'}

dict1

dict1['Name']
del dict1['Name']

dict1['Name']
dict1.get('Name', "Shiv Saxena")

dict1['Age'] = 20.2

dict1

dict1["Name"] = "Shiv Kumar"

dict1

del dict1['Name'] # remove entry with key 'Name'
dict1
dict1.clear()     # remove all entries in dict
dict1
del dict1        # delete entire dictionary
dict1

sett = {} #wrong, it will create empty dictionary
sett = set() #create empty dictionary
sett = {1,2,3}
type(sett)
dict1 = {1:2,2:2,3:2}
type(dict1)

str(dict1)
dict1
dict2 = dict1
dict2[1]=99999
dict1[1]
dict2 = dict1.copy()
dict2[1]=99999
dict2[1]=888888888
dict1[1]

# import pprint
# pprint.pprint(dict.fromkeys(list(range(1,100)),list(range(1,100))))

dict.fromkeys(list(range(1,100)),list(range(1,100))) #not expected (each value is a list of 100 elements)
dict.fromkeys(list(range(1,100)),0) # initialize with default values

list(dict1.keys())
1 in dict1.keys()

list(dict1.items())

dict1.setdefault(4, 12345) # Insert as well if not found value in map, if found simply return original value no update will be there
dict1

dict1.setdefault(4, 99999) # Add value in map

dict1.get(5, 12345) #Doesn't add value in map
dict1


dict1 = {1: 99999,     2: 2, 3: 2, 4: 12345}
dict2 = {1: 888888888, 2: 2, 3: 2}
dict1.update(dict2) # also add keys from dict2 which are not present in dict1
dict1 #{1: 888888888, 2: 2, 3: 2, 4: 12345}

dict1 = {1: 99999,     2: 2, 3: 2, 4: 12345}
dict2 = {1: 888888888, 2: 2, 3: 2, 5:7777777777}
dict1.update(dict2)
dict1 #{1: 888888888, 2: 2, 3: 2, 4: 12345}

list(dict1.values())


# Creating a set
days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
# days=(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
# days=(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],)
# type(days)
months={"Jan","Feb","Mar"}
dates={21,22,17}
print(days)
print(months)
print(dates)

# Accessing Values in a Set
for d in days:
    print(d)

#Adding Items to a Set
Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
Days.add("Sun")
print(Days)

# Removing Item from a Set
Days.discard("Sun")
print(Days)

# Union of Sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)


# Intersection of Sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays)


# Difference of Sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB
print(AllDays)

# Compare Sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)


