# import mysql.connector

# # Establish connection
# conn = mysql.connector.connect(
#     host='localhost',      # XAMPP uses localhost
#     user='root',           # Default user is root
#     password='',           # Leave empty unless you set a password
#     database='school'      # Make sure this DB exists in phpMyAdmin
# )

# # Optional: Check if connected
# if conn.is_connected():
#     print("Connected to MySQL database successfully!")



import mysql.connector

# Step 1: Connect
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)

cursor = conn.cursor()

# Step 2: Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS STUDENTS (
        ID INT PRIMARY KEY,
        NAME VARCHAR(20),
        CLASS VARCHAR(2),
        MARKS INT,
        GRADE VARCHAR(1)
    )
''')

# Step 3: Insert data
cursor.execute("INSERT INTO STUDENTS (ID, NAME, CLASS, MARKS, GRADE) VALUES (14, 'AKANKSHA', '12', 979, 'A')")
cursor.execute("INSERT INTO STUDENTS (ID, NAME, CLASS, MARKS, GRADE) VALUES (15, 'ANJALI', '12', 975, 'B')")

conn.commit()

# Step 4: Fetch and print data
cursor.execute("SELECT ID, NAME, CLASS, MARKS, GRADE FROM STUDENTS")
rows = cursor.fetchall()

for row in rows:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("CLASS =", row[2])
    print("MARKS =", row[3])
    print("GRADE =", row[4], "\n")

# Step 5: Cleanup
cursor.close()