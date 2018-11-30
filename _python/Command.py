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
    temp = self.Left_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('2', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('0', 'UTF-8'))

def right_color_change(self):
    temp = self.Right_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('3', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('0', 'UTF-8'))

def bottom_color_change(self):
    temp = self.Top_Color_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('4', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('0', 'UTF-8'))


