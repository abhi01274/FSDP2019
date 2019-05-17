"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""

import sqlite3
from pandas import DataFrame

# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'db_University.db' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE students(
          Student_Name TEXT,
          Student_Age  INTEGER,
          Student_rollno INTEGER,
          Branch TEXT
          )""")


# STEP 2
c.execute("INSERT INTO Students VALUES ('Sylvester Fernandes',22, 01,'CSE')")
c.execute("INSERT INTO Students VALUES ('Abhishek garg',19, 02,'CSE')")
c.execute("INSERT INTO Students VALUES ('prajjawal',20, 03,'IT')")
c.execute("INSERT INTO Students VALUES ('Mukul Gaur',22, 04,'IT')")
c.execute("INSERT INTO Students VALUES ('Tarun',22, 01,'ECE')")




# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM students")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Name","age","roll_no","Brach"]


# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()



#_________________________________________________________________________





