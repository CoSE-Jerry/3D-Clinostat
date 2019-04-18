import Settings
#from time import sleep
#from PyQt5.QtCore import QThread
#from PyQt5 import QtCore, QtGui, QtWidgets

def ergz_frame(self):
    Settings.sendCMD(Settings.frame_addr,"1~")

def frame_slider_change(self):
    Settings.frame_RPM=self.frame_verticalSlider.sliderPosition()/10
    self.frame_spinBox.setValue(Settings.frame_RPM)

def frame_spin_select(self):
    Settings.frame_RPM=self.frame_spinBox.value()
    CMD = "2~"+Settings.getInterval(Settings.frame_RPM)
    Settings.sendCMD(Settings.frame_addr,CMD)
    

