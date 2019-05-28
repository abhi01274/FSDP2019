"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv FileS

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.
"""



import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Female_stats.csv')
#temp = dataset.values
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:, 0:1].values


import statsmodels.api as sm
features = sm.add_constant(features)

features_opt = features[:, [1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
print("both IV are important")

from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features_opt, labels)

print(lin_reg_1.coef_)

print("When Father’s Height Is Held Constant, The Average Student Height Increases By ",lin_reg_1.coef_[0][0])
print("When Mothers’s Height Is Held Constant, The Average Student Height Increases By ",lin_reg_1.coef_[0][1])
