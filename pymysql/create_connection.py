'''
This file demonstrates how to create a connection to a MySQL database using pymysql.
It is best to store the credentials in a separate file and import them into your script.
'''
import pymysql # <--import the package
from config import DB_CONFIG # <--import the credentials (.. means go up one level)


#Establish a connection to the database:
connection = pymysql.connect(**DB_CONFIG) # <--use the credentials as imported

#ALTERNATIVE:
connection2 = pymysql.connect(host=DB_CONFIG['host'], 
                              user=DB_CONFIG['user'],
                              password=DB_CONFIG['password'],
                              database=DB_CONFIG['database']) # <--use the credentials as variables

