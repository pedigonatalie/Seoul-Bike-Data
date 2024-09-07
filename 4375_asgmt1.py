# -*- coding: utf-8 -*-
"""4375_asgmt1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CfN6E3g7uqTU0Ed2tii62JjAcZ8-wojZ

# Seoul Bike Data
We have several attributes pertaining to weather used to predict the amount of bikes rented per hour in Seoul. Predicting the amount of bikes needed in a given hour will reduce wait times.

# Importing Data Set and Libraries
"""

import pandas as pd
from sklearn.linear_model import SGDRegressor
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://github.com/pedigonatalie/Seoul-Bike-Data/raw/main/SeoulBikeData.csv'
data = pd.read_csv(url, encoding ='latin1')
df = pd.DataFrame(data)
df.head()

"""# Preprocessing Data"""

# check for null values
df.isnull().sum()

# check for missing data
df.isna().sum()

# check for inconsistencies (?)

# removing redundant rows
df.drop_duplicates(inplace=True)
df.shape

# convert any categorical attributes to numerical, if needed
# ref: #https://saturncloud.io/blog/how-to-convert-categorical-data-to-numerical-data-with-pandas/#:~:text=Converting%20Categorical%20Data%20to%20Numerical%20Data&text=The%20easiest%20way%20to%20convert,numerical%20representation%20of%20each%20category.
df['Seasons'] = df['Seasons'].astype('category')
df['Seasons'] = df['Seasons'].cat.codes

df['Holiday'] = df['Holiday'].astype('category')
df['Holiday'] = df['Holiday'].cat.codes

df['Functioning Day'] = df['Functioning Day'].astype('category')
df['Functioning Day'] = df['Functioning Day'].cat.codes

df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day of Week'] = df['Date'].dt.weekday
df.drop('Date', axis=1, inplace=True)

df.head()

# standardize the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
y = df['Rented Bike Count']
X = df.drop(['Rented Bike Count'], axis=1)
X_scaled = scaler.fit_transform(X)

# After scaling X, the columns should now have mean of 0 and variance of 1
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
X_scaled.describe()

# find attributes most correlated with the outcome
correlation_matrix = df.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)

sns.pairplot(df)

# get rid of any attributes not correlated with the outcome
features = ['Temperature(°C)', 'Humidity(%)', 'Hour', 'Dew point temperature(°C)']

sns.boxplot(data=df[features])

X = X_scaled[features]

# split the data into testing and training parts (ratio is up to us)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

X_train.shape, X_test.shape

"""# Model Construction"""

# use training dataset to construct a linear regression model using gradient descent
# Use GridSearchCV to determine the best parameters
from sklearn.model_selection import GridSearchCV
params = [{'early_stopping' : [True, False],'max_iter' : [1000, 10000, 100000], 'learning_rate' : ['constant', 'optimal', 'invscaling', 'adaptive'], 'alpha' : [0.001, 0.0001, 0.00001], 'tol' : [0.0001, 0.001, 0.01, 0.1]}]
my_grid = GridSearchCV(estimator = SGDRegressor(), param_grid=params, scoring = 'r2')
my_grid.fit(X_train, y_train)
print(my_grid.best_params_)

sgd = SGDRegressor(max_iter=10000, tol=1e-4, early_stopping = True, random_state = 5, alpha = 0.01)
sgd.fit(X_train, y_train)

# tune hyper-parameters and log experiments

sgd.coef_

sgd.intercept_

y_pred_train = sgd.predict(X_train)
mse_train = mean_squared_error(y_train, y_pred_train)
mae_train = mean_absolute_error(y_train, y_pred_train)
ev_train = explained_variance_score(y_train, y_pred_train)
r2_train = r2_score(y_train, y_pred_train)
print('MSE Train:', mse_train)
print('MAE Train:', mae_train)
print('EV Train:', ev_train)
print('R2 Train:', r2_train)
print('Score Train:', sgd.score(X_train, y_train))
print(sgd.coef_)

# apply our model to the testing portion of the dataset
sgd.score(X_test, y_test)

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score
y_pred = sgd.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
ev = explained_variance_score(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Report the test dataset error values for the best set of parameters obtained from previous part
# If you are not satisfied with your answer, you can repeat the training step.

print('MSE Test:', mse)
print('MAE Test:', mae)
print('EV Test:', ev)
print('R2 Test:', r2)
print('Score Test:', sgd.score(X_test, y_test))
print(sgd.coef_)

# residual plot
residuals = y_test - y_pred
plt.figure(figsize=(8, 6))
sns.residplot(x=y_pred, y=residuals, lowess=True, color='blue', line_kws={'color': 'red', 'lw': 1})
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()