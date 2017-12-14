import sqlite3
from sqlite3 import Error
import sys
import json
import ast


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def select_all_items(conn):
    """
    This is a sample function to get all items from the product_info table
    Query all rows in the product table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM product_info")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def queryDb(conn, base_query): #Main function to query the database, all user inputs gets queried via this function
    try:
        # print conn.cursor().execute(base_query)
        cur = conn.cursor()
        cur.execute(base_query)
        # cur.execute('''SELECT sqlite_version()''') #Check database version
        # print cur
        rows = cur.fetchall()
        print rows
        # for row in rows:
        #     print(row)
    except Error as e:
        #Handle exception here
        #Print error message
        print(e)

def main():
    database = "db/company_data.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        #Connection established, Query Database based on user Input
        print sys.argv[1]
        print "+++++++++++"
        #Base SQL query
        base_query = "SELECT count(*) FROM product_info WHERE "
        key_count = 0 #Used as a counter if there are multiple items in the dictionary/json
        try:
            if(type (json.loads(sys.argv[1])) is dict):
                user_input = json.loads(sys.argv[1]) #converts input string to dictionary
                for key in user_input:
                   # print "key: %s , value: %s" % (key, user_input[key])
                   if(key_count < 1):
                       base_query += str(key)+"='"+str(user_input[key])+"'"
                       key_count +=1
                   else:
                       base_query += " AND "+str(key)+"='"+str(user_input[key])+"'"
                print "+++++++++++++++"
                print base_query;
                queryDb(conn, base_query)
            else:
                print "Oops, invalid input"
                exit()
        except:
            print "Oops, Invalid input. Please check."
            exit()


if __name__ == '__main__':
    main()



# Code Exploits
# 1. python count.py "{\"productId\":\"1' OR productId = '2\"}"
