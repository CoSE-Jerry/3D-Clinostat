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
        if(Settings.LINKED):
            if(Settings.core_dir==0):
                self.coreReverse_pushButton.setIcon(Settings.reverse)
                self.frameReverse_pushButton.setIcon(Settings.reverse)
            else:
                self.coreReverse_pushButton.setIcon(Settings.forward)
                self.frameReverse_pushButton.setIcon(Settings.forward)
            Commands.reverse_core_select(self)
            Commands.reverse_frame_select(self)
        else:
            if(Settings.frame_dir==0):
                self.frameReverse_pushButton.setIcon(Settings.reverse)
            else:
                self.frameReverse_pushButton.setIcon(Settings.forward)
            Commands.reverse_frame_select(self)

    def reverse_core_select(self):
        if(Settings.LINKED):
            if(Settings.core_dir==0):
                self.coreReverse_pushButton.setIcon(Settings.reverse)
                self.frameReverse_pushButton.setIcon(Settings.reverse)
            else:
                self.coreReverse_pushButton.setIcon(Settings.forward)
                self.frameReverse_pushButton.setIcon(Settings.forward)
            Commands.reverse_core_select(self)
            Commands.reverse_frame_select(self)
        else:
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

    def start_timelapse(self):
        try:
            self.Timelapse_Thread = Threads.Timelapse()
            '''self.Snap_Thread.started.connect(lambda: UI_Update_Disable.snap_disable(self,sch_flip))'''
            self.Timelapse_Thread.captured.connect(lambda: UI_Update.image_update(self))
            self.Timelapse_Thread.start()
            
        except Exception as e:
            print(e)

    def rotate_image(self):
        Settings.rotation += 1
        self.start_snapshot()



            

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
        self.validate_input()

    def add_date(self):
        Settings.sequence_name = Settings.sequence_name + "_" + Settings.date
        self.title_lineEdit.setText(Settings.sequence_name)
        Settings.full_dir = Settings.default_dir + "/" + Settings.sequence_name
        self.directory_label.setText(Settings.full_dir)
        self.addDate_pushButton.setEnabled(False)

    def ICI_Change(self):
        Settings.interval = self.ICI_spinBox.value()
        self.validate_input()
                
    def ISD_Change(self):
        Settings.duration = self.ISD_spinBox.value()
        self.validate_input()

            
    def validate_input(self):
        Settings.total = int(Settings.duration/Settings.interval)
        if(Settings.total>0 and len(Settings.sequence_name)!=0):
            self.startImaging_pushButton.setEnabled(True)
        else:
            self.startImaging_pushButton.setEnabled(False)
        self.Progress_Label.setText("Progress: "+str(Settings.current) + "/" + str(Settings.total))
        

    def select_directory(self):
        m_directory = str(QFileDialog.getExistingDirectory(self, "Select Directory",'/media/pi'))
        if(len(m_directory)!=0):
            Settings.full_dir = m_directory +"/"+ Settings.sequence_name
            self.directory_label.setText(Settings.full_dir)
        self.validate_input()
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.sensor_init()

        Settings.init()
        
        self.frameErgz_pushButton.clicked.connect(lambda: Commands.ergz_motor(self,Settings.frame_addr))
        self.coreErgz_pushButton.clicked.connect(lambda: Commands.ergz_motor(self,Settings.core_addr))
        
        self.snapshot_pushButton.clicked.connect(lambda: self.start_snapshot())
        self.preview_pushButton.clicked.connect(lambda: self.start_preview())
        self.startImaging_pushButton.clicked.connect(lambda: self.start_timelapse())
        self.rotate_pushButton.clicked.connect(lambda: self.rotate_image())

        self.frame_spinBox.valueChanged.connect(lambda: self.frame_spin_select())
        self.core_spinBox.valueChanged.connect(lambda: self.core_spin_select())

        self.frame_verticalSlider.valueChanged.connect(lambda: self.frame_slider_select())
        self.core_verticalSlider.valueChanged.connect(lambda: self.core_slider_select())

        self.frameReverse_pushButton.clicked.connect(lambda: self.reverse_frame_select())
        self.coreReverse_pushButton.clicked.connect(lambda: self.reverse_core_select())

        self.link_pushButton.clicked.connect(lambda: UI_Update.link(self))

        self.Start_spinBox.valueChanged.connect(lambda: UI_Update.LED_validate(self))
        self.End_spinBox.valueChanged.connect(lambda: UI_Update.LED_validate(self))
        
        self.IR_pushButton.clicked.connect(lambda: Commands.IR_trigger(self))
        self.light_Confirm_pushButton.clicked.connect(lambda: Commands.light_confirm(self))
        self.light_Reset_pushButton.clicked.connect(lambda: Commands.light_reset(self))

        self.title_lineEdit.textChanged.connect(lambda: self.IST_Edit())
        self.addDate_pushButton.clicked.connect(lambda: self.add_date())

        self.ICI_spinBox.valueChanged.connect(lambda: self.ICI_Change())
        self.ISD_spinBox.valueChanged.connect(lambda: self.ISD_Change())
        self.directory_pushButton.clicked.connect(lambda: self.select_directory())



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
