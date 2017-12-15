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

def select_all_items(conn):
    # """
    # This is a sample function to get all items from the product_info table
    # Query all rows in the product table
    # :param conn: the Connection object
    # :return:
    # """
    cur = conn.cursor()
    cur.execute("SELECT * FROM product")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def queryDb(conn, query, query_vals): #Main function to query the database, all user inputs gets queried via this function
    try:
        print (query, query_vals)
        cur = conn.cursor()
        cur.execute(query, query_vals)
        # cur.execute("SELECT amount FROM `product` WHERE id=?", (1,)) #sample query
        rows = cur.fetchall()
        print rows
        # for row in rows:          #If there's more that one row then the results can be printed using a for loop
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
        print type(json.loads(sys.argv[1]))
        print "+++++++++++"

        key_count = 0 #Used as a counter if there are multiple items in the dictionary/json
        #Base SQL query
        base_query = "SELECT amount FROM product WHERE "
        # e_q = ()
        # query_values = list(e_q)
        query_values = ()
        
        try:
            if(type (json.loads(sys.argv[1])) is dict):
                user_input = json.loads(sys.argv[1]) #converts input string to dictionary
                for key in user_input:
                   print "key: %s , value: %s" % (key, user_input[key])
                   print key_count
                   if(key_count < 1):
                       base_query += str(key)+"=?"
                       query_values += (user_input[key],)
                       key_count +=1
                   else:
                       base_query += " AND "+str(key)+"=?"
                       query_values += (user_input[key],)

                # query_vals = tuple(query_values)
                # Call queryDb() function with required parameters to execute the query
                queryDb(conn, base_query, query_values)
            else:
                print "Oops, invalid input"
                exit()
        except:
            print "Oops, Invalid input. Please check."
            exit()


if __name__ == '__main__':
    # Main function, the program execution starts here
    main()


# "{\"id\":\"1\"}"
