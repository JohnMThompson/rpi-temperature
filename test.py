import mysql.connector
import config
import datetime
import time
import board
import adafruit_dht

db = mysql.connector.connect(
    host = config.host,
    user = config.user,
    password = config.pw,
    database = config.db
)

mycursor = db.cursor()
dhtDevice = adafruit_dht.DHT22(board.D4)
room = "Cozy Office"

while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        ct = datetime.datetime.now()
        sql = "INSERT INTO `temperature-sensor` (timestamp, room, temperature_f, humidity) VALUES (%s, %s, %s, %s)"
        val = (ct, room, temperature_f, humidity)
        mycursor.execute(sql, val)

        db.commit()

    except RuntimeError as error:
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(60)
