"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(150.0, 20.0, 1000)

plt.hist(data,100)

print(np.mean(data))
print(np.median(data))