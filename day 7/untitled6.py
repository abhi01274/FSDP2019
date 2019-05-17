"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
import json

json_student = """
{
    "Student": [{
        "name": "Mukul gaur",
        "age": 21,
        "college": "jecec"
           },
    {
         "name": "Abhishek garg",
         "age": 20,
         "college": "jecec"
    },
    {
         "name": "prajjawal kansal",
         "age": 22,
         "college": "jecec"
    }
]
}
"""
j_son_teacher= """
{
     "teachers": [{
         "fname":"yogendra",
         "lname":"Singh",
         "photo": "null",
         "department": "IT developer sector",
         "contact details" : [ {
                                 "mobile no" : 67889878,
                                 "email" : svhj@hgysd.chy
                                 "facebook" : "https://www.facebook.com/yogendra.singh.927758"
                             }]
     },
    {
         "fname":"Sylvester",
         "lname":"Fernandez",
         "photo" : "null",
         "department": "CSE",
         "contact details" : [ {
                                 "mobile no" : 67889875432,
                                 "email" : svhj@hgysd.chy
                                 "facebook" : "https://www.facebook.com/yogendra.singh.927758"
                             }]
    },
    {
         "fname":"Ashutosh ",
         "lname" : "singh",
         "photo" : "null",
         "department": "Mechanical",
         "contact details" : [ {
                                 "mobile no" :3467889878,
                                 "email" : svhj@hgysd.chy
                                 "facebook" : "https://www.facebook.com/yogendra.singh.927758"
                             }]
     }]
}


"""

jf1= json.dumps(json_student)
jf2= json.dumps(j_son_teacher)

with open("stud1.json","w") as file1:
    json.dump(json_student,file1)
with open("teac.json","w") as file2:
    json.dump(j_son_teacher,file2)
    