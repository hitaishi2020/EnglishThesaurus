import pyodbc

server = 'DESKTOP-1183CAQ\MSSQLSERVER01'
database = 'PracticeWork'
connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server='+server+';Database='+database+';Trusted_Connection=yes;')
cursor = connection.cursor()
user_input = input("Enter a word: ")
cursor.execute("Select * from Dictionary Where Expression ='%s'" %user_input)


if 1: 
    for row in cursor:
        print(row)
else:
    print("No word found!")