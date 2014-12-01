import time

import settings


__author__ = 'laurogama'
import serial


actions = {
    'ligar': 'l',
    'desligar': 'd',
    'estado':'e',
    'power': '1',
    'canalup': '2',
    'canaldown': '3',
    'volumeup': '4',
    'volumedown': '5'
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


def send_message(id, action):
    try:
        ser = serial.Serial(settings.SERIAL_PORT, 9600, timeout=1)
        if connect_target(id, ser):
            ser.write(actions[action])
            time.sleep(0.1)
            status = ser.readline()
            ser.close()
            return {
                "command": "execute action: " + action,
                "target": id,
                "status": status}
        return {"error": "Problems sending message"}
    except:
        return {"error": "Cant open serial port " + settings.SERIAL_PORT}