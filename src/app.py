from flask import Flask, render_template, send_from_directory, send_file
from flask_socketio import SocketIO, send, emit
from flask_mysqldb import MySQL
import MySQLdb
import botogram

import paho.mqtt.client as mqtt
import requests
import json
from datetime import date, datetime

app = Flask(__name__)
socketio = SocketIO(app)

db = MySQLdb.connect(host="",
                     user="",
                     passwd="",
                     db="")
cur = db.cursor() # query cursor

current_time = ""
current_date = ""
data_list = []

@app.route("/", methods=['GET', 'POST'])
def renderHomepage():
    return render_template("Homepage.html")

@app.route('/bme', methods=['GET', 'POST'])
def renderBme280():
    return render_template('Bme280.html')

@app.route('/sensirion', methods=['GET', 'POST'])
def renderSensirionSPS30():
    return render_template('Sensirion-SPS30.html')

@app.route('/omron', methods=['GET', 'POST'])
def renderOmronB5WLD0101():
    return render_template('Omron-B5W-LD0101.html')

@app.route('/fCSV1', methods=['GET', 'POST'])
def fCSV1():
    cont = 0
    with open('/path_to_csv_directory/Bme.csv','w') as f:
        db.commit()
        cur.execute('SELECT id,date,time,Temperature,Pressure,Humidity FROM ssh_project.data ORDER BY id DESC')
        for result in cur.fetchall():
            cont += 1
            if cont <= 300:
                f.write(str(result[1]) + ',' + str(result[2]) + ',' + str(result[3]) + ',' + str(result[4]) + ',' + str(result[5]) + '\n')
    
    filename="/path_to_csv_directory/Bme.csv"
    return send_file(filename, as_attachment=True)

@app.route('/fJSON1', methods=['GET', 'POST'])
def fJSON1():
    cont = 0
    js = {}
    with open('/path_to_json_directory/Bme.json','w') as f:
        db.commit()
        cur.execute('SELECT id,date,time,Temperature,Pressure,Humidity FROM ssh_project.data ORDER BY id DESC')
        for result in cur.fetchall():
            cont += 1
            if cont <= 300:
                js[cont] = {}
                js[cont]['date'] = str(result[1])
                js[cont]['time'] = str(result[2])
                js[cont]['Temperature'] = float(result[3])
                js[cont]['Pressure'] = float(result[4])
                js[cont]['Humidity'] = float(result[5])
        json.dump(js, f, indent = 6)
        cont = 0
    
    filename="/path_to_json_directory/Bme.json"
    return send_file(filename, as_attachment=True)

@app.route('/fCSV2', methods=['GET', 'POST'])
def fCSV2():
    cont = 0
    with open('/path_to_csv_directory/MassSensirion.csv','w') as f:
        db.commit()
        cur.execute('SELECT id,date,time,mP1_0,mP2_5,mP4_0,mP10 FROM ssh_project.data ORDER BY id DESC')
        for result in cur.fetchall():
            cont += 1
            if cont <= 300:
                f.write(str(result[1]) + ',' + str(result[2]) + ',' + str(result[3]) + ',' + str(result[4]) + ',' + str(result[5]) + ',' + str(result[6]) + '\n')
    filename="/path_to_csv_directory/MassSensirion.csv"
    return send_file(filename, as_attachment=True)    

@app.route('/fJSON2', methods=['GET', 'POST'])
def fJSON2():
    cont = 0
    js = {}
    with open('/path_to_json_directory/MassSensirion.json','w') as f:
        db.commit()
        cur.execute('SELECT id,date,time,mP1_0,mP2_5,mP4_0,mP10 FROM ssh_project.data ORDER BY id DESC')
        for result in cur.fetchall():
            cont += 1
            if cont <= 300:
                js[cont] = {}
                js[cont]['date'] = str(result[1])
                js[cont]['time'] = str(result[2])
                js[cont]['mPM1.0'] = float(result[3])
                js[cont]['mPM2.5'] = float(result[4])
                js[cont]['mPM4.0'] = float(result[5])
                js[cont]['mPM10'] = float(result[6])
        json.dump(js, f, indent = 6)
        cont = 0
    
    filename="/path_to_json_directory/MassSensirion.json"
    return send_file(filename, as_attachment=True)    

@app.route('/fCSV3', methods=['GET', 'POST'])
def fCSV3():
    cont = 0
    with open('/path_to_csv_directory/NumberSensirion.csv','w') as f:
        db.commit()
        cur.execute('SELECT id,date,time,nP0_5,nP1_0,nP2_5,nP4_0,nP10 FROM ssh_project.data ORDER BY id DESC')
        for result in cur.fetchall():
            cont += 1
            if cont <= 300:
                f.write(str(result[1]) + ',' + str(result[2]) + ',' + str(result[3]) + ',' + str(result[4]) + ',' + str(result[5]) + ',' + str(result[6]) + ',' + str(result[7]) + '\n')
    
    filename="/path_to_csv_directory/NumberSensirion.csv"
    return send_file(filename, as_attachment=True)    

@app.route('/fJSON3', methods=['GET', 'POST'])
def fJSON3():
    cont = 0
    js = {}
    with open('/path_to_json_directory/NumberSensirion.json','w') as f:
        db.commit()
        cur.execute('SELECT id,date,time,nP0_5,nP1_0,nP2_5,nP4_0,nP10 FROM ssh_project.data ORDER BY id DESC')
        for result in cur.fetchall():
            cont += 1
            if cont <= 300:
                js[cont] = {}
                js[cont]['date'] = str(result[1])
                js[cont]['time'] = str(result[2])
                js[cont]['nPM0.5'] = float(result[3])
                js[cont]['nPM1.0'] = float(result[4])
                js[cont]['nPM2.5'] = float(result[5])
                js[cont]['nPM4.0'] = float(result[6])
                js[cont]['nPM10'] = float(result[7])
        json.dump(js, f, indent = 6)
        cont = 0
    
    filename="/path_to_json_directory/NumberSensirion.json"
    return send_file(filename, as_attachment=True)    

@app.route('/fCSV4', methods=['GET', 'POST'])
def fCSV4():
    cont = 0
    with open('/path_to_csv_directory/Omron.csv','w') as f:
        db.commit()
        cur.execute('SELECT id,date,time,Humidity,Vout1 FROM ssh_project.data ORDER BY id DESC')
        for result in cur.fetchall():
            cont += 1
            if cont <= 300:
                f.write(str(result[1]) + ',' + str(result[2]) + ',' + str(result[3]) + ',' + str(result[4]) + '\n')
    
    filename="/path_to_csv_directory/Omron.csv"
    return send_file(filename, as_attachment=True)   

@app.route('/fJSON4')
def fJSON4():
    cont = 0
    js = {}
    with open('/path_to_json_directory/Omron.json','w') as f:
        db.commit()
        cur.execute('SELECT id,date,time,Humidity,Vout1 FROM ssh_project.data ORDER BY id DESC')
        for result in cur.fetchall():
            cont += 1
            if cont <= 300:
                js[cont] = {}
                js[cont]['date'] = str(result[1])
                js[cont]['time'] = str(result[2])
                js[cont]['Humidity'] = float(result[3])
                js[cont]['Vout1'] = int(result[4])         
        json.dump(js, f, indent = 6)
        cont = 0
    filename="/path_to_json_directory/Omron.json"
    return send_file(filename, as_attachment=True)

def on_connect(client, userdata, flags, rc):
    client.subscribe([('esp32/data', 0)])

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    data_list = str(data).split(',')

    today = date.today()
    current_date = today.strftime("%Y-%m-%d")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    cur.execute("USE ssh_project")
    cur.execute("INSERT INTO data (date, time, Temperature, Pressure, Humidity, mP1_0, mP2_5, mP4_0, mP10, nP0_5, nP1_0, nP2_5, nP4_0, nP10, Vout1, Vout2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (current_date, current_time, data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5], data_list[6], data_list[7], data_list[8], data_list[9], data_list[10], data_list[11], data_list[12], data_list[13]))
    db.commit()

    data_list.insert(0, current_time)
    data_list.insert(0, current_date)

    socketio.emit('sendData', data_list)


if __name__ == "__main__":
    client = mqtt.Client()
  
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host = 'test.mosquitto.org')
    client.loop_start()

    socketio.run(app)
    client.loop_stop()
