"""
Q2. Code Challenge (Connecting Hearts)


Downlaod Link: http://openedx.forsk.in/c4x/Manipal_University/FL007/asset/Resource.zip

What influences love at first sight? (Or, at least, love in the first four minutes?)this dataset was compiled
 by Columbia Business School Professors Ray Fisman and Sheena Iyengar for their paper Gender Differences in
  Mate Selection: Evidence from a Speed Dating Experiment.
Data was gathered from participants in experimental speed dating events from 2002-2004. During the events, 
the attendees would have a four minute "first date" with every other participant of the opposite sex. At the
 end of their four minutes, participants were asked if they would like to see their date again.

They were also asked to rate their date on six attributes: Attractiveness, Sincerity, Intelligence, Fun, 
Ambition, and Shared Interests.

The dataset also includes questionnaire data gathered from participants at different points in the process.

These fields include: demographics, dating habits, self-perception across key attributes, beliefs on what
 others find valuable in a mate, and lifestyle information.

See the Key document attached for details of every column and for the survey details.


What does a person look for in a partner? (both male and female)

 
For example: being funny is more important for women than man in selecting a partner! Being sincere on the
 other hand is more important to men than women.

What does a person think that their partner would look for in them? Do you think what a man thinks a
woman wants from them matches to what women really wants in them or vice versa. TIP: If it doesn’t then 
it will be one sided :)

Plot Graphs for:
        How often do they go out (not necessarily on dates)?
        In which activities are they interested?
    
  If the partner is from the same race are they more keen to go for a date?
  What are the least desirable attributes in a male partner? Does this differ for female partners?
  How important do people think attractiveness is in potential mate selection vs. its real impact?
"""
import pandas as pd

dataset=pd.read_csv("Dating_Data.csv")
  
  
dataset1=dataset[dataset["gender"]==0]

features1=dataset1[["attr1_1","sinc1_1","intel1_1","fun1_1","amb1_1","shar1_1"]].dropna()


a1= features1.iloc[:,0].sum()
a2= features1.iloc[:,1].sum()
a3= features1.iloc[:,2].sum()
a4= features1.iloc[:,3].sum()
a5= features1.iloc[:,4].sum()
a6= features1.iloc[:,5].sum()

list1=[a1,a2,a3,a4,a5,a6]

import matplotlib.pyplot as plt


lables1= ["attr","sinc","intell","fun1","amb1","shar"]

plt.pie(list1, labels=lables1, autopct="%1.1f%%" )
  
  
#**************************************************************************88

dataset2=dataset[dataset["gender"]==1]

features2=dataset2[["attr1_1","sinc1_1","intel1_1","fun1_1","amb1_1","shar1_1"]].dropna()


aa1= features2.iloc[:,0].sum()
aa2= features2.iloc[:,1].sum()
aa3= features2.iloc[:,2].sum()
aa4= features2.iloc[:,3].sum()
aa5= features2.iloc[:,4].sum()
aa6= features2.iloc[:,5].sum()

list2=[aa1,aa2,aa3,aa4,aa5,aa6]

import matplotlib.pyplot as plt

lables1= ["attr","sinc","intell","fun1","amb1","shar"]

plt.pie(list2, labels=lables1, autopct="%1.1f%%" )
  
  
#*******************************************************************************  


dataset3=dataset[dataset["gender"]==1]

features3=dataset3[["attr3_s","sinc3_s","intel3_s","fun3_s","amb3_s"]].dropna()


aaa1= features3.iloc[:,0].sum()
aaa2= features3.iloc[:,1].sum()
aaa3= features3.iloc[:,2].sum()
aaa4= features3.iloc[:,3].sum()
aaa5= features3.iloc[:,4].sum()
list3=[aaa1,aaa2,aaa3,aaa4,aaa5]

lables3= ["attr","sinc","intell","fun1","amb1"]

plt.pie(list3, labels=lables3, autopct="%1.1f%%" )
  
#***************************************************************************\


dataset4=dataset[dataset["gender"]==0]

features4=dataset4[["attr3_s","sinc3_s","intel3_s","fun3_s","amb3_s"]].dropna()


aaa1= features4.iloc[:,0].sum()
aaa2= features4.iloc[:,1].sum()
aaa3= features4.iloc[:,2].sum()
aaa4= features4.iloc[:,3].sum()
aaa5= features4.iloc[:,4].sum()
list3=[aaa1,aaa2,aaa3,aaa4,aaa5]

lables3= ["attr","sinc","intell","fun1","amb1"]

plt.pie(list3, labels=lables3, autopct="%1.1f%%" )


#****************************************************************************

