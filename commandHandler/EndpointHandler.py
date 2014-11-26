import time

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

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)


def confirm_command(result):
    print result
    if result == 'OK':
        return True
    return False


# def connect_target(id, ser):
# print "connect_Target \n"
# ser.write("+++")
# # print ser.readall()
# if ser.readall() == "OK\r":
# print "+++ OK"
#         ser.write("ATDL" + id)
#         print ser.readall()
#         if ser.readall() == "OK\r":
#             print "atdl " + id + " OK"
#             ser.write("ATWR")
#             if ser.readall() == "OK\r":
#                 ser.write("ATCN")
#                 if ser.readall() == "OK\r":
#                     return True
#     print "error"
#     return False


def connect_target(id, ser):
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
    if connect_target(id, ser):
        ser.write(actions[action])
        return {
            "command": "execute action: " + action,
            "target": id,
            "status": ser.readline()}

    return "Problems sending message"