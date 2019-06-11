"""
Q1. 

(Click Here To Download Training data File): 
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json

(Click Here To Download Test data File):
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json


This is the data for local classified advertisements. It has 9 prominent sections: jobs, resumes, gigs, personals, housing, community, services, for-sale and discussion forums. Each of these sections is divided into subsections called categories. For example, the services section has the following categories under it:
beauty, automotive, computer, household, etc.

For a set of sixteen different cities (such as newyork, Mumbai, etc.), we provide to you data from four sections

        for-sale
        housing
        community
        services

and we have selected a total of 16 categories from the above sections.

        activities
        appliances
        artists
        automotive
        cell-phones
        childcare
        general
        household-services
        housing
        photography
        real-estate
        shared
        temporary
        therapeutic
        video-games
        wanted-housing

Each category belongs to only 1 section.

About Data:

        city (string) : The city for which this Craigslist post was made.
        section (string) : for-sale/housing/etc.
        heading (string) : The heading of the post.

each of the fields have no more than 1000 characters. The input for the program has all the fields but category which you 
have to predict as the answer.

A total of approximately 20,000 records have been provided to you, proportionally represented across these sections, 
categories and cities. The format of training data is the same as input format but with an additional field "category", 
the category in which the post was made.

Task:

    Given the city, section and heading of an advertisement, can you predict the category under which it was posted?
    Also Show top 5 categories which has highest number of posts
    
"""



import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt


url="http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json"
url2="http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json"
data1= requests.get(url)
data2= requests.get(url2)

data1=data1.text
data2=data2.text


dataset_train= pd.read_json(data1,lines=True)
dataset_test= pd.read_json(data2,lines=True)


import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []


for i in range(0, 20217):
    review = re.sub('[^a-zA-Z]', ' ', dataset_train['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features2 = cv.fit_transform(corpus).toarray()
features2= pd.DataFrame(features2)



from sklearn.preprocessing import LabelEncoder
labelen= LabelEncoder()
dataset_train["city"]=labelen.fit_transform(dataset_train.iloc[:,1])


from sklearn.preprocessing import LabelEncoder
labelen= LabelEncoder()
dataset_train["section"]=labelen.fit_transform(dataset_train.iloc[:,3])

features=pd.DataFrame(dataset_train.iloc[:,[1,3]])



from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0,1])
features = onehotencoder.fit_transform(features.iloc[:,0:2]).toarray()



faetures2=np.array(features2)

features3=np.append(features2,features,axis=1)


labels= dataset_train.iloc[:,0:1]



#Traing test split
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features3, labels, test_size=0.2, random_state=0) 



from sklearn.ensemble import RandomForestClassifier

Classifier = RandomForestClassifier(n_estimators=125, random_state=0)  
Classifier.fit(features_test, labels_test)  

labels_pred = Classifier.predict(features_test)  




"""-_______________________________________________test____________________________________________________"""




corpus1 = []


for i in range(0, 15370):
    review10 = re.sub('[^a-zA-Z]', ' ', dataset_test['heading'][i])
    review10 = review10.lower()
    review10 = review10.split()
    review10 = [word for word in review10 if not word in set(stopwords.words('english'))]
    
    ps = PorterStemmer()
    review10 = [ps.stem(word) for word in review10]
    review10 = ' '.join(review10)
    corpus1.append(review10)
    
from sklearn.feature_extraction.text import CountVectorizer
cv2 = CountVectorizer(max_features = 1500)
features10 = cv2.fit_transform(corpus1).toarray()
features10= pd.DataFrame(features10)


dataset_test["city"]=labelen.fit_transform(dataset_test.iloc[:,0])

dataset_test["section"]=labelen.fit_transform(dataset_test.iloc[:,2])

features11=pd.DataFrame(dataset_test.iloc[:,[0,2]])



from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0,1])
features12 = onehotencoder.fit_transform(features11.iloc[:,0:2]).toarray()

faetures12=np.array(features12)

features13=np.append(features12,features2,axis=1)


labels= dataset_train.iloc[:,0:1]


a=Classifier.predict(features13)


b=a.value_counts()
print(b.head(5))













