import sys, sqlite3, json

company_db_file = 'company_data.db'

# Connect to the DB
conn = sqlite3.connect(company_db_file)
c = conn.cursor()

# Count and print stock numbers for product id
for arg in sys.argv[1:]:
    # print("-------xxx-----")
    # print arg
    # print("-------xxx-----")
    input_json = json.loads(arg)
    # print("------------")
    # print ("SELECT amount FROM product WHERE id = " + str(input_json['productId']))
    # print("------------")
    c.execute("SELECT amount FROM product WHERE id = " + str(input_json['productId']))
    sys.stdout.write(str(c.fetchall())+ "\n")

conn.commit()
conn.close()
