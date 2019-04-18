import smbus
i2c_cmd = 0x5E

def init():
    global frame_RPM
    frame_RPM = 0.3

    global lighting_addr
    lighting_addr = 0x08
    
    global frame_addr
    frame_addr = 0x09

    global core_addr
    core_addr = 0x10
    

def sendCMD(addr,cont):
    bus = smbus.SMBus(1)
    converted = []
    for b in cont:
        converted.append(ord(b))
    bus.write_i2c_block_data(addr, i2c_cmd, converted)

def getInterval(RPM):
    return str(int(round(60/(RPM*0.351488))))
    

