"""

Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.
"""


import pandas as pd
import numpy as np
from apyori import apriori

dataset = pd.read_csv('Market_Basket_Optimisation.csv',header=None)


def cart(items):
    tmp_cart = list(set(items))
    if np.nan in tmp_cart:
        tmp_cart.remove(np.nan)
    return tmp_cart

transactions=list(dataset.apply(cart,axis=1))



rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)
results = list(rules)





for item in results:
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("--------------------------------------")



