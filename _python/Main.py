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
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        Settings.init()

        self.topColor_comboBox.currentIndexChanged.connect(lambda: Command.top_color_change(self))
        self.leftColor_comboBox.currentIndexChanged.connect(lambda: Command.left_color_change(self))
        self.rightColor_comboBox.currentIndexChanged.connect(lambda: Command.right_color_change(self))
        self.bottomColor_comboBox.currentIndexChanged.connect(lambda: Command.bottom_color_change(self))
        self.IR_pushButton.clicked.connect(lambda: Command.IR_trigger(self))

        

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
