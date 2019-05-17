
"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""


entry= input("enter the days")
entry=entry.split(",")
days= ['sunday','monday' ,'tuesday','wednesday','thursday','friday','saturday']

result= set(entry).union(set(days))
result=set(result)
print(result)