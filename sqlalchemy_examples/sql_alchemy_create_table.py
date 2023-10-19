'''
This is an example of how to create/update table using SQLAlchemy.
'''

from sqlalchemy import create_engine, text, Column, Integer, String #To create a connection to a database and create columns
from sqlalchemy.orm import sessionmaker # To create a session to a database
from sqlalchemy.ext.declarative import declarative_base #To create a base class for the table
import MySQLdb # To connect to MySQL with sqlalchemy
from config import DB_CONFIG

# Create an engine that connects to the census.sqlite file: engine
db_url = "mysql://%s:%s@%s/%s" % (DB_CONFIG['user'], DB_CONFIG['password'], DB_CONFIG['host'], DB_CONFIG['database'])

engine = create_engine(db_url)

# Create a Session:
Session = sessionmaker(bind=engine)
session = Session()

#Create a base class for the table:
Base = declarative_base()

#Create a class for the table:
class Animals(Base):
    __tablename__ = 'animals'
    id = Column(Integer, primary_key=True)
    species = Column(String(255))
    age = Column(String(255))

#Create the table:
Base.metadata.create_all(engine)

#Create an instance of the class:
dog = Animals(species='dog', age='5')

#Add the instance to the session:
session.add(dog)

#Commit the session:
session.commit()

#Query the database:
query = text("SELECT * FROM animals")

#Execute the query and store the results in results:
results = session.execute(query).fetchall()

#print the results:
for result in results:
    print(result)


#Close the session:
session.close()
