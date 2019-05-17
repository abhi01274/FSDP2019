# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:36:54 2019

@author: Abhishek
"""

counter=0
with open("absentee.txt",'wt') as fp:
    while counter<26:
        name=input("entr name of student>>")
        if not name:
            break
        else:
            fp.write(name+"\n")
        counter=counter+1




