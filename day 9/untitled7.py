"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


"""
from bs4 import BeautifulSoup
import requests
from pandas import DataFrame


import sqlite3


ranks = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(ranks).text

soup = BeautifulSoup(source,"lxml")

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




# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'teams1.db' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html



for i in range(0,11):
    c.execute("INSERT INTO teams1 VALUES ('{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i]))

c.execute("select * from teams1")
df = DataFrame(c.fetchall())

conn.commit()


conn.close()


    











