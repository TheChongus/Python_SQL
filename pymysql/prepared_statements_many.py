'''This file demonstrates how to use executemany() to insert multiple rows into a MySQL database using pymysql.
It inserts multiple rows into the users_test_table table using a prepared statement.
'''
import pymysql
from config import DB_CONFIG


#specify the values to insert into the query:
#IMPORTANT: values must be a LIST of TUPLES, even if there is only one tuple:
values = [
          ('John', 'Smith', 'jsmith@fullyaccountable.com', '1-234-330-1234', '123 Main St', '12345', 'USA'),
          ('Jane', 'Doe', 'jdoe@fullyaccountable.com', '1-234-330-1234', '123 Main St', '12345', 'USA'),
          ('Bob', 'Jones', 'Bjones@fullyaccountable.com', '1-234-330-1234', '123 Main St', '12345', 'USA'),
           ('Sally', 'Smith', 'Ssmith@fullyaccountable.com', '1-234-330-1234', '123 Main St', '12345', 'USA')
            ]


#Establish our connection:
conn = pymysql.connect(**DB_CONFIG)

#create a cursor object to execute queries:
cursor = conn.cursor()

#define your SQL query with placeholders instead of the values:
query = """Insert into users_test_table 
                       (first_name, last_name, email, phone, address, postalZip, country)
                       values (%s, %s, %s, %s, %s, %s, %s);"""

#execute the query with the values:
cursor.executemany(query, values)

#commit the changes to the database:
conn.commit()

#close the cursor:
cursor.close()

#close the connection:
conn.close()

