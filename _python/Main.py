# always seem to need this
import sys
import smbus
import time

bus = smbus.SMBus(1)
address = 0x09
i2c_cmd = 0x5E
 
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
 
# This is our window from QtCreator
import Clinostat_UI
 
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, Clinostat_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def ergz_frame_select(self):
        converted = []
        for b in "1~":
            converted.append(ord(b))
        bus.write_i2c_block_data(address, i2c_cmd, converted)
        print("press")
        
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.frameErgz_pushButton.clicked.connect(lambda: self.ergz_frame_select())
 
# I feel better having one of these
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
