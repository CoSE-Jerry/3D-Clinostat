import Settings
from time import sleep
from PyQt5.QtCore import QThread

def top_color_change(self):
    temp = self.topColor_comboBox.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('1', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('0', 'UTF-8'))

def left_color_change(self):
    temp = self.leftColor_comboBox.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('2', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('0', 'UTF-8'))

def right_color_change(self):
    temp = self.rightColor_comboBox.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('3', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('0', 'UTF-8'))

def bottom_color_change(self):
    temp = self.bottomColor_comboBox.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('4', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('0', 'UTF-8'))

def IR_trigger(self):
    
    if Settings.IR_STAT:
        Settings.ASD.write(bytes('6', 'UTF-8'))
        Settings.IR_STAT=False
    if not Settings.IR_STAT:
        Settings.ASD.write(bytes('5', 'UTF-8'))
        Settings.IR_STAT=True



