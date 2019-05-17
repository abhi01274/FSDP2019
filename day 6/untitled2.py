# -*- coding: utf-8 -*-
"""
Code Challenge
  Filename: 
    map2.py
  Problem Statement:

names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print (names)



(Hopefully, the secret agents will have good memories and won’t forget each other’s secret code names during the secret mission.)


Rewrite the above code using map.
    

"""


inp= input("netr the names")
inp=inp.split()
names = ['Mary', 'Isla', 'Sam']

a=map(hash,names)
print(list(a))