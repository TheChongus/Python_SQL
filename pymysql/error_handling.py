import pymysql
from config import DB_CONFIG

try:
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM THIS_TABLE_DOESNT_EXIST;""")

except pymysql.Error as e:
    print("Error", e)
    #We aren't using rollback() here because we didn't make any changes to the database, we only requested data from it.
    #you can also log the error or take other actions here


finally:
    cursor.close()
    conn.close()
