import Settings
#from time import sleep
#from PyQt5.QtCore import QThread
#from PyQt5 import QtCore, QtGui, QtWidgets

def ergz_frame(self):
    Settings.sendCMD(Settings.frame_addr,"1~")

