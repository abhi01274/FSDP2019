

"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""
dict1= {"a": 0, "b":0, "c": 0}

print("enter the values for>>")
a= int(input("a"))
b= int(input("b"))
c= int(input("c"))

dict1['a']= a
dict1['b']= b
dict1['c']= c
sum1=0

for val in dict1.values():
    if val == (15 or 16):
        sum1=sum1+val
    elif val in range(13,20):
        continue
    else:
        sum1=sum1+val
print("your sum is ",sum1)
