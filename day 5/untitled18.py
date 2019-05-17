"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""

import re

entry= input("entr the string>>")

try:
    result= re.match(r'[+-]{1}*[+-]{1}\d{1,}*\d{1,}.\d{1,}',entry)
    print(result)
except Exception as e:
    print(e)
