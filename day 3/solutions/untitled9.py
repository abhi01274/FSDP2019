
"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""

str1= input("enter the comma saperated nos")
str1=str1.split(",")
list1=[]

for item in str1:
    if item not in list1:
        list1.append(item)
    else:
        continue
list1=list1[::-1]
print(list1)