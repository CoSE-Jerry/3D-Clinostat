import Settings
import Commands

#always seem to need this
import sys
 
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
 
# This is our window from QtCreator
import Clinostat_UI

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, Clinostat_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def link(self):
        if(Settings.LINKED):
            Settings.LINKED = False
            self.frameLink_pushButton.setIcon(Settings.broken)
            self.coreLink_pushButton.setIcon(Settings.broken)
        else:
            Settings.LINKED = True
            self.frameLink_pushButton.setIcon(Settings.linked)
            self.coreLink_pushButton.setIcon(Settings.linked)

    def frame_slider_select(self):
        if(Settings.LINKED):
            Commands.linked_slider_change(self)
        else:
            Commands.frame_slider_change(self)

    def core_slider_select(self):
        if(Settings.LINKED):
            Commands.linked_slider_change(self)
        else:
            Commands.core_slider_change(self)

    def frame_spin_select(self):
        Commands.frame_spin_select(self)

    def core_spin_select(self):
        Commands.core_spin_select(self)

    def reverse_frame_select(self):

        if(Settings.frame_dir==0):
            self.frameReverse_pushButton.setIcon(Settings.reverse)
        else:
            self.frameReverse_pushButton.setIcon(Settings.forward)
        Commands.reverse_frame_select(self)

    def reverse_core_select(self):

        if(Settings.core_dir==0):
            self.coreReverse_pushButton.setIcon(Settings.reverse)
        else:
            self.coreReverse_pushButton.setIcon(Settings.forward)
        Commands.reverse_core_select(self)
            
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        Settings.init()
        
        self.frameErgz_pushButton.clicked.connect(lambda: Commands.ergz_motor(self,Settings.frame_addr))
        self.coreErgz_pushButton.clicked.connect(lambda: Commands.ergz_motor(self,Settings.core_addr))

        self.frame_spinBox.valueChanged.connect(lambda: self.frame_spin_select())
        self.core_spinBox.valueChanged.connect(lambda: self.core_spin_select())

        self.frame_verticalSlider.valueChanged.connect(lambda: self.frame_slider_select())
        self.core_verticalSlider.valueChanged.connect(lambda: self.core_slider_select())

        self.frameReverse_pushButton.clicked.connect(lambda: self.reverse_frame_select())
        self.coreReverse_pushButton.clicked.connect(lambda: self.reverse_core_select())

        self.frameLink_pushButton.clicked.connect(lambda: self.link())
        self.coreLink_pushButton.clicked.connect(lambda: self.link())


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
