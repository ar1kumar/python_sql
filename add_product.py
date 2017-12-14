from connect import *

add_product = ("INSERT INTO product_info "
               "(product_name, category, supervisor_id) "
               "VALUES (%s, %s, %s)")

data_product = ('Fork', 'Utilities', 1)

# Insert new employee
cursor.execute(add_product, data_product)
emp_no = cursor.lastrowid

# Make sure data is committed to the database
cnx.commit()
# Close the database connection once the operations are finished
cursor.close()
cnx.close()
