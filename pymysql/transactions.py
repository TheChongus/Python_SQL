'''
This file demonstrates how to use transactions in pymysql.
Transactions are used to ensure that all queries in a transaction are executed successfully, or none of them are.
'''
import pymysql
from config import DB_CONFIG

#Establish our connection:
conn = pymysql.connect(**DB_CONFIG)

try:
    #create a cursor object to execute queries:
    cursor = conn.cursor()

    #start a transaction:
    conn.begin()

    #define your SQL query with placeholders instead of the values:
    cursor.execute("""UPDATE users_test_table SET email = 'Test@fullyaccountable.com' WHERE id = 1;""")
    cursor.execute("""UPDATE failure_test_table SET email = 'thiswillfail@fully.com' WHERE id = 200;""")    

    #commit the changes to the database:
    conn.commit()

    #close the cursor:
    cursor.close()

except Exception as e:
    #Rollback the transaction if there is an error:
    conn.rollback()
    print("An error was encountered, rolling back the transaction.")
    print(e)

finally:
    #close the connection:
    conn.close()