'''This file demonstrates how to create a connection to a MySQL database using pymysql.
It inserts a single row into the users_test_table table using a prepared statement.
'''

import pymysql
from config import DB_CONFIG

#Establish our connection:
conn = pymysql.connect(**DB_CONFIG)

#create a cursor object to execute queries:
cursor = conn.cursor()

#define your SQL query with placeholders instead of the values:
query = """Insert into users_test_table 
                       (first_name, last_name, phone, email, address, postalZip, country)
                       values (%s, %s, %s, %s, %s, %s, %s);"""

#specify the values to insert into the query:
values = ('John', 'Smith', 'jsmith@fullyaccountable.com', '1-234-330-1234', '123 Main St', '12345', 'USA')

#execute the query with the values:
cursor.execute(query, values)

#commit the changes to the database:
conn.commit()

#close the cursor:
cursor.close()

#close the connection:
conn.close()