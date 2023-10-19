import pandas as pd #import the pandas library
from sqlalchemy import create_engine #To create a connection to a database
from config import DB_CONFIG #To import the database configuration

#Create a database engine:
engine = create_engine("mysql://%s:%s@%s/%s" % (DB_CONFIG['user'], DB_CONFIG['password'], DB_CONFIG['host'], DB_CONFIG['database']))


#Read data from a table into a DataFrame:
query = 'Select * from orders_test_table;'
df = pd.read_sql_query(query, engine)

#Perform some data manipulation with Pandas:
df['total'] = df['quantity'] * df['unit_price']

#Write the DataFrame to a different table:
table_name = 'fake_order_totals_table'
df.to_sql(table_name, engine, if_exists='append', index=False)
#Note: The table will be created if it does not exist
#Note: if_exists='append' means that if the table already exists, the data will be appended to the table
#Note: index=False means that the DataFrame index will not be written to the table
