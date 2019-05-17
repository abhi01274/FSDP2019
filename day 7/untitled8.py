"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
   
    compact=ultra&apiKey=f45f0f5ec708b8c8fa1a
    
    
"""

import requests
entry = int(input("enter the no"))
url1 = "https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=f45f0f5ec708b8c8fa1a"
response = requests.get(url1)
response.content
res1= response.json()

print("the value is >>" , res1["USD_PHP"]*entry)