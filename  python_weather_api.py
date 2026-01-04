import os
from dotenv import load_dotenv
from urllib.request import urlopen
from urllib.parse import urlencode
import ssl
import json
import sqlite3
from datetime import datetime, UTC

load_dotenv()

conn = sqlite3.connect('weather.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS WEATHER (City TEXT,Temp INTEGER,
            Weather_condition TEXT,Humidity INTEGER,Sunrise TEXT,Sunset TEXT) ''')

def format_timestamp(ts) :

    try:
        dt = datetime.fromtimestamp(ts,UTC)
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    
    except :
         return "Invalid Timestamp"
    


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


baseurl = 'https://api.openweathermap.org/data/2.5/weather?'


while True :
    address = input('Enter your address - ')
    if address.lower() == 'break' or address.lower() == "" :
        break

    cur.execute(''' SELECT Temp FROM WEATHER WHERE City = ?''',(address,))
    
    try :
        row = cur.fetchone()[0]
        print(f'Found in Databse,"{address}"')
        continue

    except :
        pass

    parameter = {}
    parameter['q'] = address
    parameter['appid'] = os.getenv('OPENWEATHER_API_KEY')

    url = baseurl + urlencode(parameter)
    print(f'URL YOU RETRIEVED : {url}')
    
    try :
        html = urlopen(url,timeout=30, context=ctx)
        data = html.read().decode()

    except :
        print('Data not found')
        continue
    # print(data)
    # print(type(data)

    try :
        js = json.loads(data)
        # print(json.dumps(js,indent=4))

    except :
        print('Error Decoding JSON')


    try :

        main = js.get('main')
        sys = js.get('sys')
        weather_data = js.get('weather')[0]

    except :
        print('Unexcepted format')
        print(js)
        print()

    if not js or  'main' not in js :
        print('=== Download error ===')
        continue

    if len(js['main']) == 0 :
        print('=== Object not found ===')
        continue

    temp = main.get('temp')
    weather_condition = weather_data.get('description')
    humidity = main.get('humidity')
    sunrise = sys.get('sunrise')
    try :
        sunrise = format_timestamp(sunrise)

    except :
        print(f'Fail to parse sunrise : {sunrise}')


    sunset = sys.get('sunset')
    try :
        sunset = format_timestamp(sunset)

    except :
        print(f'Fail to parse sunset : {sunset}')


    
    cur.execute(''' INSERT OR IGNORE INTO WEATHER (City,Temp,Weather_condition,Humidity,Sunrise,Sunset) VALUES (?,?,?,?,?,?)''',
                (address,temp,weather_condition,humidity,sunrise,sunset))
    conn.commit()


    print(f'You address - {address}')
    print(f"{address}'s temp - {temp}")
    print(f"{address}'s sunrise - {sunrise}")
    print(f"{address}'s sunset - {sunset}")
    print(f"{address}'s humidity - {humidity}")
    print(f"{address}'s weather condition - {weather_condition}")
    print()