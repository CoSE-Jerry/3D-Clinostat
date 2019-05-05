import smbus
from PyQt5 import QtGui

i2c_cmd = 0x5E

def init():

    global LINKED
    LINKED = True

    global IR_STAT
    IR_STAT = False

    global i2c_open
    i2c_open =True
    
    global frame_RPM
    frame_RPM = 0.3

    global core_RPM
    core_RPM = 0.3

    global lighting_addr
    lighting_addr = 0x08
    
    global frame_addr
    frame_addr = 0x09

    global core_addr
    core_addr = 0x10

    global frame_dir
    frame_dir = 0

    global core_dir
    core_dir = 0

    global custom_R
    custom_R=0
    global custom_G
    custom_G=0
    global custom_B
    custom_B=0
    global custom_W
    custom_W=0

    global ACC_X_text
    ACC_X_text="offline"
    global ACC_Y_text
    ACC_Y_text="offline"
    global ACC_Z_text
    ACC_Z_text="offline"

    global GYRO_X_text
    GYRO_X_text="offline"
    global GYRO_Y_text
    GYRO_Y_text="offline"
    global GYRO_Z_text
    GYRO_Z_text="offline"
    
    global MAG_X_text
    MAG_X_text="offline"
    global MAG_Y_text
    MAG_Y_text="offline"
    global MAG_Z_text
    MAG_Z_text="offline"


    global forward
    forward = QtGui.QIcon()
    forward.addPixmap(QtGui.QPixmap("../_image/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    global reverse
    reverse = QtGui.QIcon()
    reverse.addPixmap(QtGui.QPixmap("../_image/Reverse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    global linked
    linked = QtGui.QIcon()
    linked.addPixmap(QtGui.QPixmap("../_image/Link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
    global broken
    broken = QtGui.QIcon()
    broken.addPixmap(QtGui.QPixmap("../_image/Broken_Link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        

def sendCMD(addr,cont):
    bus = smbus.SMBus(1)
    converted = []
    for b in cont:
        converted.append(ord(b))
    bus.write_i2c_block_data(addr, i2c_cmd, converted)

def getInterval(RPM):
    return str(int(round(60/(RPM*0.351488))))
    

