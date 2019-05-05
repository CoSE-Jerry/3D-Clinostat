import Settings
import socket
import board
import busio
import adafruit_fxos8700

from time import sleep
from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from picamera import PiCamera

class Snap(QThread):

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip_address = "10.0.5.2"
        server_address = (ip_address, 23456)
        sock.connect(server_address)
        sock.sendall('A'.encode())

        with open('../_temp/snapshot.jpg', 'wb') as f:
                print('file opened')
                while True:
                    data = sock.recv(1024)
                    if not data:
                        break
                    f.write(data)
        sock.close()

class Preview(QThread):

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip_address = "10.0.5.2"
        server_address = (ip_address, 23456)
        sock.connect(server_address)
        sock.sendall('P'.encode())

        with open('../_temp/preview.jpg', 'wb') as f:
                print('file opened')
                while True:
                    data = sock.recv(1024)
                    if not data:
                        break
                    f.write(data)
        sock.close()

class Sensor(QThread):
    update = QtCore.pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = adafruit_fxos8700.FXOS8700(i2c)

        while True:
            accel_x, accel_y, accel_z = sensor.accelerometer
            mag_x, mag_y, mag_z = sensor.magnetometer

            ACC_X_text= round(accel_x,2)
            ACC_Y_text= round(accel_y,2)
            ACC_Z_text= round(accel_z,2)
            
            Settings.MAG_text = 'Magnetometer (uTesla): ({0:0.3f}, {1:0.3f}, {2:0.3f})'.format(mag_x, mag_y, mag_z)
            self.update.emit()
            sleep(0.5)
            

