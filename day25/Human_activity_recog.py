"""
Q1. Human Activity Recognition

Human Activity Recognition with Smartphones

(Recordings of 30 study participants performing activities of daily living)

(Click Here To Download Dataset): https://github.com/K-Vaid/Python-Codes/blob/master/Human_activity_recog.zip



In an experiment with a group of 30 volunteers within an age bracket of 19 to 48 years, each person performed six
activities (WALKING, WALKING UPSTAIRS, WALKING DOWNSTAIRS, SITTING, STANDING, LAYING) wearing a smartphone 
(Samsung Galaxy S II) on the waist. The experiments have been video-recorded to label the data manually.

The obtained dataset has been randomly partitioned into two sets, where 70% of the volunteers was selected for
generating the training data and 30% the test data.

 

Attribute information 

For each record in the dataset the following is provided:

        Triaxial acceleration from the accelerometer (total acceleration) and the estimated body acceleration. 
        Triaxial Angular velocity from the gyroscope.
        A 561-feature vector with time and frequency domain variables.
        Its activity labels.
        An identifier of the subject who carried out the experiment.

Train a tree classifier to predict the labels from the test data set using the following approaches:

  (a) a decision tree approach,

  (b) a random forest approach and

  (c) a logistic regression.

  (d) KNN approach

Examine the result by reporting the accuracy rates of all approach on both the testing and training data set.
 Compare the results. Which approach would you recommend and why?

        Perform feature selection and repeat the previous step. Does your accuracy improve?
        Plot two graph showing accuracy bar score of all the approaches taken with and without feature selection.

""""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset_train= pd.read_csv("train.csv")
dataset_test= pd.read_csv("test.csv")

features_train= dataset_train.iloc[:,:561]
labels_train= dataset_train.iloc[:,562:]


features_test= dataset_train.iloc[:,:561]
labels_test= dataset_train.iloc[:,562:]


from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
labels_train = labelencoder.fit_transform(labels_train)
labels_test = labelencoder.fit_transform(labels_test)

labels_train =pd.DataFrame(labels_train)
labels_test =pd.DataFrame(labels_test)

#loop for features selection

import statsmodels.api as sm
features_x = sm.add_constant(features_train)
list2=[]
list1=list(range(562))
while True:
    features_opt= features_x.iloc[:,list1].values
    regressor_OLS=sm.OLS(endog = labels_train, exog=features_opt).fit()
    list2=regressor_OLS.pvalues
    list2-=list2[0]
    temp=np.max(list2)
    temp2=list2.argmax()
    temp2=int(temp2[1:])
    if temp>0.08:
        list1.pop(temp2)
    else:
        break

list1.pop(0)
list1=np.array(list1)
list1=list1-1


features_red=features_train.iloc[:,list1]


#************************** kNN Apporach (without feature selection)*******************************#


from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

probability = classifier.predict_proba(features_test)
labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
from sklearn import metrics
cm = confusion_matrix(labels_test, labels_pred)

print (metrics.mean_squared_error(labels_test, labels_pred))


#************************* kNN Apporach (With feature selection)****************************************#

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_red, labels_train)
labels_pred = classifier.predict(features_red)

cm = confusion_matrix(labels_train, labels_pred)
print (metrics.mean_squared_error(labels_train, labels_pred))



#************************* logistic regression (without feature selection)***************************#


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)


predd=classifier.predict(features_test)
cm2 = confusion_matrix(labels_test, predd)
print (metrics.mean_squared_error(labels_test, predd))

#***************************logistic regression (with feature selection)**********************



from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_red, labels_train)


predd=classifier.predict(features_red)
cm2 = confusion_matrix(labels_test, predd)
print (metrics.mean_squared_error(labels_test, predd))


#************************** Decision Tree (without feature selection)*********************************#


from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

cm3 = confusion_matrix(labels_test, labels_pred)
print (metrics.mean_squared_error(labels_test, labels_pred))

#************************** Decision Tree (with feature selection)*********************************#


from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_red, labels_train)

labels_pred = classifier.predict(features_red) 

cm3 = confusion_matrix(labels_test, labels_pred)
print (metrics.mean_squared_error(labels_test, labels_pred))



#************************** Random Froest (without feature selection)***********************************#


from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features_train, labels_train)  

labels_pred = classifier.predict(features_test)  

cm4 = confusion_matrix(labels_test, labels_pred)
print (metrics.mean_squared_error(labels_test, labels_pred))


#************************** Random Froest (with feature selection)***********************************#


from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features_red, labels_train)  

labels_pred = classifier.predict(features_red)  

cm4 = confusion_matrix(labels_test, labels_pred)
print (metrics.mean_squared_error(labels_test, labels_pred))





