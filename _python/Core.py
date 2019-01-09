import socket
import subprocess
import os
import sys
from picamera import PiCamera
from threading import Thread
from time import sleep

HOST = ''
PORT = 5560

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    return conn

def dataTransfer(conn):
    while True:
        data = conn.recv(1024)
        command = data.decode('utf-8')
        if command == 'S':
            print(command)
            SnapShot = SnapShotProgram()
            SnapShotThread = Thread(target=SnapShot.run) 
            SnapShotThread.start()
        print("waiting")

class SnapShotProgram:  
    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        try:
            file = "/home/pi/3D-Clinostat/_temp/Snapshot.jpg"
            with PiCamera() as camera:
                sleep(0.8)
                camera.resolution = (310,310)
                camera.capture(file)
            os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + file + " /3D_Clinostat/Snapshot/")
            print("test")
        except Exception as e:
            print(e)
        
s = setupServer()

conn = setupConnection()
while True:
    while True:
        try:
            dataTransfer(conn)
        except socket.error as msg:
            print("disconnect")
