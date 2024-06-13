# Importing the necessary libraries
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load the dataset
df = pd.read_csv('titanic.csv')

# Identify the categorical data
## categorical data is 'Sex', 'Pclass', 'Embarked' in independent features set
categorical_data = ['Sex', 'Pclass', 'Embarked']




# Implement an instance of the ColumnTransformer class
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(),categorical_data)], remainder = 'passthrough')

# Apply the fit_transform method on the instance of ColumnTransformer
x = np.array(ct.fit_transform(df))

# Convert the output into a NumPy array


# Use LabelEncoder to encode binary categorical data
le = LabelEncoder()
y = le.fit_transform(df['Survived'])

# Print the updated matrix of features and the dependent variable vector
print(x)
print(y)
