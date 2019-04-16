import serial

def init():
    global ASD
    ASD = serial.Serial('/dev/ttyS0', 9600)

    global custom_R
    custom_R=0
    global custom_G
    custom_G=0
    global custom_B
    custom_B=0
    global custom_W
    custom_W=0

