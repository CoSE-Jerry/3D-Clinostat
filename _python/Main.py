# import basic libraries
import time
import sys

#import UI functions

# import settings
import Settings

# import custom functions
import Command
 
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
        if(Settings.LINKED):
            Command.reverse_linked(self)
            if(Settings.frame_dir==0):
                self.frameReverse_pushButton.setIcon(reverse)
        else:
            Command.reverse_frame(self)

    def reverse_core_select(self):
        if(Settings.LINKED):
            Command.reverse_linked(self)
        else:
            Command.reverse_core(self)
        
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
        

        self.R_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.G_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.B_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.W_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.BRT_spinBox.valueChanged.connect(lambda: self.brightness_change())
        

# main function
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()

    forward = QtGui.QIcon()
    forward.addPixmap(QtGui.QPixmap("../_image/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    reverse = QtGui.QIcon()
    reverse.addPixmap(QtGui.QPixmap("../_image/Reverse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    
    # without this, the script exits immediately.
    sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
    main()
