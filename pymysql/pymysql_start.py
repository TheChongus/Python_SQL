'''
To Install pymysql using pip: 

'pip install pymysql'

(Best to use a virtual environment to avoid conflicts with other packages)
'''

#Step 1: - import the package into your python script:
import pymysql


#Step 2: import the credentials for the database you want to connect to:
from config import DB_CONFIG


#Now we can use the credentials as imported or assign them to variables:
host = DB_CONFIG['host']
user = DB_CONFIG['user']
password = DB_CONFIG['password']
database = DB_CONFIG['database']

'''
ALTERNATIVE: 
assign credentials to environment variables and retrieve them from the OS:

Instructions to add environment variables are in the README.md file in the main directory.

If using environment variables, you can retrieve them like this:
import os  <--must import the os package
import pymysql

host = os.environ.get('DB_HOST')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
database = os.environ.get('DB_DATABASE')

'''

