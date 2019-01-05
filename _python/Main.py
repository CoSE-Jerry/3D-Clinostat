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

    def custom_update(self):
        Settings.custom_R = self.R_spinBox.value()
        Settings.custom_G = self.G_spinBox.value()
        Settings.custom_B = self.B_spinBox.value()
        Settings.custom_W = self.W_spinBox.value()

    def brightness_change(self):
        Settings.ASD.write(bytes('2~'+str(self.BRT_spinBox.value()), 'UTF-8'))

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
        #Settings.ASD.write(bytes("8~1~"+str(Settings.core_RPM), 'UTF-8'))

    def frame_change(self):
        Settings.frame_RPM=self.frame_verticalSlider.sliderPosition()
        self.frame_spinBox.setValue(Settings.frame_RPM)
        Settings.ASD.write(bytes("7~1~"+str(Settings.frame_RPM), 'UTF-8'))

    def core_change(self):
        Settings.core_RPM=self.core_verticalSlider.sliderPosition()
        self.core_spinBox.setValue(Settings.core_RPM)
        Settings.ASD.write(bytes("8~1~"+str(Settings.core_RPM), 'UTF-8'))

    def frame_select(self):
        if(Settings.LINKED):
            self.linked_change()
        else:
            self.frame_change()

    def core_select(self):
        if(Settings.LINKED):
            self.linked_change()
        else:
            self.core_change()

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
            self.linked_spin_change()
        else:
            self.frame_spin_change()

    def linked_spin_change(self):
        if(self.frame_spinBox.value() != Settings.frame_RPM):
            Settings.frame_RPM=self.frame_spinBox.value()
            Settings.core_RPM=Settings.frame_RPM
            self.core_spinBox.setValue(Settings.core_RPM)
        else:
            Settings.core_RPM = self.core_spinBox.value()
            Settings.frame_RPM=Settings.core_RPM
            self.frame_spinBox.setValue(Settings.frame_RPM)

        self.core_verticalSlider.setValue(Settings.core_RPM)
        self.frame_verticalSlider.setValue(Settings.frame_RPM)
        
        Settings.ASD.write(bytes("7~1~"+str(Settings.frame_RPM), 'UTF-8'))
        #Settings.ASD.write(bytes("8~1~"+str(Settings.core_RPM), 'UTF-8'))

    def frame_spin_change(self):
        Settings.frame_RPM=self.frame_spinBox.value()
        self.frame_verticalSlider.setValue(Settings.frame_RPM)
        Settings.ASD.write(bytes("7~1~"+str(Settings.frame_RPM)+"~", 'UTF-8'))

    def core_spin_select(self):
        if(Settings.LINKED):
            self.linked_spin_change()
        else:
            self.core_spin_change()

    def core_spin_change(self):
        Settings.core_RPM=self.core_spinBox.value()
        self.core_verticalSlider.setValue(Settings.core_RPM)
        Settings.ASD.write(bytes("8~1~"+str(Settings.frame_RPM), 'UTF-8'))

    def ergz(self):
        Settings.ASD.write(bytes("7~0~", 'UTF-8'))
        #Settings.ASD.write(bytes("7~1~3", 'UTF-8'))
        
        
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
        self.frameErgz_pushButton.clicked.connect(lambda: self.ergz())


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
