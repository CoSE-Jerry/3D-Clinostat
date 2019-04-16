import smbus

def init():
    global bus
    bus = smbus.SMBus(1)

