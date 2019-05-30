"""
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year",
    "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the
    MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration
    around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from
    both the models)

"""

#6,215,100,2630,22.2,80,3

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 

dataset = pd.read_fwf("Auto_mpg.txt",header=None)  


dataset.columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]

df=pd.DataFrame(dataset)
df1=df[["car name","mpg"]]
print(df1.max())

list2=[]

features= dataset.iloc[:,1:-1]
labels = dataset['mpg'] 


features["horsepower"]=features["horsepower"].replace(["?"], features["horsepower"].mode())

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 

from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)

df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
df


list1=[6,215,100,2630,22.2,80,3]
list1= np.array(list1)
list1=list1.reshape(1,-1)
print("mpg of given car with the features is ",regressor.predict(list1)[0],"mpg")








#random forest-----------------------------------------------------------------







from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)  
list2.append(sc)

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=95, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)  


df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  

df


list1=[6,215,100,2630,22.2,80,3]
list1= np.array(list1)
list1=list1.reshape(1,-1)
list2[0]

list1=list2[0].transform(list1)

print("the mpg of car is",regressor.predict(list1)[0])  

























