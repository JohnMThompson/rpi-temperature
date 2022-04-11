from random import randint
import mysql.connector
import config
import datetime
import time

db = mysql.connector.connect(
    host = config.host,
    user = config.user,
    password = config.pw,
    database = config.db
)

mycursor = db.cursor()

for i in range(10):
    temperature = randint(60,75)
    humidity = randint(50,100)
    room = "Cozy"
    ct = datetime.datetime.now()
    sql = "INSERT INTO `temperature-sensor` (timestamp, room, temperature_f, humidity) VALUES (%s, %s, %s, %s)"
    val = (ct, room, temperature, humidity)
    mycursor.execute(sql, val)

    db.commit()
    time.sleep(5)
