import mysql.connector
conn = mysql.connector.connect(host = 'localhost',
                       user = 'root',
                       password = '',
                       database = 'school')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENTS
               (ID INT PRIMARY KEY ,
               NAME VARCHAR(20),
               CLASS VARCHAR(2),
               MARKS INT,
               GRADE VARCHAR(1)
)
''')

cursor.execute("INSERT INTO STUDENTS (ID,NAME,CLASS,MARKS,GRADE) VALUES (11,'AKANKSHA','12',979,'A')")
cursor.execute("INSERT INTO STUDENTS (ID,NAME,CLASS,MARKS,GRADE) VALUES (12,'ANJALI','12',975,'B')")

conn.commit()

cursor.execute('SELECT ID,NAME,CLASS,MARKS,GRADE FROM STUDENTS')
row = cursor.fetchall()

for i in row:
    print(i)
    print('ID = ',i[0])
    print('NAME = ',i[1])
    print('CLASS = ',i[2])
    print('MARKS = ',i[3])
    print('GRADE = ',i[4],'\n')

cursor.close()