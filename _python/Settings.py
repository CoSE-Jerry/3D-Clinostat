import serial

def init():
    global ASD
    ASD = serial.Serial('/dev/ttyUSB0', 9600)

    global IR_STAT
    IR_STAT = False

    global LINKED
    LINKED = True

    global inner_RPM
    inner_RPM = 3

    global outer_RPM
    outer_RPM = 3

    global custom_R
    custom_R=0
    global custom_G
    custom_G=0
    global custom_B
    custom_B=0
    global custom_W
    custom_W=0

