import mysql.connector
import config
import datetime

db = mysql.connector.connect(
    host = config.host,
    user = config.user,
    password = config.pw,
    database = config.db
)

ct = datetime.datetime.now()

mycursor = db.cursor()

sql = "INSERT INTO customers (name, address, timestamp) VALUES (%s, %s, %s)"
val = ("Ashley", "456 Main Street", ct)
mycursor.execute(sql, val)

db.commit()



