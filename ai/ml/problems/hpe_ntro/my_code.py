import pandas as pd
from numpy.core import int64, float64
from sklearn.linear_model import LogisticRegression

pd.set_option('display.width', 320)
pd.set_option('display.max_columns', None)
df_train = pd.read_csv("titanic_train.csv")
df_test = pd.read_csv("titanic_test.csv")

print('Columns other than int and float: ', df_train.select_dtypes(exclude=[int64, float64]).columns)
print('Columns of type int: ', df_train.select_dtypes(include=[int64]).columns)
print('Columns of type float: ', df_train.select_dtypes(include=[float64]).columns)

for column in df_train.columns:
    print("############################################################")
    print("Details of ", column, "::")
    print("##################")
    print(df_train[[column]].info())
    print("##################")
    print(df_train[column].value_counts())


df_train_drop = df_train.drop(['Name', 'Ticket', 'PassengerId', "Cabin"], axis=1)
df_train_encoded = pd.get_dummies(df_train_drop, columns=["Sex", "Embarked"])

df_train_encoded['Age'].fillna((df_train_encoded['Age'].mean()), inplace=True)

tuples_having_null_values = df_train_encoded.isnull().any(axis=1)
if len(df_train_encoded[tuples_having_null_values])==0:
    print("Hurrey! no nan values")

print("Since", (sum(tuples_having_null_values) * 100 / df_train_encoded.shape[0]), "% records have missing entries")

df_train_X = df_train_encoded.drop('Survived', axis=1)
ser_train_y = df_train_encoded['Survived']

model = LogisticRegression()
model.fit(df_train_X, ser_train_y)

df_test_drop = df_train.drop(['Name', 'Ticket', 'PassengerId', "Cabin"], axis=1)
df_test_encoded = pd.get_dummies(df_test_drop, columns=["Sex", "Embarked"])
df_test_encoded['Age'].fillna((df_test_encoded['Age'].mean()), inplace=True)


tuples_having_null_values = df_test_encoded.isnull().any(axis=1)
if len(df_test_encoded[tuples_having_null_values])==0:
    print("Hurrey! no nan values")

df_test_X = df_test_encoded.drop('Survived', axis=1)
ser_test_y = df_test_encoded['Survived']

model.score(df_test_X, ser_test_y)


