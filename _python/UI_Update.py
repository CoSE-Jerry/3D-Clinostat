import PyQt5
import os
import Settings
from PyQt5 import QtCore, QtGui, QtWidgets



def cycle_start(self):
    self.confirmCycle_pushButton.setText("TERMINATE CYCLE")
    Settings.cycle_running = True

def cycle_END(self):
    self.confirmCycle_pushButton.setText("CONFIRM")
    Settings.cycle_running = False

def imaging_start(self):
    self.core_status_label.setText("Imaging Core Status: IMAGING")
    Settings.imaging = True
    update_imaging(self)
    
    
def snap_complete(self):
    self.core_status_label.setText("Imaging Core Status: IDLE")
    
    snap_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
    self.Image_Frame.setPixmap(QtGui.QPixmap(snap_img))
    Settings.imaging = False
    Settings.trasmitted =0
    update_imaging(self)

def preview_complete(self):
    self.core_status_label.setText("Imaging Core Status: IDLE")
    if(Settings.imaging_mode==1):
        preview_img = PyQt5.QtGui.QImage("../_temp/preview.jpg")
        self.Image_Frame.setPixmap(QtGui.QPixmap(preview_img))
        os.system("gpicview ../_temp/preview.jpg")
    else:
        preview_img = PyQt5.QtGui.QImage("../_temp/preview.png")
        self.Image_Frame.setPixmap(QtGui.QPixmap(preview_img))
        os.system("gpicview ../_temp/preview.png")
    Settings.imaging = False
    Settings.trasmitted =0
    update_imaging(self)

def image_captured(self):
    capture_img = PyQt5.QtGui.QImage(Settings.current_image)
    self.Image_Frame.setPixmap(QtGui.QPixmap(capture_img))
    Settings.trasmitted = 0
    self.core_status_label.setText("Imaging Core Status: IDLE")
    self.Progress_Label.setText("Progress: "+str(Settings.current+1) + "/" + str(Settings.total))
    self.startImaging_pushButton.setEnabled(True)



def sensor_update(self):

    if(Settings.tag_index == 0):
        self.ACC_X_text_label.setText(Settings.ACC_X_text)
        self.ACC_Y_text_label.setText(Settings.ACC_Y_text)
        self.ACC_Z_text_label.setText(Settings.ACC_Z_text)

    elif(Settings.tag_index == 1):
        self.GYRO_X_text_label.setText(Settings.GYRO_X_text)
        self.GYRO_Y_text_label.setText(Settings.GYRO_Y_text)
        self.GYRO_Z_text_label.setText(Settings.GYRO_Z_text)
        
    else:
        self.MAG_X_text_label.setText(Settings.MAG_X_text)
        self.MAG_Y_text_label.setText(Settings.MAG_Y_text)
        self.MAG_Z_text_label.setText(Settings.MAG_Z_text)
    

def LED_validate(self):
    if(self.Start_spinBox.value()>=self.End_spinBox.value()):
        self.light_Confirm_pushButton.setEnabled(False)
    else:
        self.light_Confirm_pushButton.setEnabled(True)

def link(self):
    if(Settings.LINKED):
        Settings.LINKED = False
        self.link_pushButton.setIcon(Settings.broken)
    else:
        Settings.LINKED = True
        self.link_pushButton.setIcon(Settings.linked)

def validate_input(self):
    Settings.total = int(Settings.duration/Settings.interval)
    if(Settings.total>0 and len(Settings.sequence_name)!=0):
        self.startImaging_pushButton.setEnabled(True)
    else:
        self.startImaging_pushButton.setEnabled(False)
    self.Progress_Label.setText("Progress: "+str(Settings.current) + "/" + str(Settings.total))

def update_imaging(self):
    if(Settings.imaging):
        self.snapshot_pushButton.setEnabled(False)
        self.preview_pushButton.setEnabled(False)     
        self.rotate_pushButton.setEnabled(False)
        self.startImaging_pushButton.setEnabled(False)
        
    else:
        self.snapshot_pushButton.setEnabled(True)
        self.preview_pushButton.setEnabled(True)
        self.rotate_pushButton.setEnabled(True)

        validate_input(self)

def transmit_update(self):
    Settings.trasmitted += 1
    self.core_status_label.setText("Recieving Packets: " + str(Settings.trasmitted))

def transmitst(self):
    self.startImaging_pushButton.setEnabled(False)

def timelapse_start(self):
    Settings.timelapse_running = True
    self.snapshot_pushButton.setEnabled(False)
    self.preview_pushButton.setEnabled(False)     
    self.rotate_pushButton.setEnabled(False)

    self.title_lineEdit.setEnabled(False)
    self.addDate_pushButton.setEnabled(False)
    self.ICI_spinBox.setEnabled(False)
    self.ISD_spinBox.setEnabled(False)
    self.directory_pushButton.setEnabled(False)
    self.x_resolution_spinBox.setEnabled(False)
    self.y_resolution_spinBox.setEnabled(False)
    self.PNG_radioButton.setEnabled(False)
    self.JPG_radioButton.setEnabled(False)

    self.startImaging_pushButton.setText("TERMINATE TIMELAPSE")

    self.core_status_label.setText("Imaging Core Status: IMAGING")
    self.Progress_Bar.setMaximum(Settings.total)
    self.Progress_Bar.setMinimum(0)

def timelapse_end(self):
    Settings.timelapse_running = True
    self.snapshot_pushButton.setEnabled(True)
    self.preview_pushButton.setEnabled(True)     
    self.rotate_pushButton.setEnabled(True)

    self.title_lineEdit.setEnabled(True)
    self.addDate_pushButton.setEnabled(True)
    self.ICI_spinBox.setEnabled(True)
    self.ISD_spinBox.setEnabled(True)
    self.directory_pushButton.setEnabled(True)
    self.x_resolution_spinBox.setEnabled(True)
    self.y_resolution_spinBox.setEnabled(True)
    self.PNG_radioButton.setEnabled(True)
    self.JPG_radioButton.setEnabled(True)
    self.startImaging_pushButton.setText("START TIMELAPSE")

    self.core_status_label.setText("Imaging Core Status: IDLE")    

        
