import serial

def init():
    global ASD
    ASD = serial.Serial('/dev/ttyUSB0', 9600)

    global IR_STAT
    IR_STAT = False

