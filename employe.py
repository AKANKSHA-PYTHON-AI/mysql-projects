import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="company"  # Make sure this DB exists!
)

cursor = conn.cursor()

# Drop and recreate table
cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    employes VARCHAR(300),
    email VARCHAR(255)
)
""")

# Insert data
cursor.execute("INSERT INTO users (name, age,employes,email) VALUES (%s, %s,%s,%s)",
               ("Adi", 29, "Developer", "akumatha@gmail.com"))


conn.commit()

# Fetch and print all rows
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
