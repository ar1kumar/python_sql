import mysql.connector

# Connection configuration
db_config = {
    'user' : 'root',
    'password' :'its@tr@p',
    'host' : 'localhost',
    'database' : 'company_data'
}
# Python Connection function
cnx = mysql.connector.connect(**db_config)
# connection variable
cursor = cnx.cursor(buffered=True)
