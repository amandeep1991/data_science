
# Numpy Arrays vs Lists: [Less memory, Better performance]
>* Numpy arrays are densely packed arrays of homogeneous type. Python lists, by contrast, are arrays of pointers to objects, even when all of them are of the same type. So, you get the benefits of locality of reference.
>* Also, many Numpy operations are implemented in C, avoiding the general cost of loops in Python, pointer indirection and per-element dynamic type checking. The speed boost depends on which operations you're performing

# Pearson Coefficient
>* **numpy.corrcoef**: Return Pearson product-moment correlation coefficients
```python
import numpy as np
x,y = [], []
np.corrcoef(x, y)[0,1]
```

>* Better option is use **scipy.stats.pearsonr**, which calculates a Pearson correlation coefficient and the p-value for testing non-correlation.
>>* The Pearson correlation coefficient measures the linear relationship between two datasets. Strictly speaking, Pearson’s correlation requires that each dataset be normally distributed. Like other correlation coefficients, this one varies between -1 and +1 with 0 implying no correlation. Correlations of -1 or +1 imply an exact linear relationship. Positive correlations imply that as x increases, so does y. Negative correlations imply that as x increases, y decreases.
>>* The p-value roughly indicates the probability of an uncorrelated system producing datasets that have a Pearson correlation at least as extreme as the one computed from these datasets. The p-values are not entirely reliable but are probably reasonable for datasets larger than 500 or so.
```python
import scipy
x,y = [], []
scipy.stats.pearsonr(x, y)
``` 

# Return a contiguous flattened array. (\\mine: More options for ravel needs to be explored)
```python
import numpy as np
first_array = np.array([[1,2,3,4],[1,2,3,4]])
np.ravel(first_array)
```

# Generate a np-array of floats (\\mine: More options for ravel needs to be explored)
```python
import numpy as np
np.random.randn(9)
```


# Difference between np.random.seed() and np.random.RandomState()
>* If you want to set the seed that calls to np.random... will use, use np.random.seed.
>* If you want to use the class, you must save an instance of the class, initiated with a seed.