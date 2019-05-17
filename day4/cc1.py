# -*- coding: utf-8 -*
"""
Created on Fri May 10 15:55:22 2019

@author: Abhishek
"""

filename1=str(input("write the file name which you want to copy::" ))
filename2=str(input("write the file name of new file::" ))

filename1=open(filename1, mode='r')
filename2=open(filename2,mode='w')

for line in filename1:
    filename2.write(line)
filename1.close()
filename2.close()
    