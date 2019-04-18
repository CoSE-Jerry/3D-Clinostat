import Settings
#from time import sleep
#from PyQt5.QtCore import QThread
#from PyQt5 import QtCore, QtGui, QtWidgets

def ergz_frame(self,addr):
    Settings.sendCMD(addr,"1~")

def ergz_core(self):
    Settings.sendCMD(Settings.core_addr,"1~")

def frame_slider_change(self):
    Settings.frame_RPM=self.frame_verticalSlider.sliderPosition()/10
    self.frame_spinBox.setValue(Settings.frame_RPM)

def frame_spin_select(self):
    Settings.frame_RPM=self.frame_spinBox.value()
    
    self.frame_verticalSlider.blockSignals(True)
    self.frame_verticalSlider.setValue(Settings.frame_RPM*10)
    self.frame_verticalSlider.blockSignals(False)
    
    CMD = "2~"+Settings.getInterval(Settings.frame_RPM)
    Settings.sendCMD(Settings.frame_addr,CMD)

def reverse_frame_select(self):
    if(Settings.frame_dir==0):
        Settings.frame_dir=1
    else:
        Settings.frame_dir=0
    Settings.sendCMD(Settings.frame_addr,"3~"+str(Settings.frame_dir))
    

