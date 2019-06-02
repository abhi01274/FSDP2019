"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score

"""



import pandas as pd  
import numpy as np  


dataset = pd.read_csv("kc_house_data.csv")


features= dataset.drop(["date","price"],axis=1)
labels = dataset.iloc[:,2:3]

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 


from sklearn import metrics
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)  



# Fitting Polynomial Regression to the dataset
from sklearn.linear_model import LinearRegression

lin_reg_2 = LinearRegression()
lm1=lin_reg_2.fit(features_train, labels_train)

lm2=lin_reg_2.predict(features_test)
print (metrics .mean_squared_error(labels_test,lm2 ) )





 
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
lm_lasso = Lasso() 
lm_ridge =  Ridge() 



predict_test_lm=lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)

lm2=lm_lasso.predict(features_test)
lm3=lm_ridge.predict(features_test)


print (np.round(metrics .mean_squared_error(labels_test, lm2),2) )

print (np.round(metrics .mean_squared_error(labels_test, lm3),2) )








