import Settings
from time import sleep
import socket
#from PyQt5.QtCore import QThread
#from PyQt5 import QtCore, QtGui, QtWidgets

def init():
    clear_lights
    sleep(0.1)
    Settings.sendCMD(Settings.frame_addr,"5~")
    sleep(0.1)
    Settings.sendCMD(Settings.core_addr,"5~")
    


def light_confirm(self):
    curr_cmd = "1~"+str(self.Start_spinBox.value())+"~"+str(self.End_spinBox.value())+"~"+ str(self.R_spinBox.value()) + "~" + str(self.G_spinBox.value()) + "~" + str(self.B_spinBox.value()) + "~"+str(self.W_spinBox.value())
    Settings.commands_list.append(curr_cmd)
    Settings.sendCMD(Settings.lighting_addr,curr_cmd)
    sleep(0.1)
    curr_cmd = "2~"+str(self.BRT_spinBox.value())
    Settings.commands_list.append(curr_cmd)
    Settings.sendCMD(Settings.lighting_addr,curr_cmd)

def light_reset(self):
    Settings.sendCMD(Settings.lighting_addr,"1~0~34~0~0~0~0")
    sleep(0.1)
    Settings.sendCMD(Settings.lighting_addr,"2~50")

    self.R_spinBox.setValue(0)
    self.G_spinBox.setValue(0) 
    self.B_spinBox.setValue(0)
    self.W_spinBox.setValue(0)
    self.Start_spinBox.setValue(0)
    self.End_spinBox.setValue(1)
    self.BRT_spinBox.setValue(50)
    Settings.commands_list.clear()

def clear_lights():
    Settings.sendCMD(Settings.lighting_addr,"1~0~34~0~0~0~0")
    
def ergz_motor(addr):
    if(Settings.LINKED):
        Settings.sendCMD(Settings.frame_addr,"1~")
        Settings.sendCMD(Settings.core_addr,"1~")
    else:
        Settings.sendCMD(addr,"1~")

def frame_slider_change(self):
    Settings.frame_RPM=self.frame_verticalSlider.sliderPosition()/10

    self.frame_spinBox.blockSignals(True)
    self.frame_spinBox.setValue(Settings.frame_RPM)
    CMD = "2~"+Settings.getInterval(Settings.frame_RPM)
    Settings.sendCMD(Settings.frame_addr,CMD)
    
    self.frame_spinBox.blockSignals(False)
    
def core_slider_change(self):
    Settings.core_RPM=self.core_verticalSlider.sliderPosition()/10
    self.core_spinBox.blockSignals(True)
    self.core_spinBox.setValue(Settings.core_RPM)
    CMD = "2~"+Settings.getInterval(Settings.core_RPM)
    Settings.sendCMD(Settings.core_addr,CMD)
    
    self.core_spinBox.blockSignals(False)

def linked_slider_change(self):
    self.core_spinBox.blockSignals(True)
    self.frame_spinBox.blockSignals(True)
    self.core_verticalSlider.blockSignals(True)
    self.frame_verticalSlider.blockSignals(True)
    
    if(Settings.frame_RPM != self.frame_verticalSlider.sliderPosition()/10):
        Settings.frame_RPM=self.frame_verticalSlider.sliderPosition()/10
        Settings.core_RPM=Settings.frame_RPM
        self.core_verticalSlider.setValue(Settings.core_RPM*10)
        self.core_spinBox.setValue(Settings.core_RPM)
        self.frame_spinBox.setValue(Settings.frame_RPM)
    else:
        Settings.core_RPM=self.core_verticalSlider.sliderPosition()/10
        Settings.frame_RPM=Settings.core_RPM
        self.frame_verticalSlider.setValue(Settings.frame_RPM*10)
        self.core_spinBox.setValue(Settings.core_RPM)
        self.frame_spinBox.setValue(Settings.frame_RPM)

    CMD = "2~"+Settings.getInterval(Settings.frame_RPM)
    Settings.sendCMD(Settings.frame_addr,CMD)
    sleep(0.02)
    CMD = "2~"+Settings.getInterval(Settings.core_RPM)
    Settings.sendCMD(Settings.core_addr,CMD)
    
    self.core_spinBox.blockSignals(False)
    self.frame_spinBox.blockSignals(False)
    self.core_verticalSlider.blockSignals(False)
    self.frame_verticalSlider.blockSignals(False)


def linked_spin_change(self):
    self.core_spinBox.blockSignals(True)
    self.frame_spinBox.blockSignals(True)
    self.core_verticalSlider.blockSignals(True)
    self.frame_verticalSlider.blockSignals(True)
    
    if(Settings.frame_RPM != self.frame_spinBox.value()):
        
        Settings.frame_RPM=self.frame_spinBox.value()
        Settings.core_RPM=Settings.frame_RPM
        self.core_verticalSlider.setValue(Settings.core_RPM*10)
        self.frame_verticalSlider.setValue(Settings.frame_RPM*10)
        self.core_spinBox.setValue(Settings.core_RPM)
        
    else:
        Settings.core_RPM=self.core_spinBox.value()
        Settings.frame_RPM=Settings.core_RPM
        self.frame_verticalSlider.setValue(Settings.frame_RPM*10)
        self.core_verticalSlider.setValue(Settings.core_RPM*10)
        self.frame_spinBox.setValue(Settings.frame_RPM)

    CMD = "2~"+Settings.getInterval(Settings.frame_RPM)
    Settings.sendCMD(Settings.frame_addr,CMD)
    sleep(0.02)
    CMD = "2~"+Settings.getInterval(Settings.core_RPM)
    Settings.sendCMD(Settings.core_addr,CMD)
    
    self.core_spinBox.blockSignals(False)
    self.frame_spinBox.blockSignals(False)
    self.core_verticalSlider.blockSignals(False)
    self.frame_verticalSlider.blockSignals(False)

def frame_spin_select(self):
    Settings.frame_RPM=self.frame_spinBox.value()
    
    self.frame_verticalSlider.blockSignals(True)
    self.frame_verticalSlider.setValue(Settings.frame_RPM*10)
    self.frame_verticalSlider.blockSignals(False)
    
    CMD = "2~"+Settings.getInterval(Settings.frame_RPM)
    Settings.sendCMD(Settings.frame_addr,CMD)

def core_spin_select(self):
    Settings.core_RPM=self.core_spinBox.value()
    
    self.core_verticalSlider.blockSignals(True)
    self.core_verticalSlider.setValue(Settings.core_RPM*10)
    self.core_verticalSlider.blockSignals(False)
    
    CMD = "2~"+Settings.getInterval(Settings.core_RPM)
    Settings.sendCMD(Settings.core_addr,CMD)

def reverse_frame_select(self):
    if(Settings.frame_dir==0):
        Settings.frame_dir=1
    else:
        Settings.frame_dir=0
    Settings.sendCMD(Settings.frame_addr,"3~"+str(Settings.frame_dir))

def reverse_core_select(self):
    if(Settings.core_dir==0):
        Settings.core_dir=1
    else:
        Settings.core_dir=0
    Settings.sendCMD(Settings.core_addr,"3~"+str(Settings.core_dir))

def IR_trigger(self):
    Settings.sendCMD(Settings.lighting_addr,"3~")
    Settings.commands_list.append("3~")
    if not Settings.IR_STAT:
        Settings.IR_STAT=True
        self.IR_pushButton.setText("INFRARED:ON")
    
    else:
        Settings.IR_STAT=False
        self.IR_pushButton.setText("INFRARED:OFF")

    

