import Settings
from time import sleep
from PyQt5.QtCore import QThread
from PyQt5 import QtCore, QtGui, QtWidgets



def top_color_change(self):
    temp = self.topColor_comboBox.currentIndex()
    print("top")
    if temp == 1:
        Settings.ASD.write(bytes("1~0~8~255~0~0~0", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~0~8~0~255~0~0", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~0~8~0~0~255~0", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~0~8~0~0~0~255", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~0~8~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~"+str(Settings.custom_W), 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~0~8~0~0~0~0", 'UTF-8'))

def left_color_change(self):
    temp = self.leftColor_comboBox.currentIndex()
    print("left")
    if temp == 1:
        Settings.ASD.write(bytes("1~8~15~255~0~0~0", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~8~15~0~255~0~0", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~8~15~0~0~255~0", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~8~15~0~0~0~255", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~8~15~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~" +str(Settings.custom_W), 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~8~15~0~0~0~0", 'UTF-8'))

def right_color_change(self):
    temp = self.rightColor_comboBox.currentIndex()
    print("right")
    if temp == 1:
        Settings.ASD.write(bytes("1~15~23~255~0~0~0", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~15~23~0~255~0~0", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~15~23~0~0~255~0", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~15~23~0~0~0~255", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~15~23~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~" +str(Settings.custom_W), 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~15~23~0~0~0~0", 'UTF-8'))

def bottom_color_change(self):
    temp = self.bottomColor_comboBox.currentIndex()
    print("bottom")
    if temp == 1:
        Settings.ASD.write(bytes("1~23~30~255~0~0~0", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~23~30~0~255~0~0", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~23~30~0~0~255~0", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~23~30~0~0~0~255", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~23~30~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~" +str(Settings.custom_W), 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~23~30~0~0~0~0", 'UTF-8'))

def IR_trigger(self):

    if not Settings.IR_STAT:
        Settings.ASD.write(bytes("5~", 'UTF-8'))
        Settings.IR_STAT=True
        self.IR_pushButton.setText("INFRARED:ON")
    
    else:
        Settings.ASD.write(bytes("5~", 'UTF-8'))
        Settings.IR_STAT=False
        self.IR_pushButton.setText("INFRARED:OFF")

def Cooling_trigger(self):

    if not Settings.CL_STAT:
        Settings.ASD.write(bytes("6~", 'UTF-8'))
        Settings.CL_STAT=True
        self.Cooling.setText("COOLING:ON")
    
    else:
        Settings.ASD.write(bytes("6~", 'UTF-8'))
        Settings.CL_STAT=False
        self.Cooling.setText("COOLING:OFF")

def linked_change(self):
    if(Settings.frame_RPM != self.frame_verticalSlider.sliderPosition()):
        Settings.frame_RPM=self.frame_verticalSlider.sliderPosition()
        Settings.core_RPM=Settings.frame_RPM
        self.core_verticalSlider.setValue(Settings.core_RPM)
    else:
        Settings.core_RPM = self.core_verticalSlider.sliderPosition()
        Settings.frame_RPM=Settings.core_RPM
        self.frame_verticalSlider.setValue(Settings.frame_RPM)

    self.core_spinBox.blockSignals(True)
    self.frame_spinBox.blockSignals(True)
    self.core_spinBox.setValue(Settings.core_RPM)
    self.frame_spinBox.setValue(Settings.frame_RPM)
    self.core_spinBox.blockSignals(False)
    self.frame_spinBox.blockSignals(False)
        
    Settings.ASD.write(bytes("7~1~"+str(Settings.frame_RPM), 'UTF-8'))
    sleep(Settings.hold)
    Settings.ASD.write(bytes("8~1~"+str(Settings.core_RPM), 'UTF-8'))

def frame_change(self):
    Settings.frame_RPM=self.frame_verticalSlider.sliderPosition()
    self.frame_spinBox.setValue(Settings.frame_RPM)
    Settings.ASD.write(bytes("7~1~"+str(Settings.frame_RPM), 'UTF-8'))

def core_change(self):
    Settings.core_RPM=self.core_verticalSlider.sliderPosition()
    self.core_spinBox.setValue(Settings.core_RPM)
    Settings.ASD.write(bytes("8~1~"+str(Settings.core_RPM), 'UTF-8'))
    print(Settings.core_RPM)

def linked_spin_change(self):
    if(self.frame_spinBox.value() != Settings.frame_RPM):
        Settings.frame_RPM=self.frame_spinBox.value()
        Settings.core_RPM=Settings.frame_RPM
        self.core_spinBox.setValue(Settings.core_RPM)
    else:
        Settings.core_RPM = self.core_spinBox.value()
        Settings.frame_RPM=Settings.core_RPM
        self.frame_spinBox.setValue(Settings.frame_RPM)

    self.core_verticalSlider.blockSignals(True)
    self.frame_verticalSlider.blockSignals(True)
    self.core_verticalSlider.setValue(Settings.core_RPM)
    self.frame_verticalSlider.setValue(Settings.frame_RPM)
    self.core_verticalSlider.blockSignals(False)
    self.frame_verticalSlider.blockSignals(False)
        
    Settings.ASD.write(bytes("7~1~"+str(Settings.frame_RPM), 'UTF-8'))
    sleep(Settings.hold)
    Settings.ASD.write(bytes("8~1~"+str(Settings.core_RPM), 'UTF-8'))

def frame_spin_change(self):
    Settings.frame_RPM=self.frame_spinBox.value()
    self.frame_verticalSlider.blockSignals(True)
    self.frame_verticalSlider.setValue(Settings.frame_RPM)
    self.frame_verticalSlider.blockSignals(False)
    Settings.ASD.write(bytes("7~1~"+str(Settings.frame_RPM)+"~", 'UTF-8'))
        
def core_spin_change(self):
    Settings.core_RPM=self.core_spinBox.value()
    self.core_verticalSlider.blockSignals(True)
    self.core_verticalSlider.setValue(Settings.core_RPM)
    self.core_verticalSlider.blockSignals(False)
    Settings.ASD.write(bytes("8~1~"+str(Settings.frame_RPM), 'UTF-8'))

def ergz_linked(self):
    Settings.ASD.write(bytes("7~0~", 'UTF-8'))
    sleep(Settings.hold)
    Settings.ASD.write(bytes("8~0~", 'UTF-8'))

def ergz_frame(self):
    Settings.ASD.write(bytes("7~0~", 'UTF-8'))

def ergz_core(self):
    Settings.ASD.write(bytes("8~0~", 'UTF-8'))

def reverse_linked(self):
    if(Settings.frame_dir==0):
        Settings.frame_dir=1
    else:
        Settings.frame_dir=0

    if(Settings.core_dir==0):
        Settings.core_dir=1
    else:
        Settings.core_dir=0

    Settings.ASD.write(bytes("7~2~"+str(Settings.frame_dir), 'UTF-8'))
    sleep(Settings.hold)
    Settings.ASD.write(bytes("8~2~"+str(Settings.core_dir), 'UTF-8'))

def reverse_frame(self):
    if(Settings.frame_dir==0):
        Settings.frame_dir=1
    else:
        Settings.frame_dir=0
    Settings.ASD.write(bytes("7~2~"+str(Settings.frame_dir), 'UTF-8'))

def reverse_core(self):
    if(Settings.core_dir==0):
        Settings.core_dir=1
    else:
        Settings.core_dir=0
    Settings.ASD.write(bytes("8~2~"+str(Settings.core_dir), 'UTF-8'))

def linked_apply(self):
    Settings.ASD.write(bytes("7~3~"+str(self.frameCD_spinBox.value())+"~"+str(self.framePW_spinBox.value())+"~"+str(self.framePI_spinBox.value())+"~"+self.frameMS_comboBox.currentText()+"~", 'UTF-8'))
    sleep(Settings.hold)
    Settings.ASD.write(bytes("8~3~"+str(self.coreCD_spinBox.value())+"~"+str(self.corePW_spinBox.value())+"~"+str(self.corePI_spinBox.value())+"~"+self.coreMS_comboBox.currentText()+"~", 'UTF-8'))

def linked_reset(self):
    Settings.ASD.write(bytes("7~3~0~2~380~128~", 'UTF-8'))
    sleep(Settings.hold)
    Settings.ASD.write(bytes("8~3~0~2~380~128~", 'UTF-8'))

def frame_apply(self):
    Settings.ASD.write(bytes("7~3~"+str(self.frameCD_spinBox.value())+"~"+str(self.framePW_spinBox.value())+"~"+str(self.framePI_spinBox.value())+"~"+self.frameMS_comboBox.currentText()+"~", 'UTF-8'))

def core_apply(self):
    Settings.ASD.write(bytes("8~3~"+str(self.coreCD_spinBox.value())+"~"+str(self.corePW_spinBox.value())+"~"+str(self.corePI_spinBox.value())+"~"+self.coreMS_comboBox.currentText()+"~", 'UTF-8'))
    
def frame_reset(self):
    Settings.ASD.write(bytes("7~3~0~2~380~128~", 'UTF-8'))

def core_reset(self):
    Settings.ASD.write(bytes("8~3~0~2~380~128~", 'UTF-8'))

def music(self):
    if(Settings.music == 0):
        Settings.music=1
        Settings.ASD.write(bytes("3", 'UTF-8'))
    else:
        Settings.music=0
        Settings.ASD.write(bytes("4", 'UTF-8'))
    


