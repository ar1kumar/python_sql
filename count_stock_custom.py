import sqlite3
from sqlite3 import Error
import sys
import json
import ast


def create_connection(db_file):
    # """ create a database connection to the SQLite database
    #     specified by the db_file
    # :db_file: database file
    # :return: Connection object or None
    # """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def queryDb(conn, base_query): #Main function to query the database, all user inputs gets queried via this function
    try:
        cur = conn.cursor()
        cur.execute(base_query)
        # cur.execute('''SELECT sqlite_version()''') #Check database version
        rows = cur.fetchall()
        print rows
        # for row in rows:
        #     print(row)
    except Error as e:
        #Handle exception here
        #Print error message
        print(e)

def main():
    database = "company_data.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        #Connection established, Query Database based on user Input
        print sys.argv[1]
        print "+++++++++++"
        #Base SQL query
        base_query = "SELECT amount FROM product WHERE "
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
