import mysql.connector
details = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'office'
)
cursor = details.cursor()

cursor.execute('''CREATE TABLE RESUME
                (ID INT PRIMARY KEY,
                NAME VARCHAR(20),
                ADDRESS VARCHAR(50),
                JOB VARCHAR(20),
                SALARY INT
)
''')

cursor.execute("INSERT INTO RESUME (ID,NAME,ADDRESS,JOB,SALARY) VALUES (11,'AKANKSHA','PULIVENDULA','AI_DEVELOPER',100000);")
cursor.execute("INSERT INTO RESUME (ID,NAME,ADDRESS,JOB,SALARY) VALUES (12,'SWETHA','KADAPA','DATA_SCIENTIST',90000);")
cursor.execute("INSERT INTO RESUME (ID,NAME,ADDRESS,JOB,SALARY) VALUES (13,'JYOTHI','HYDERABAD','DATA_ANALYIST',120000);")
cursor.execute("INSERT INTO RESUME (ID,NAME,ADDRESS,JOB,SALARY) VALUES (14,'RAM','BANGLORE','PYTHON_DEVELOPER',115000)")

details.commit()
cursor.execute('SELECT ID,NAME,ADDRESS,JOB,SALARY FROM RESUME')
rows = cursor.fetchall()

for r in rows:
    print('ID = ',r[0])
    print('NAME = ',r[1])
    print('ADDRESS = ',r[2])
    print('JOB = ',r[3])
    print('SALARY = ',r[4])

cursor.close()
details.close()