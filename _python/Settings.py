import smbus
import time
from PyQt5 import QtGui

i2c_cmd = 0x5E

def init():

    global LINKED
    LINKED = True

    global IR_STAT
    IR_STAT = False

    global imaging 
    imaging =False
    
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

    global tag_index
    tag_index = 0

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

    global sequence_name
    sequence_name=""

    global current_image
    current_image=""

    global default_dir
    default_dir = "/home/pi/Desktop"

    global full_dir
    full_dir = ""

    global date
    date = time.strftime('%m_%d_%Y')

    global interval
    interval = 1

    global duration
    duration = 1

    global total
    total = 1

    global current
    current = 0

    global rotation
    rotation = 0

    global x_resolution
    x_resolution=2464

    global y_resolution
    y_resolution=2464

    global imaging_mode
    imaging_mode = 1

    global trasmitted
    trasmitted = 0

    global commands_list
    commands_list = []

    global timelapse_running
    timelapse_running =False

    global cycle_time
    cycle_time=60
    
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


