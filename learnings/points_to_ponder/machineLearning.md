# What is machine learning
    * next natural step of AI - processing, understanding data and reacting intelligence
    * applied statistics - evaluate, summarize data using advance formulaes
    * advanced algorithms - operate on input and provide some output
So to recapitulate  it is the next evolution step for a lot of things

# How machine learning different from traditional programming?
    * Traditionally we built the decision making directly into the program.
        * So if we want to write traditional program to detect a human face, we would write look the eyes, eye-brows, nose, mouth etc.
    * With machine learning, we would write any of such thing in the program. We would build an agent which would look at a set of images at a time and figure out whose face that might be.
        * why now - computers are more relied now a days and a lot of data is getting generated so is at our service to make risk-free strategies to increase the profit.

# Applications:-
    * Machine learning can be applied to nearly all the domains.
    * To exemplify - Electronic Trading, disease diagnosis,
    
# Important Points:
>* Today I know that the most important thing to learn to become a Data Scientist is the pipeline, i.e, the process of getting and processing data, understanding the data, building the model, evaluating the results (both of the model and the data processing phase) and deployment.
>* Pipelining is important in datascience:
![001.MachineLearning_Pipeline.jpg](img/001.MachineLearning_Pipeline.jpg)

# Types of data
>1. Numerical
>>* Quantitative Measurement
>>>* **Discrete** - Integer based, countable number of possible values
>>>* **Continous** - Infinite number of possible values.
>2. Categorical
>>* No inherit mathematical meaning. 
>>* Can represent them compactly by numbers but they must not add any mathematical meaning in it. 
>3. Ordinal
>>* Categorical type data which have some mathematical meaning in it.
>>>* Movie Rating, Juice glass size.

# Mean, Median & Mode
>* Mean - average
>* Median - sort & take average of middle element (**less susceptible to outliers**)  
>* Mode -  most common value (only works with discrete numerical or categorical or ordinal data)




# Variance and Standard Deviation:
>* Both tells about spread of the data, shape & distribution of data-set.
>>* Variance:
>>>* Average of the squared differences from the mean.
>>* Standard Deviation:
>>>* square root of the variance.
>>* Data points tha lie more than 1 std from the mean can be considered as unusual.

# Population vs Sample:
>* Population - complete set of data-set. Population Variance is used.
>* Sample - subset of complete set of data-set. Sample Variance is used.
>>* Sum of squared differences from mean / (n-1)
![002.MachineLearning_Variance.jpg](img/002.MachineLearning_Variance.jpg)

# Probability Density Function: (continuous data)
![003.MachineLearning_NormalDensiityDistribution.jpg](img/003.MachineLearning_NormalDensiityDistribution.jpg)

# Probability Mass Function: (discrete data)
![004.MachineLearning_ProbabilityMassFunction.jpg](img/004.MachineLearning_ProbabilityMassFunction.jpg)


# Percentiles and moments
>* Percentiles: In the data-set, what's the point at which X% of the values are less than that value? Eg - Income Distribution.
>>* 50 percentile means median
>>* Used in quartile or normal distribution
![007.MachineLearning_Percentiles.jpg](img/007.MachineLearning_Percentiles.jpg)
>* Moments:
>>* Quantitative measures of the shape of a probability density function.
![008.MachineLearning_Moments.jpg](img/008.MachineLearning_Moments.jpg)  
>>* Used to measure the shape of the **density function**.
>>>* The first moment is the mean.
>>>* The second moment is the variance.
>>>* Third moment is called **skew**:
>>>>* How lopsided is the distribution?
>>>>* A distribution with a longer tail on the left will be skewed left and have negative skew.
![009.MachineLearning_3rdMomentSkew.jpg](img/009.MachineLearning_3rdMomentSkew.jpg)
>>>* Fourth Moment is **kurtosis**:
>>>>* How thick is the tail and how sharp is the peak, compared to the normal distribution.
>>>>* **Higher peaks have higher kurtosis**
![010.MachineLearning_4thMomentKurtosis.jpg](img/010.MachineLearning_4thMomentKurtosis.jpg)
>>* **Understanding skew: change the normal distribution to be centered around 10 instead of 0, and see what effect that has on the moments. The skew is still near zero; skew is associated with the shape of the distribution, not its actual offset in X. (only mean changes as per the position other nth moment will remain the same)**
 




