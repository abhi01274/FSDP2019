"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""

from bs4 import BeautifulSoup
import requests
#import urllib



#specify the url
ranks = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(ranks).text

soup = BeautifulSoup(source,"lxml")

print (soup.prettify())

all_tables=soup.find_all('table')

right_table=soup.find('table', class_='table')

tb= right_table.find('tbody')
#Generate lists
A=[]
B=[]
C=[]
D=[]

for row in tb.findAll('tr'):
    cells = row.findAll('td')
    teams = row.findAll('td')
    A.append(teams[0].text.strip())
    B.append(cells[1].text.strip())
    C.append(cells[2].text.strip())
    D.append(cells[3].text.strip())
       
import pandas as pd
from collections import OrderedDict

col_name = ["Ranks","Team","Weighted matches","points","rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")