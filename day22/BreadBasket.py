"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
"""



import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt

dataset = pd.read_csv('BreadBasket_DMS.csv')

dataset["Item"].value_counts()


index= dataset.index[dataset["Item"]== "NONE"].tolist()
dataset.drop(index,axis=0,inplace= True)

x= dataset["Item"].value_counts().head(15)
name=x.index.tolist()
count= x.values.tolist()

plt.pie(count,labels=name)


#---------------------------------------------------------------------


dataset1=dataset[["Transaction","Item"]]
dic={}
list1=[] 
          
mylist=[]

for i, j in dataset1.values:    
    if i in dic:
        dic[i]=dic[i]+' '+j
    else:
        dic[i]=j
for i,j in dic.items():
    list1.append(dic[i])
for i in list1:
    str1=i.split(' ')
    mylist.append(str1)


rules = apriori(mylist, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)
results = list(rules)





for item in results:
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")




#---------------------------------------------------------------------------
    
    
    
for i in results:
    a=i[0]
    b=list(a)
    j=1
    print("associated itemsof ",j,":",b[1:])
    j+=1














