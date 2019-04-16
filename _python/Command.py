import Settings
from time import sleep
from PyQt5.QtCore import QThread
from PyQt5 import QtCore, QtGui, QtWidgets

def ergz_frame(self):
    Settings.ASD.write(bytes("7~0~", 'UTF-8'))

