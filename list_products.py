import pprint #pretty prints the output
import sys
import json
from connect import *

# input_data = json.loads(sys.argv[1])
#print sys.argv[1]
print "+++++++++++"

# MySQL query
query = ("SELECT * FROM `product_info`")

query_data = (1,2)

cursor.execute(query)
result = cursor.fetchall()
print "---------"
pprint.pprint(result) 
print "---------"
cursor.close()
cnx.close()
