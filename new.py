import mysql.connector

connection = mysql.connector.connect(host="localhost",
                                     user= 'root',
                                     password='',
                                     database='test.db')

cursor = connection.cursor()

cursor.execute('create a table employe details')
cursor.execute('''(
               ID INT PRIMARY KEY NOT NULL,
               NAME           TEXT NOT NULL,
               AGE            INT NOT NULL,
               ADDRESS        CHAR(50),
               JOB            TETX,
               SALARY         REAL);''')

cursor.execute('INSERT INTO EMPLOYE DETAIL(ID,NAME,AGE,ADDRESS,JOB,SALARY) VALUES (1,AKANKSHA,18,HYDERABAD,AI DEVELOPER,500000)')
connection.commit()

cursor.execute('SELECT ID,NAME,AGE,ADDRESS,JOB,SALARY FROM EMPLOYE DETAILS')

rows = cursor.fetchall()
for row in rows :
    print(row)

cursor.close()
connection.close