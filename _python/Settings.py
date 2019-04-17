import smbus
i2c_cmd = 0x5E

def init():
    global frame_RPM
    frame_RPM = 3
    

def sendCMD(addr,cont):
    bus = smbus.SMBus(1)
    converted = []
    for b in cont:
        converted.append(ord(b))
    bus.write_i2c_block_data(addr, i2c_cmd, converted)
    

