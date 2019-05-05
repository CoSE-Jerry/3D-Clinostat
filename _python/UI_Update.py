import PyQt5
import os
import Settings
from PyQt5 import QtCore, QtGui, QtWidgets

def snap_complete(self):
    snap_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
    self.Image_Frame.setPixmap(QtGui.QPixmap(snap_img))
    #self.Snapshot.setText("Snapshot")
    #self.Snapshot.setEnabled(True)

def preview_complete(self):
    preview_img = PyQt5.QtGui.QImage("../_temp/preview.jpg")
    self.Image_Frame.setPixmap(QtGui.QPixmap(preview_img))
    os.system("gpicview ../_temp/preview.jpg")
    
    #self.Snapshot.setText("Snapshot")
    #self.Snapshot.setEnabled(True)

def sensor_update(self):
    self.ACC_X_text_label.setText(Settings.ACC_X_text)
    self.ACC_Y_text_label.setText(Settings.ACC_Y_text)
    self.ACC_Z_text_label.setText(Settings.ACC_Z_text)

    self.GYRO_X_text_label.setText(Settings.GYRO_X_text)
    self.GYRO_Y_text_label.setText(Settings.GYRO_Y_text)
    self.GYRO_Z_text_label.setText(Settings.GYRO_Z_text)

    self.MAG_X_text_label.setText(Settings.MAG_X_text)
    self.MAG_Y_text_label.setText(Settings.MAG_Y_text)
    self.MAG_Z_text_label.setText(Settings.MAG_Z_text)
    
