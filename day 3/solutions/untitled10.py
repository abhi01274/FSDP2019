
"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""


list1= input("enter the 1st comma saperated list")
list1=list1.split(",")
list2= input("enter the 2nd comma saperated list")
list2=list2.split(",")

list1=set(list1)
list2=set(list2)

list1=list1.intersection(list2)
print(list1)