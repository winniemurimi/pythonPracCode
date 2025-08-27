import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='',
    password='',
    database=''
)
cursor = connection.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
)
''')

# Insert data into the table
cursor.execute('INSERT INTO users (name, age) VALUES (%s, %s)', ('Nat', 30))
cursor.execute('INSERT INTO users (name, age) VALUES (%s, %s)', ('Bright', 25))

# Commit the changes
connection.commit()

# Retrieve data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
cursor.close()
connection.close()