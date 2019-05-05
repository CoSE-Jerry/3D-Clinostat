import Settings
import Commands
import Threads
import UI_Update
import os
import time

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

    def custom_update(self):
        Settings.custom_R = self.R_spinBox.value()
        Settings.custom_G = self.G_spinBox.value()
        Settings.custom_B = self.B_spinBox.value()
        Settings.custom_W = self.W_spinBox.value()
        Settings.LED_start = self.Start_spinBox.value()
        Settings.LED_end = self.End_spinBox.value()

        if(Settings.LED_start>=Settings.LED_end):
            self.light_Confirm_pushButton.setEnabled(False)
        else:
            self.light_Confirm_pushButton.setEnabled(True)
            

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

    def start_snapshot(self):
        try:
            self.Snap_Thread = Threads.Snap()
            '''self.Snap_Thread.started.connect(lambda: UI_Update_Disable.snap_disable(self,sch_flip))'''
            self.Snap_Thread.finished.connect(lambda: UI_Update.snap_complete(self))
            self.Snap_Thread.start()
            
        except Exception as e:
            print(e)

    def start_preview(self):
        try:
            self.Preview_Thread = Threads.Preview()
            '''self.Snap_Thread.started.connect(lambda: UI_Update_Disable.snap_disable(self,sch_flip))'''
            self.Preview_Thread.finished.connect(lambda: UI_Update.preview_complete(self))
            self.Preview_Thread.start()
            
        except Exception as e:
            print(e)

    def sensor_init(self):

            os.system("i2cdetect -y 1 > ../_temp/output.txt")

            if '1f' in open('../_temp/output.txt').read():
                self.Sensor_Thread = Threads.Sensor()
                self.Sensor_Thread.update.connect(lambda: UI_Update.sensor_update(self))
                self.Sensor_Thread.start()

    def IST_Edit(self):
        Settings.sequence_name = self.title_lineEdit.text()
        Settings.full_dir = Settings.default_dir + "/" + Settings.sequence_name
        self.directory_label.setText(Settings.full_dir)
        
        if Settings.date not in Settings.sequence_name: 
            self.addDate_pushButton.setEnabled(True)
        if(len(Settings.sequence_name) == 0):
            self.addDate_pushButton.setEnabled(False)
            
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.sensor_init()

        
        Settings.init()
        
        self.frameErgz_pushButton.clicked.connect(lambda: Commands.ergz_motor(self,Settings.frame_addr))
        self.coreErgz_pushButton.clicked.connect(lambda: Commands.ergz_motor(self,Settings.core_addr))
        
        self.snapshot_pushButton.clicked.connect(lambda: self.start_snapshot())
        self.preview_pushButton.clicked.connect(lambda: self.start_preview())

        self.frame_spinBox.valueChanged.connect(lambda: self.frame_spin_select())
        self.core_spinBox.valueChanged.connect(lambda: self.core_spin_select())

        self.frame_verticalSlider.valueChanged.connect(lambda: self.frame_slider_select())
        self.core_verticalSlider.valueChanged.connect(lambda: self.core_slider_select())

        self.frameReverse_pushButton.clicked.connect(lambda: self.reverse_frame_select())
        self.coreReverse_pushButton.clicked.connect(lambda: self.reverse_core_select())

        self.frameLink_pushButton.clicked.connect(lambda: self.link())
        self.coreLink_pushButton.clicked.connect(lambda: self.link())

        self.R_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.G_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.B_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.W_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.Start_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.End_spinBox.valueChanged.connect(lambda: self.custom_update())

        self.IR_pushButton.clicked.connect(lambda: Commands.IR_trigger(self))
        self.light_Confirm_pushButton.clicked.connect(lambda: Commands.light_confirm(self))
        self.light_Reset_pushButton.clicked.connect(lambda: Commands.light_reset(self))
        self.BRT_spinBox.valueChanged.connect(lambda: Commands.brightness_change(self))

        self.title_lineEdit.textChanged.connect(lambda: self.IST_Edit())


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
