"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.

"""


import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 

dataset = pd.read_csv("PastHires.csv")  
dataset= dataset.replace({"Y" : 1 ,"N" :0,"BS" : 0, "MS" :1 , "PhD" : 2})

features = dataset.drop('Hired', axis=1)  
labels = dataset["Hired"]



from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features, labels)  

labels_pred = classifier.predict(features)

df=pd.DataFrame({'Actual':labels, 'Predicted':labels_pred})  
df

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_pred,labels)

classifier.score(features,labels_pred)



#random forest


from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=25, random_state=0)  
classifier.fit(features, labels)  
labels_pred = classifier.predict(features)  


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_pred,labels)

classifier.score(features,labels_pred)


