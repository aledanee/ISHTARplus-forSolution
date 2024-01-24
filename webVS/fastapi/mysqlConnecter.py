import MySQLdb

# Database configuration
db_config = {
    'host': 'localhost:3306',
    'user': 'root',
    'passwd': 'morootok',
    'db': 'ishtarblog',
}

# Create a connection to the database
conn = MySQLdb.connect(**db_config)