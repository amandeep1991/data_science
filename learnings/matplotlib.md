# Enable inline plotting in jupiter notebook
# %matplotlib inline

```python
import matplotlib.pyplot as plt
plt.clf() # clear the graph

import numpy as np
incomes = np.random.normal(100.0, 50.0, 10000)
plt.hist(incomes, 50) # Used to find the shape and distribution of the data
plt.show()
```

# Line Plot:
>* Used to track changes over short and long periods of time.
>* Can also be used to compare changes over the same period of time for more than one group.

# Scatter Plot
>* Used to determine relationships between the two different things i.e. Co-relation between two or more variables.

# Histogram Plot
>* Used to visualize the distribution of data (normal distribution or skewed distribution etc).

# Box Plot
>* Used to summarize the data
>>* Uses:
>>>* Useful for visualizing the spread & skew of data.
>>>* The red line represents the median of the data, and the box represents the bounds of the 1st and 3rd quartiles.
>>>* So, half of the data exists within the box.
>>>* The dotted-line "whiskers" indicate the range of the data - except for outliers, which are plotted outside the whiskers. Outliers are 1.5X or more the interquartile range.
>>>* This example below creates uniformly distributed random numbers between -40 and 60, plus a few outliers above 100 and below -100:
>>* **5-point summary**:
>>>* Minimum value – the smallest value in the data set
>>>* Second quartile – the value below which the lower 25% of the data are contained
>>>* Median value – the middle number in a range of numbers
>>>* Third quartile – the value above which the upper 25% of the data are contained
>>>* Maximum value – the largest value in the data set

```python
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
population = [2.5, 3.6, 5.2, 6.9]
plt.plot(year, population)
plt.show()


plt.clf()
plt.plot(year, population)
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()


plt.scatter(year, population)



values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values)
plt.show()

plt.hist(values, bins=3)
plt.show()


plt.boxplot(values)


# Line plot for normal distribution (pdf - probability density function)
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.01)

plt.plot(x, norm.pdf(x))
plt.show()


# Mutiple Plots on One Graph
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()


# Save it to a File
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.savefig('.\myPlot.png', format='png')


# Adjust the axes
axes = plt.axes()

axes.set_xlim([-5, 5])   # show graph for values of x between -5 and 5 
axes.set_ylim([0, 1.0])  # show graph for values of y between 0 and 1.0
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()


# Add a Grid
axes = plt.axes()

axes.grid()

plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()



# Change Line Types and Colors
plt.plot(x, norm.pdf(x), 'b-') # 'b-' -> blue line
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r:') # 'r:' -> red dots
plt.show()


# Labeling Axes and Adding a Legend
plt.xlabel('Greebles')
plt.ylabel('Probability')

plt.plot(x, norm.pdf(x), 'b-')
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r:')

plt.legend(['Sneetches', 'Gacks'], loc=4) # labelling for different lines in the graph

plt.show()

```


# XKCD Style
```python

import matplotlib.pyplot as plt
import numpy as np

plt.xkcd()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([-30, 10])

data = np.ones(100)
data[70:] -= np.arange(30)

# color = 'r' for red text or annotation
# xytext = left top corner for text
# xy = arrow pointing to this location
# arrowprops = properties of arrow in the form of dictionary
plt.annotate(
    'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
    xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10)) 

plt.plot(data) # plt.plot(data, 'r') for red line

plt.xlabel('time')
plt.ylabel('my overall health')

```

# Pie Chart
```python
import matplotlib.pyplot as plt

# Remove XKCD mode:
plt.rcdefaults()

values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
explode = [0.3, 0, 0.2, 0, 0]
labels = ['India', 'United States', 'Russia', 'China', 'Europe']
plt.pie(values, colors= colors, labels=labels, explode = explode)
plt.title('Student Locations')
plt.show()

```


# Bar Chart
```python
import matplotlib.pyplot as plt

values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
plt.bar(range(0,5), values, color= colors)
plt.show()

```

# Scatter Plot
```python
from pylab import randn
import matplotlib.pyplot as plt

X = randn(500)
Y = randn(500)
plt.scatter(X,Y)
plt.show()
```

