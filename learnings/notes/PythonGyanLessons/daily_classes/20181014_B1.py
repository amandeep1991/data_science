list_of_integers = [1, 2, 3, 4, 5 ]


list_of_strings = ["a1", "b2", "c3", "d4"]


different_data_types_are_supported = ['Python', 'Machine Learning', 8000, 18000]

different_data_types_are_supported[3] = 19000

# Will throw error
# different_data_types_are_supported[5] = 19000

del different_data_types_are_supported[1]
different_data_types_are_supported

for i in different_data_types_are_supported:
    print(i)

print(different_data_types_are_supported)

max(different_data_types_are_supported)

dd = []
dd = list()

tt = (1,2,3)
type(tt)

ll = list(tt)
type(ll)

ll
different_data_types_are_supported.append(ll)

different_data_types_are_supported = ['Python', 'Machine Learning', 8000, 18000]

different_data_types_are_supported.extend(ll)

different_data_types_are_supported + ll

ll.extend(ll)

ll.append(1)
ll.count(1)

ll.index(2)

ll
ll.insert(0,2)

ll.pop()

ll.remove(1)
ll

ll.reverse()

different_data_types_are_supported.sort()
ll.sort()
ll


my_tuple = ('Vinod', 'Sahil')
print(my_tuple)

del my_tuple

print("After deleting my_tuple : ")
print(my_tuple)

tuple(ll)


dict1 = {'Name': 'Shiv', 'Age': 20, 'Class': 'First'}
dict1

dict1['Name']

dict1['City'] = 'India'

dict1.get('Name ','Aman')
dict1.get('Address1','Gurgaon')

dict1.get('Name','Sahil')

dict1.setdefault('Address2', 'Gurugram') #It adds as well if not present
dict1.setdefault('Address2', 'Gurugram') #It adds as well if not present
dict1.setdefault('Name', 'Vinod')

dict1['City'] = 'India1'
dict1['City'] = 'India2'
dict1['City'] = 'India3'
dict1['City'] = 'India4'
dict1['City'] = 'India5'

del dict1['Name']

ddd = {}

type(ddd)

ddd[(1,2,3)]='a'
ddd[[1,2,3]]='b'


ll = ['property1']

for i in range(2,100):
    ll.append('property'+str(i))

ddd['property1']


ddd = ddd.fromkeys(ll, None)
ddd.keys()
ddd.values()
ddd.items()


dict1 = {1: 99999,     2: 2, 3: 2, 4: 12345}
dict2 = {1: 888888888, 2: 2, 3: 2}
dict1.update(dict2) # also add keys from dict2 which are not present in dict1








ll = [['First','second','third','fourth','fifth'],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
print(ll)
import pprint
pprint.pprint(ll)















import pandas as pd
import os
os.getcwd()
os.chdir("F:\\StudyMaterial\\Efforts\\technical\\Machine Learning\\pyCharmWorkspace\\data_science\\zdata")
df = pd.read_csv('All.csv')
df
df.columns
df.index

df.iloc[1,:]
df.iloc[:,0]

df.loc[:, 'StatusDate']


