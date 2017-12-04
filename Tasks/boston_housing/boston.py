# Boston data set. I will solve use some examples from medium stackoverflow


import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
import sklearn.cross_validation
import statsmodels.api as sm

import seaborn as sns
sns.set_style('whitegrid')
sns.set_context('poster')

#
from sklearn.datasets import load_boston
boston = load_boston()
# By itself boston variable it is - Dictionary
print(boston.data.shape) # 506, 13
# It means, there are 506 rows of data with 13 columns
# So, how to know what are the names of these columns?
print(boston.feature_names) #['CRIM' 'ZN' 'INDUS' ...

# Let's convert it to pandas
bos = pd.DataFrame(boston.data)
print(bos.head())

# Columns are showing only indexes, not names, so..
# Convert indexes to the column names
bos.columns = boston.feature_names
print(bos.head())

# Column like price isn't in dataframe, because of
# column is available in other attribute called target
# We well use 'shape' of the boston.target
print(boston.target.shape)
# 506 rows is showing

# Now let add PRICE to DateFrame
bos['PRICE'] = boston.target
print(bos.head())

# Some STATISTICS
# Summary statistics
print(bos.describe())

# Split train-text dataset
# Split dataset into two:
# Target value and predictor values.
X = bos.drop('PRICE', axis = 1)
Y = bos['PRICE']

# Splitting dataset into train set, using snippet below
X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, Y, test_size = 0.33, random_state = 5)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

# Running Linear Regression
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X_train, Y_train)

Y_pred = lm.predict(X_test)

plt.scatter(Y_test, Y_pred)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$") # Let's show the plot 
plt.show()

# Now let's check Mean Squared Error
mse = sklearn.metrics.mean_squared_error(Y_test, Y_pred)
print(mse)