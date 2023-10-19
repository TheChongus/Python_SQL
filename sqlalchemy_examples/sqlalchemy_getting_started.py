'''
To install sqlalchemy:
'pip install sqlalchemy'
'pip install mysqlclient' # To connect to MySQL with sqlalchemy
'''

#In your python script, import the required SQLAlchemy modules:
from sqlalchemy import create_engine, text # To create a connection to a database
from sqlalchemy.orm import sessionmaker # To create a session to a database
import MySQLdb # To connect to MySQL with sqlalchemy
from config import DB_CONFIG

# Create an engine that connects to the census.sqlite file: engine
db_url = "mysql://%s:%s@%s/%s" % (DB_CONFIG['user'], DB_CONFIG['password'], DB_CONFIG['host'], DB_CONFIG['database'])

engine = create_engine(db_url)

# Create a Session:
Session = sessionmaker(bind=engine)
session = Session()

#Define a function to select data from the users_test table:
def get_user_data():
    #Define the SQL query using a text object:
    stmt = text("SELECT * FROM users_test_table")

    #execute the query and store the results in results:
    results = session.execute(stmt).fetchall()

    #print the results:
    for result in results:
        print(result)



#Call the function to get the data:
get_user_data()

#Close the session:
session.close()
