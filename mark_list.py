import mysql.connector
marks = mysql.connector.connect(host = 'localhost',
                        user = 'root',
                        password = '',
                        database = 'college')
cursor = marks.cursor()
cursor.execute('''CREATE TABLE BOOK (
             ID INT PRIMARY KEY,
             NAME VARCHAR(30),
             MAT INT,
             PHY INT,
             CHE INT,
             TOTAL_MARKS INT,
             GRADE VARCHAR(1)
)
''')

cursor.execute("INSERT INTO BOOK (ID,NAME,MAT,PHY,CHE,TOTAL_MARKS,GRADE) VALUES (1,'AKANKSHA',98,97,99,294,'A');")
cursor.execute("INSERT INTO BOOK (ID,NAME,MAT,PHY,CHE,TOTAL_MARKS,GRADE) VALUES (2,'SWETHA',99,94,96,289,'A');")
cursor.execute("INSERT INTO BOOK (ID,NAME,MAT,PHY,CHE,TOTAL_MARKS,GRADE) VALUES (3,'LATHA',90,92,91,273,'B')")

marks.commit()
cursor.execute('SELECT ID,NAME,MAT,PHY,CHE,TOTAL_MARKS,GRADE FROM BOOK')
row = cursor.fetchall()

for i in row :
    print('ID = ',i[0])
    print('NAME = ',i[1])
    print('MAT = ',i[2])
    print('PHY = ',i[3])
    print('CHE = ',i[4])
    print('TOTAL_MARKS = ',i[5])
    print('GRADE = ',i[6],'\n') 

cursor.close()