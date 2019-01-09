from PyQt5 import QtCore
from time import sleep
from PyQt5.QtCore import QThread

PORT = 5560


class Snap(QThread):

    captured = QtCore.pyqtSignal()
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False
        
    def run(self):
        HOST="192.168.1.130"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST,PORT))
            s.send(str.encode("S"))
            s.close
        except Exception as e:
            print(e)
        
        
