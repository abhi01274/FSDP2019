"""

Code Challenges:
    Name:
        University Admission Prediction Tool
    File Name:
        uni_admin.py
    Dataset:
        University_data.csv
    Problem Statement:
         Perform Linear regression to predict the chance of admission based on all the features given.
         Based on the above trained results, what will be your estimated chance of admission.

"""
import pandas as pd  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('University_data.csv')  

#data prep
features = dataset.iloc[:, :-1].values  
label = dataset.iloc[:, -1 ].values 



from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

features = features[:, 1:]


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, label, test_size=0.3, random_state=0)  


#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 


pred= regressor.predict(features_test)

