'''
SQLAlchemy is well-optimized for database interactions, 
while Pandas is optimized for in-memory data manipulation. 
By using both tools together, you can benefit from the best of both worlds: 
efficient database operations and flexible data manipulation.

In summary, SQLAlchemy and Pandas complement each other in a data analysis workflow. 
SQLAlchemy helps fetch and store data in a relational database, 
while Pandas is excellent for data transformation, analysis, and preparation.
'''
'''
install pandas
'pip install pandas'
'''
# import pandas
import pandas as pd
from sqlalchemy import create_engine #To create a connection to a database
from config import DB_CONFIG #To import the database configuration

# Create an engine that connects to mysql using the configuration in config.py: engine
engine = create_engine("mysql://%s:%s@%s/%s" % (DB_CONFIG['user'], DB_CONFIG['password'], DB_CONFIG['host'], DB_CONFIG['database']))

#Read data from a table into a DataFrame:
query = 'SELECT * FROM orders_test_table;'
df = pd.read_sql_query(query, engine)

#Print the head of the DataFrame:
print(df.head())

#Close the connection:
engine.dispose()

