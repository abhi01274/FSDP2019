
"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""


dic={'digit': 0, 'letter':0, 'space':0}
letter="qwertyuiopasdfghjklzxcvbnm"
digits="1234567890"
str1=input("enter ur string")
for item in str1:
    if item in letter:
        dic['letter']=dic['letter']+1
    elif item in digits:
        dic['digit']= dic['digit']+1
    else:
        dic['space']=dic['space']+1
print(dic)