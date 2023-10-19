import pandas as pd #import the pandas library
from sqlalchemy import create_engine #To create a connection to a database
from config import DB_CONFIG #To import the database configuration

#Create a DataFrame from a dictionary:
data = {'name': ['John', 'Jane', 'Joe', 'Janet'], 'age': [34, 28, 51, 43]}
df = pd.DataFrame(data, columns=['name', 'age'])

#create an engine that connects to mysql using the configuration in config.py: engine
engine = create_engine("mysql://%s:%s@%s/%s" % (DB_CONFIG['user'], DB_CONFIG['password'], DB_CONFIG['host'], DB_CONFIG['database']))

#Write the DataFrame to a database table:
table_name = 'cool_table_name'
df.to_sql(table_name, engine, if_exists='replace', index=False) 
#if_exists='replace' means that if the table already exists, it will be overwritten
#index=False means that the DataFrame index will not be written to the table
#Note: The table will be created if it does not exist