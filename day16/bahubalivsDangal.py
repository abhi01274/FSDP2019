"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""


import pandas as pd  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')  

#data prep
features = dataset.iloc[:, :-2].values  
label1 = dataset.iloc[:, 1:2].values 
label2= dataset.iloc[:,2:].values



from sklearn.model_selection import train_test_split  
features_train1, features_test1, labels_train1, labels_test1 = train_test_split(features, label1, test_size=0.3, random_state=0)  
features_train2, features_test2, labels_train2, labels_test2 = train_test_split(features, label2, test_size=0.3, random_state=0)  

from sklearn.linear_model import LinearRegression  
regressor1 = LinearRegression()  
regressor1.fit(features_train1, labels_train1) 

regressor2 = LinearRegression()  
regressor2.fit(features_train2, labels_train2) 

pred1=regressor2.predict(features_test1) 

print("bahubali collections are: ",regressor1.predict(10))
print("Dangal collections are: ",regressor2.predict(10))


#------------------------------------------------------------------------------



#alternate with two labels


import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')  

#data prep
features = dataset.iloc[:, :-2].values  
label = dataset.iloc[:, 1:3].values 


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, label, test_size=0.3, random_state=0)  

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 

pred1= np.array([10])
pred1=pred1.reshape(1,-1)
pred1=regressor.predict(pred1) 

print("on day 10 bahubali at ",pred1[0][0])
print("on day 10 Dangal is at ",pred1[0][1])
