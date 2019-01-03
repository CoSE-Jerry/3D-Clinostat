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

# UI variables

# global variables
 
# create class for Raspberry Pi GUI
class MainWindow(QMainWindow, Clinostat_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def outer_change(self):
        if(Settings.LINKED):
            Settings.outer_RPM=self.outer_verticalSlider.sliderPosition()
            Settings.inner_RPM=Settings.outer_RPM
            #self.inner_verticalSlider.setValue(Settings.inner_RPM)
            self.inner_spinBox.setValue(Settings.inner_RPM)
            self.outer_spinBox.setValue(Settings.outer_RPM)
            Settings.ASD.write(bytes("5~"+str(Settings.outer_RPM), 'UTF-8'))
            sleep(3);
            Settings.ASD.write(bytes("6~"+str(Settings.inner_RPM), 'UTF-8'))
        else:
            Settings.outer_RPM=self.outer_verticalSlider.sliderPosition()
            self.outer_spinBox.setValue(Settings.outer_RPM)
            Settings.ASD.write(bytes("5~"+str(Settings.outer_RPM), 'UTF-8'))

    def inner_change(self):
        if(Settings.LINKED):
            #Settings.inner_RPM=self.inner_verticalSlider.sliderPosition()
            Settings.outer_RPM=Settings.inner_RPM            
            self.outer_verticalSlider.setValue(Settings.outer_RPM)
            self.inner_spinBox.setValue(Settings.inner_RPM)
            self.outer_spinBox.setValue(Settings.outer_RPM)
            Settings.ASD.write(bytes("5~"+str(Settings.outer_RPM), 'UTF-8'))
            #Settings.ASD.write(bytes("6~"+str(Settings.inner_RPM), 'UTF-8'))
        else:
            #Settings.inner_RPM=self.inner_verticalSlider.sliderPosition()
            self.inner_spinBox.setValue(Settings.inner_RPM)
            Settings.ASD.write(bytes("6~"+str(Settings.inner_RPM), 'UTF-8'))

    def custom_update(self):
        Settings.custom_R = self.R_spinBox.value()
        Settings.custom_G = self.G_spinBox.value()
        Settings.custom_B = self.B_spinBox.value()
        Settings.custom_W = self.W_spinBox.value()

    def brightness_change(self):
        Settings.ASD.write(bytes('2~'+str(self.BRT_spinBox.value()), 'UTF-8'))

    def link(self):
        if(Settings.LINKED):
            Settings.LINKED = False
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../_image/Broken_Link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_link.setIcon(icon)
        else:
            Settings.LINKED = True
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../_image/Link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_link.setIcon(icon)
        
        
 
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
        #self.outer_verticalSlider.valueChanged.connect(lambda: self.outer_change())
        #self.inner_verticalSlider.valueChanged.connect(lambda: self.inner_change())
        #self.outer_spinBox.valueChanged.connect(lambda: self.inner_spin_change())
        #self.inner_spinBox.valueChanged.connect(lambda: self.inner_spin_hange())
        self.pushButton_link.clicked.connect(lambda: self.link())

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
    
    # without this, the script exits immediately.
    sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
    main()
