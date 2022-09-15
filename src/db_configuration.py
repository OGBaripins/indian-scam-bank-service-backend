import mysql.connector
import sys

# Making connection to DB
try:
    mydb = mysql.connector.connect(
        host="sql11.freesqldatabase.com",
        port="3306",
        user="sql11520035",
        password="WjRaAgGLiL",
        database="sql11520035"
    )
except:
    print("Connection to database was unsuccessful")
    sys.exit()

cur = mydb.cursor(buffered=True, dictionary=True)

cur.execute("SELECT * FROM accounts")

data = cur.fetchall()
print(data)
