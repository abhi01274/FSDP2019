
"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""


import csv

def readlist():
    with open("zoo.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            next(csv_reader)
            print (row)

def list_of_animal():
    list1=[]
    with open("zoo.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            if row[0] not in list1:
                list1.append(row[0])
        print(list1)
        
        
        
        

def waterneed():
    with open("zoo.csv") as csv_file:
        temp=0
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
           
            temp=temp+int(row[2])
        print (temp)
