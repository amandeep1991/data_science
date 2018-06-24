import datetime
import random
import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print(sys.version)
print(pd.__version__)
print(matplotlib.__version__)


def generate_dates_using_date_time():
    global dummy_dates_pd
    start_date = datetime.datetime(1990, 1, 1)
    end_date = datetime.datetime(2018, 12, 31, 0, 0, 0)
    step = datetime.timedelta(hours=24)
    dummy_dates = []
    while start_date < end_date:  dummy_dates.append(start_date.strftime('%Y-%m-%d %H:%M:%S')); start_date += step;
    random.seed(278)
    return list(map(lambda x: x[:-9], dummy_dates))


#### Creating Data (using Zip and List)
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names, births, names)) # list of tuples (each tuple have 3 elements and above one has 2 elements)
BabyDataSet = list(zip(names, births))
df = pd.DataFrame(data=BabyDataSet, columns = ['Names', 'Births'])
df = pd.DataFrame(data=BabyDataSet, columns = ['Names', 'Births'], index=['A', 'B', 'C', 'D', 'E' ])
df.to_csv('springfactories.csv', index=False, header = False) #write to csv
pd.read_csv('springfactories.csv', index_col=0) # read from csv mentioning that first column is index
pd.read_csv('springfactories.csv', header=None, index_col=False) #read from csv without header and index column

#types of columns in dataframe
df.dtypes
df.Names.dtypes
df.Births.dtypes

# Ascending (expand the column selection automatically while sorting)
df.sort_values(['Names'])
df.sort_values(['Births'], ascending=False) # Descending

# Add new column
df['Numbers2'] = pd.Series(np.random.rand(5), index=df.index)
df['Numbers3'] = pd.Series(np.random.choice(66000, 5, replace=True), index=df.index)
# df['Numbers3'] = pd.Series(np.random.choice(1000, 6, replace=True), index=df.index) #6!=5 (expected numbers)

# update value of a cell in pandas
df.set_value('C', 'Numbers2', 0.90)
df.set_value('E', 'Numbers2', 0.90)
df.sort_values(['Numbers2', 'Numbers1', 'Numbers3'], ascending=False) # Descending
df['Numbers1'].max()
# df['Numbers1','Births'].max() # Error as df[ ..., ....] is invalid
df[['Numbers1','Births']].max() # Return max of two columns
df.max() # return max for all the columns
type(df['Names']) # Series
type(df[['Names']]) # DataFrame

df.plot() # draw all the indexes on x axis and their values on y-axis
plt.show()

df['Births'].plot()
plt.show()

# Maximum value in the data set
max_value_of_births = df['Births'].max()
# Name associated with the maximum value
index_satisfying_condition_of_max_births = df['Births'] == df['Births'].max()
type(index_satisfying_condition_of_max_births)
name_having_maximum_number_of_births = df['Names'][index_satisfying_condition_of_max_births].values
text_to_display = str(index_satisfying_condition_of_max_births) + " - " + name_having_maximum_number_of_births
# Add text to graph
df['Births'].plot()
plt.annotate(text_to_display, xy=(1, index_satisfying_condition_of_max_births), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')
print("The most popular name")
df[df['Births'] == df['Births'].max()]
plt.show()

dummy_dates_pd = generate_dates_using_date_time()
daily_branch_balance = [random.uniform(5000000, 100000000001) for x in range(len(dummy_dates_pd))]
list_of_tuples = list(zip(dummy_dates_pd, daily_branch_balance))
data_set = pd.DataFrame(data=list_of_tuples, columns=["Date", "BranchBalance"]) # index parameter --> index to rows

# The mapping can be specified many different ways:
#
# Type-1: A Python function, to be called on each of the axis labels.
# Type-2: A list or NumPy array of the same length as the selected axis.
# Type-3: A dict or Series, providing a label -> group name mapping.
# Type-4: For DataFrame objects, a string indicating a column to be used to group. Of course df.groupby('A') is just syntactic sugar for df.groupby(df['A']), but it makes life simpler.
# Type-5: For DataFrame objects, a string indicating an index level to be used to group.
# Type-6: A list of any of the above things

# A string passed to groupby may refer to either a column or an index level. If a string matches both a column name and an index level name then a warning is issued and the column takes precedence. This will result in an ambiguity error in a future version.
df_gb = data_set.groupby(['Date'])  # Creation of groupby object
df_gb = data_set.groupby('Date')  # Equivalent to above
print(df_gb)
type(df_gb)

# Type-1: A Python function, to be called on each of the axis labels.
def get_letter_type(letter):
    if letter.lower() in 'aieou':
        return 'vowel'
    else:
        return 'consonant'
df_gb_1 = data_set.head().groupby(get_letter_type, axis=1)



# data_set.pivot()