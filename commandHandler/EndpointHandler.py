import time

import settings


__author__ = 'laurogama'
import serial


actions = {
    'ligar': 'l',
    'desligar': 'd',
    'power': 'c1',
    'canalup': 'c2',
    'canaldown': 'c3',
    'volumeup': 'c4',
    'volumedown': 'c5'
}


def confirm_command(result):
    print result
    if result == 'OK':
        return True
    return False


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
                "status": status}, 200
        return "Problems sending message" , 500
    except:
        return "Cant open serial port " + settings.SERIAL_PORT, 503