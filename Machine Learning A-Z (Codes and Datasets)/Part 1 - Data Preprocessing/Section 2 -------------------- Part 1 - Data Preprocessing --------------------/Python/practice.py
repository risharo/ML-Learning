# Importing the necessary libraries
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load the dataset
df = pd.read_csv('titanic.csv')

# Identify the categorical data
print(df.info())
for i in list(df):
    # if df[i].dtype == object:
        unique_val = len(set(df[i].values))
        print(f"{i} has dtype:{df[i].dtype}\n unique values: {unique_val}")
        if unique_val<50:
                print(set(df[i].values))
        print("\n")
#categorical data is sex, Embarked
# Implement an instance of the ColumnTransformer class


# Apply the fit_transform method on the instance of ColumnTransformer


# Convert the output into a NumPy array


# Use LabelEncoder to encode binary categorical data


# Print the updated matrix of features and the dependent variable vector

