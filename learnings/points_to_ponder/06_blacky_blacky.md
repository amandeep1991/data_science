######1. Can you just go through your resume, what projects you have worked and on which project you are currently working?

######2. What technology you are using for this project?
>>2.1. **Collateral Management** - Using Calypso with Microservices (Doesn't give any cognitive features)

>>2.2. For the same we have some modules written in python (reading Oracle DB - sqlalchemy - select query, created few models - send out a report to CVO users)


######3. What kind of algorithms you are using to predict this model?
>>3.1. Linear regression


######4. What kind of bi-variant or dependent variable, continuous variables? What about independent variable and how many in total, what's the performance of this model? What is the R-square of the model then what's the performance measuring criteria?
>>4.1. Dependent - continuous

>>4.2. Independent variables - combination of both continuous and categorical. Total were 70 to 80 and used 50-60 features

>>4.3. The coefficient of determination, R2, is used to analyze how differences in one variable can be explained by a difference in a second variable.
>>>4.3.1. The range is 0 to 1 

>>>4.3.2. The correlation coefficient formula will tell you how strong of a linear relationship there is between two variables. 

>>>4.3.3. R Squared is the square of the correlation coefficient, r (hence the term r squared). 

>>>4.3.4. It gives you an idea of how many data points fall within the results of the line formed by the regression equation. 

>>>4.3.5. The higher the coefficient, the higher percentage of points the line passes through when the data points and line are plotted.

>>>4.3.6. If the coefficient is 0.80, then 80% of the points should fall within the regression line. Values of 1 or 0 would indicate the regression line represents all or none of the data, respectively.

>>>4.3.7. The CoD can be negative, although this usually means that your model is a poor fit for your data. It can also become negative if you didn’t set an intercept.

>>>4.3.8. Key Limitations of R-squared:

>>>> R-squared cannot determine whether the coefficient estimates and predictions are biased, which is why you must assess the residual plots.

>>>> R-squared does not indicate whether a regression model is adequate. You can have a low R-squared value for a good model, or a high R-squared value for a model that does not fit the data!.


>>>4.3.9. **sklearn.metrics.r2_score(y_true, y_pred)** - 0.9


######5. What is the training and test split - 80 to 20? (what about period)


######6. Why you selected regression as the first? - dependent variable is continous that's why a regression.


######7. You must have judges certain criteria whether this is suitable for regression or not (about independant variables)
>>7.1. Business initially gave around 70 to 80 percentage


######8. What about other criteria?
>>8.1. Did you check the relationship between dependent and independant variable?

>>8.2. Let's one of the indepandant variable is non-linearly relates to dependant variables? Did you check the same between each possible combination?


######9. You did courses on machine learning?
>>9.1. In which scenario we use decision tree or random forest or clustering for this one or gradient or ada boosting in one?

>>9.2. Supervised or Non-Supervised? -> Classification problem

>>9.3. On what basis you pick the first node of among all independent variables?

>>>9.3.1. Entropy Formula

>>>9.3.2. Gini Formula

>>9.4. At what point should we stop the tree?

>>>9.4.1. We can go till the last leave node but that would be an overfitting (ideally we should prune these leaves)

>>>9.4.2. This is situational question

>>9.5. Have you used any pruning techniques for decision tree
>>> 1. Pre-pruning:

>>> 2. Reduced error pruning (Starting at the leaves, each node is replaced with its most popular class. If the prediction accuracy is not affected then the change is kept. While somewhat naive, reduced error pruning has the advantage of simplicity and speed)

>>> 3. Error complexity pruning (Starting at the leaves, each node is replaced with its most popular class. If the prediction accuracy is not affected then the change is kept. While somewhat naive, reduced error pruning has the advantage of simplicity and speed)

>>> 4. Cost complexity pruning (Starting at the leaves, each node is replaced with its most popular class. If the prediction accuracy is not affected then the change is kept. While somewhat naive, reduced error pruning has the advantage of simplicity and speed)

######10. Single dimension array: calculate sliding window average

######11. Features that have been used (eligiblity criteria, ratings) 
######12. I have an equation with 3 variables and these 3 features are highly correlated, where do you think it will create problem if I just need to predict the value of dependent value. (if I am just interested in final value of prediction)
######13. If you are created different models for different security, so let's pick one security why I need all independent variables independant for the final value.
######14. What is collinearity?
######15. Let's talk about scatter plot - correction vs spearsman vs kandal ( y =x is correlated means correlation = 1, but what if y = x*2 what is the correlation)
######16. What does expectation mean?
######17. Relationship between expectation and pearson coorelation coefficient?
######18. Can correlation coefficients work non-linear kind of relation? Why it is not good?
######19. You worked in linear reqression. What is main linear regression hypothesis? Is there any assumption or hypothesis which we need to satisfy before applying it. -> Multicollinear (is it only for linear regression or for others as well). What things I need to test before applying linear regression.
######20. What is the difference between R-square and Adjusted R-square.
######21. From explaination: Why increase to R-square will lead to over-fitting
######22. You have 5 variables and r-square of model is very less. Non of them is having linear relation. YOu don't have any other data. What would be the next step.
    I would exclude a particular feature and then find r-square - issue
    Main reason why model didn't performed well, you can only used linear regression model. Is there anything you can do here --> polynomial regression
######23. How do you figure out what polynomial I should use. Start with 2 degress but then you tried 3 and it got improved. But where to stop to avoid over-fitting. - techniques - ridge regression/lasso?
######24. Linear regression vs ridge regression
######25. What is regularization? types-ridge regression?
######26. Liquidity funds model creation? redemption/txn cost. start with data management/data pipeline-etl/data-processing - a lot of noisy data/later on creating models/how much money should we have in reserved/ python or scala(mostly) - sparks.