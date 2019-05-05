import Settings
import socket
import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c
import os

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
        cmd = "A~"+str(350)+"~"+str(350)+"~"+str(Settings.rotation)+"~1"
        sock.sendall(cmd.encode())

        with open('../_temp/snapshot.jpg', 'wb') as f:
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

        cmd = "A~"+str(Settings.x_resolution)+"~"+str(Settings.y_resolution)+"~"+str(Settings.rotation)+"~"+str(Settings.imaging_mode)
        
        sock.sendall(cmd.encode())

        if(Settings.imaging_mode):
            with open('../_temp/preview.jpg', 'wb') as f:
                    while True:
                        data = sock.recv(1024)
                        if not data:
                            break
                        f.write(data)
            sock.close()

        else:
            with open('../_temp/preview.png', 'wb') as f:
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

        i2c2 = busio.I2C(board.SCL, board.SDA)
        sensor2 = adafruit_fxas21002c.FXAS21002C(i2c2)

        while True:
            accel_x, accel_y, accel_z = sensor.accelerometer
            gyro_x, gyro_y, gyro_z = sensor2.gyroscope
            mag_x, mag_y, mag_z = sensor.magnetometer
            
            Settings.ACC_X_text= "{0:.2f}".format(accel_x)
            Settings.ACC_Y_text= "{0:.2f}".format(accel_y)
            Settings.ACC_Z_text= "{0:.2f}".format(accel_z)
            
            Settings.GYRO_X_text= "{0:.2f}".format(gyro_x)
            Settings.GYRO_Y_text= "{0:.2f}".format(gyro_y)
            Settings.GYRO_Z_text= "{0:.2f}".format(gyro_z)

            Settings.MAG_X_text= "{0:.2f}".format(mag_x)
            Settings.MAG_Y_text= "{0:.2f}".format(mag_y)
            Settings.MAG_Z_text= "{0:.2f}".format(mag_z)
            
            self.update.emit()
            sleep(0.1)

class Timelapse(QThread):
    captured = QtCore.pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        if(not os.path.isdir(Settings.full_dir)):
            os.mkdir(Settings.full_dir)
        for i in range(Settings.total):
            Settings.current_image = Settings.full_dir + "/" +Settings.sequence_name + "_%04d.jpg" % i
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ip_address = "10.0.5.2"
            server_address = (ip_address, 23456)
            sock.connect(server_address)
            sock.sendall('P'.encode())

            with open(Settings.current_image, 'wb') as f:
                print('file opened')
                while True:
                    data = sock.recv(1024)
                    if not data:
                        break
                    f.write(data)
            sock.close()
        
            self.captured.emit()
            sleep(Settings.interval)

            

