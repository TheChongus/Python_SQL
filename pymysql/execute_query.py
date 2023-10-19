'''
This file demonstrates how to create a connection to a MySQL database using pymysql.
It is best to store the credentials in a separate file and import them into your script.
'''
import pymysql # <--import the package
from config import DB_CONFIG # <--import the credentials (.. means go up one level)

#ALTERNATIVE:
conn = pymysql.connect(host=DB_CONFIG['host'], 
                              user=DB_CONFIG['user'],
                              password=DB_CONFIG['password'],
                              database=DB_CONFIG['database']) # <--use the credentials as variables

#STANDARD QUERY, RESULTS COME BACK AS A TUPLE OF TUPLES:
cursor = conn.cursor() # <--create a cursor object to execute queries
cursor.execute('SELECT * FROM users_test_table;') # <--execute a query
result = cursor.fetchall() # <--fetch the results of the query


cursor.close() # <--close the cursor
print("-------------------")
print("Results as a tuple of tuples:")
print(result) # <--print the results


#TUPLE OF TUPLES IS NOT VERY USEFUL, SO LET'S CONVERT IT TO A LIST OF DICTIONARIES:
cursor = conn.cursor(pymysql.cursors.DictCursor) # <--create a cursor object to execute queries
cursor.execute('SELECT * FROM users_test_table') # <--execute a query
result = cursor.fetchall() # <--fetch the results of the query
dict_result = cursor.fetchall()


cursor.close() # <--close the cursor
print("-------------------")
print("Results as a list of dictionaries:")
print(result) # <--print the results

#Now we can iterate over the list of dictionaries:
print("-------------------")
for row in result:
    print(row['first_name']) # <--print the first name from each row


#Return a single row:
cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute('SELECT * FROM users_test_table WHERE id = 1;')
result = cursor.fetchone() # <--fetch a single row
cursor.close()

#Return a single value:
print("-------------------")
print("Single value:")
print(result)