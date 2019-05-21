"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""

import pandas as pd
import numpy as np
df= pd.read_csv('Automobile.csv')

df['price'] = df['price'].fillna(round(df['price'].mean()))

arr= np.array(df['price'])
 
mean= np.mean(arr)
min1= np.min(arr)
min1= np.max(arr)
sd= np.std(arr)
