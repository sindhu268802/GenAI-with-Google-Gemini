import sqlite3

## Connect to SQLite database
connection = sqlite3.connect('student.db')

# Create a cursor object to record,create,table,retrieve
cursor=connection.cursor()

# Create a table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Sindhu','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Arun','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('John','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Deepa','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Priya','DEVOPS','A',35)''')

## Display All the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()