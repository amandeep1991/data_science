import pandas as pd
import numpy as np
from numpy.core import int64, float64
from sklearn.linear_model import LogisticRegression

# pd.set_option('display.width', None)
from ml.problems.hpe_ntro.my_code import df_train

pd.set_option('display.width', 320)
pd.set_option('display.max_columns', None)


df = pd.read_csv("titanic_train.csv")

df.describe()
len(df.columns)
df.describe().shape
df.info()

df.dtypes
type(df.dtypes)

sum(df.dtypes == int64)
sum(df.dtypes == float64)
sum(df.dtypes == object)
sum(df.dtypes != int64)
df.loc[:,df.dtypes==object].head()

df.where(df.dtypes!=int64, df).head()

df.query(df.dtypes!=int64 & df.dtypes!=float64)

df.loc[:, (df.dtypes!=int64) & (df.dtypes!=float64)].head()
df.select_dtypes(exclude=[float64, int64]).head()
df.select_dtypes(exclude=['float64', 'int64']).head()
df.select_dtypes(include=['object']).head()
df_obj = df.select_dtypes(include=[object])

isnull__any_axis_0 = df_obj.isnull().any(axis=0)
isnull__any_axis_0

isnull__any_axis_1 = df_obj.isnull().any(axis=1)
type(df_obj[isnull__any_axis_1])
len(df_obj[isnull__any_axis_1])
df_obj.shape
df_obj[isnull__any_axis_1].shape
df_obj.info()
dd1 = df_obj["Name"].value_counts()
dd2 = df_obj["Sex"].value_counts()
dd3 = df_obj["Ticket"].value_counts()
dd4 = df_obj["Cabin"].value_counts()
dd5 = df_obj["Embarked"].value_counts()

value_counts_list = (dd1,dd2,dd3,dd4,dd5)
ddd = pd.DataFrame()
for v_c in value_counts_list:
    if len(v_c)<5:
        ddd = ddd.append(v_c)
ddd


# cleanup_nums = {"Embarked": {"S": 1, "C": 2, "Q": 3},
#                 "Sex": {"male": 0, "female": 1}}

# Label encoding is simply converting each value in a column to a number.
# df_obj.replace(cleanup_nums, inplace=True)
df_obj["Embarked"] = df_obj["Embarked"].astype('category')
df_obj.columns
df_obj['Embarked_num'].value_counts()


#3 - One Hot Encoding
# Label encoding has the advantage that it is straightforward but it has the disadvantage that the numeric values can be “misinterpreted” by the algorithms. For example, the value of 0 is obviously less than the value of 4 but does that really correspond to the data set in real life? Does a wagon have “4X” more weight in our calculation than the convertible?
# This has the benefit of not weighting a value improperly but does have the downside of adding more columns to the data set.
pd.get_dummies(df_obj, columns=["Sex","Embarked"]).head()

# 4 - Custom Binary Encoding
# Depending on the data set, you may be able to use some combination of label encoding and one hot encoding to create a binary column that meets your needs for further analysis.
df_obj["OHC_Code"] = np.where(df_obj["Sex"].str.contains("male"), 1, other=0)

#5 Scikit-Learn: But pandas are simpler


# Deleting columns
# Delete the "Area" column from the dataframe
data = pd.DataFrame()
data = data.drop("Area", axis=1)
# alternatively, delete columns using the columns parameter of drop
data = data.drop(columns="area")
# Delete the Area column from the dataframe in place
# Note that the original 'data' object is changed when inplace=True
data.drop("Area", axis=1, inplace=True)
# Delete multiple columns from the dataframe
data = data.drop(["Y2001", "Y2002", "Y2003"], axis=1)


df['Cabin'].describe()
df[['Cabin']].info()

df.columns

# df_x = df.

model = LogisticRegression()
model.fit()


df_train.Age.where(np.isnan(df.Age), df.Age,other=0)

df.Age[889]
type(df.Age[888])
df.Age[887]

df.isnull().any(axis=1)