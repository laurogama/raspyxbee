import time

import settings


__author__ = 'laurogama'
import serial


actions = {
    'ligar': 'l',
    'desligar': 'd',
    'estado': 'e',
    'estadoporta':'f',
    'poweron': 'l',
    'poweroff':'d',
    'canalup': '2',
    'canaldown': '3',
    'volumeup': '4',
    'volumedown': '5',
    'verde': 'g',
    'vermelho': 'r',
    'laranja': 'o',
    'energia': 'e',
    'food': '1',
    'water': '2',
    'distancia': 'l',
    'check': '3'
}


def connect_target(id, ser):
    print "target:" + id
    ser.write("+++")
    time.sleep(0.1)
    print ser.readline()
    time.sleep(0.1)
    ser.write("atdl" + id + "\r")
    time.sleep(0.1)
    print ser.readline()
    time.sleep(0.1)
    ser.write("atwr\r")
    time.sleep(0.1)
    print ser.readline()
    time.sleep(0.1)
    ser.write("atcn\r")
    time.sleep(0.1)
    print ser.readline()
    time.sleep(0.1)
    return True


def prepare_message(action, id, ser):
    ser.write(actions[action])
    time.sleep(0.1)
    status = ser.readline()
    ser.close()
    if status == "":
        return {"command": action,
                "target": id,
                "error": "empty response",
                "status": "error"
        }
    print status
    return {
        "command": action,
        "target": id,
        "status": status}


def send_message(id, action):
    try:
        ser = serial.Serial(settings.SERIAL_PORT, 9600, timeout=1)
        if connect_target(id, ser):
            return prepare_message(action, id, ser)
        else:
            reset_xbee()
        if connect_target(id, ser):
            return prepare_message(action, id, ser)
        return {"error": "Problems sending message"}
    except:
        return {"error": "Cant open serial port " + settings.SERIAL_PORT}


def reset_xbee():
    ser = serial.Serial(settings.SERIAL_PORT, 9600, timeout=1)
    try:
        ser.write("+++")
        time.sleep(0.1)
        print ser.readline()
        time.sleep(0.1)
        ser.write("atfr")
        ser.close()
        return {"status": "OK"}
    except:
        return {"error": "Cant reset"}
