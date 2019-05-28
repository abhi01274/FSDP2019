"""

Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.

"""


import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('bluegills.csv')
features = dataset.iloc[:, 0:1].values
labels = dataset.iloc[:, 1].values

#let's first analyze the data
# Visualising the Linear Regression results
plt.scatter(features, labels)

# Fitting Linear Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_objects= PolynomialFeatures(degree = 3)
features_poly = poly_objects.fit_transform(features)


from sklearn.linear_model import LinearRegression

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)

plt.scatter(features, labels ,color = 'red')
plt.plot(features ,lin_reg_2.predict(features_poly))

lin_reg_2.predict(poly_objects.transform(5))















