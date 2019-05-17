"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.

"""

import pymongo
#import dns # required for connecting with SR

client = pymongo.MongoClient("mongodb://abhishek01274:Abhishek%40123@cluster0-shard-00-00-vr8zm.mongodb.net:27017,cluster0-shard-00-01-vr8zm.mongodb.net:27017,cluster0-shard-00-02-vr8zm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")


mydb = client.abhishek_db

def add_Stud(name, age, roll_no, branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.abhishek_coll2.insert_one(
            {
            "name" : name,
            "Age" : age,
            "roll_no" : roll_no,
            "branch" : branch
            })
    return "Employee added successfully"


def fetch_all_students():
    user = mydb.abhishek_coll2.find()
    for i in user:
        print (i)




add_Stud('abhishek', 18, 1,'cse')
add_Stud('prajjawal', 19, 2,'It')
add_Stud('Mukul', 20,3,'it')
add_Stud('tarun',20,4,'it')

fetch_all_students()