# import basic libraries
import time
import sys

#import UI functions

# import settings
import Settings

import Threads

# import custom functions
import Command
from time import sleep
import os
import sys
 
# import Qt content
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
 
# import generated UI
import Clinostat_UI
 
# create class for Raspberry Pi GUI
class MainWindow(QMainWindow, Clinostat_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def custom_update(self):
        Settings.custom_R = self.R_spinBox.value()
        Settings.custom_G = self.G_spinBox.value()
        Settings.custom_B = self.B_spinBox.value()
        Settings.custom_W = self.W_spinBox.value()

    def brightness_change(self):
        Settings.ASD.write(bytes('2~'+str(self.BRT_spinBox.value()), 'UTF-8'))

    def frame_select(self):
        if(Settings.LINKED):
            Command.linked_change(self)
        else:
            Command.frame_change(self)

    def core_select(self):
        if(Settings.LINKED):
            Command.linked_change(self)
        else:
            Command.core_change(self)

    def link(self):
        if(Settings.LINKED):
            Settings.LINKED = False
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../_image/Broken_Link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.frameLink_pushButton.setIcon(icon)
            self.coreLink_pushButton.setIcon(icon)
        else:
            Settings.LINKED = True
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../_image/Link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.frameLink_pushButton.setIcon(icon)
            self.coreLink_pushButton.setIcon(icon)

    def frame_spin_select(self):
        if(Settings.LINKED):
            Command.linked_spin_change(self)
        else:
            Command.frame_spin_change(self)

    def core_spin_select(self):
        if(Settings.LINKED):
            Command.linked_spin_change(self)
        else:
            Command.core_spin_change(self)

    def ergz_frame_select(self):
        if(Settings.LINKED):
            Command.ergz_linked(self)
        else:
            Command.ergz_frame(self)

    def ergz_core_select(self):
        if(Settings.LINKED):
            Command.ergz_linked(self)
        else:
            Command.ergz_core(self)

    def reverse_frame_select(self):
        forward = QtGui.QIcon()
        forward.addPixmap(QtGui.QPixmap("../_image/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        reverse = QtGui.QIcon()
        reverse.addPixmap(QtGui.QPixmap("../_image/Reverse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        
        if(Settings.LINKED):
            Command.reverse_linked(self)
            if(Settings.frame_dir==0):
                self.frameReverse_pushButton.setIcon(reverse)
            else:
                self.frameReverse_pushButton.setIcon(forward)
            if(Settings.core_dir==0):
                self.coreReverse_pushButton.setIcon(reverse)
            else:
                self.coreReverse_pushButton.setIcon(forward)
        else:
            Command.reverse_frame(self)
            if(Settings.frame_dir==0):
                self.frameReverse_pushButton.setIcon(reverse)
            else:
                self.frameReverse_pushButton.setIcon(forward)

    def reverse_core_select(self):
        forward = QtGui.QIcon()
        forward.addPixmap(QtGui.QPixmap("../_image/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        reverse = QtGui.QIcon()
        reverse.addPixmap(QtGui.QPixmap("../_image/Reverse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        if(Settings.LINKED):
            Command.reverse_linked(self)
            if(Settings.frame_dir==0):
                self.frameReverse_pushButton.setIcon(reverse)
            else:
                self.frameReverse_pushButton.setIcon(forward)
            if(Settings.core_dir==0):
                self.coreReverse_pushButton.setIcon(reverse)
            else:
                self.coreReverse_pushButton.setIcon(forward)
        else:
            Command.reverse_core(self)
            if(Settings.core_dir==0):
                self.coreReverse_pushButton.setIcon(reverse)
            else:
                self.coreReverse_pushButton.setIcon(forward)

    def apply_frame_select(self):
        if(Settings.LINKED):
            Command.linked_apply(self)
        else:
            Command.frame_apply(self)

    def apply_core_select(self):
        if(Settings.LINKED):
            Command.linked_apply(self)
        else:
            Command.core_apply(self)

    def reset_frame_select(self):
        if(Settings.LINKED):
            Command.linked_reset(self)
        else:
            Command.frame_reset(self)

    def reset_core_select(self):
        if(Settings.LINKED):
            Command.linked_reset(self)
        else:
            Command.core_reset(self)

    def snapshot(self):
        try:
            self.Snap_Thread = Threads.Snap()
            self.Snap_Thread.start()
            sleep(10)
            os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh download /3D_Clinostat/Snapshot/Snapshot.jpg /home/pi/3D-Clinostat/_temp/")
            
        except Exception as e:
            print(e)
        
        
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        Settings.init()

        self.topColor_comboBox.currentIndexChanged.connect(lambda: Command.top_color_change(self))
        self.leftColor_comboBox.currentIndexChanged.connect(lambda: Command.left_color_change(self))
        self.rightColor_comboBox.currentIndexChanged.connect(lambda: Command.right_color_change(self))
        self.bottomColor_comboBox.currentIndexChanged.connect(lambda: Command.bottom_color_change(self))
        self.IR_pushButton.clicked.connect(lambda: Command.IR_trigger(self))
        self.Cooling.clicked.connect(lambda: Command.Cooling_trigger(self))
        
        self.frame_verticalSlider.valueChanged.connect(lambda: self.frame_select())
        self.core_verticalSlider.valueChanged.connect(lambda: self.core_select())
        
        self.frame_spinBox.valueChanged.connect(lambda: self.frame_spin_select())
        self.core_spinBox.valueChanged.connect(lambda: self.core_spin_select())
        
        self.coreLink_pushButton.clicked.connect(lambda: self.link())
        self.frameLink_pushButton.clicked.connect(lambda: self.link())
        
        self.frameErgz_pushButton.clicked.connect(lambda: self.ergz_frame_select())
        self.coreErgz_pushButton.clicked.connect(lambda: self.ergz_core_select())

        self.frameReverse_pushButton.clicked.connect(lambda: self.reverse_frame_select())
        self.coreReverse_pushButton.clicked.connect(lambda: self.reverse_core_select())

        self.frameApply_pushButton.clicked.connect(lambda: self.apply_frame_select())
        self.frameReset_pushButton.clicked.connect(lambda: self.reset_frame_select())

        self.coreApply_pushButton.clicked.connect(lambda: self.apply_core_select())
        self.coreReset_pushButton.clicked.connect(lambda: self.reset_core_select())

        self.music_pushButton.clicked.connect(lambda: Command.music(self))
        
        self.R_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.G_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.B_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.W_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.BRT_spinBox.valueChanged.connect(lambda: self.brightness_change())

        self.snapshot_pushButton.clicked.connect(lambda: self.snapshot())
        

# main function
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
        
    # without this, the script exits immediately.
    sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
    main()
