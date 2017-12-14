import sys
import json
import ast
from connect import *

# input_data = json.loads(sys.argv[1])
print sys.argv[1]
print "+++++++++++"

#Base SQL query
base_query = "SELECT * FROM `product_info` WHERE "
key_count = 0
try:
    if(type (json.loads(sys.argv[1])) is dict):
        user_input = json.loads(sys.argv[1]) #converts input string to dictionary
        for key in user_input:
           # print "key: %s , value: %s" % (key, user_input[key])
           if(key_count < 1):
               base_query += "`"+str(key)+"`='"+str(user_input[key])+"'"
               key_count +=1
           else:
               base_query += " AND `"+str(key)+"`='"+str(user_input[key])+"'"
    else:
        print "Oops, invalid input"
        exit()
except:
    print "Oops, Invalid input. Please check."
    exit()

print "+++++++++++++++"
print base_query;

def queryDb():
    # MySQL query
    query = (base_query)

    query_data = (user_input)

    cursor.execute(query)
    result = cursor.fetchall()
    print "---------"
    print result
    print "---------"
    cursor.close()
    cnx.close()

# if(user_input['productId']):
#     queryDb(user_input['productId'])
# else:
#     print "Sorry, Invalid input"

queryDb()
