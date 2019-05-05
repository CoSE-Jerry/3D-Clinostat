import PyQt5
import os
#import sys
from PyQt5 import QtCore, QtGui, QtWidgets

def snap_complete(self):
    snap_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
    self.Image_Frame.setPixmap(QtGui.QPixmap(snap_img))
    #self.Snapshot.setText("Snapshot")
    #self.Snapshot.setEnabled(True)

def Preview_complete(self):
    preview_img = PyQt5.QtGui.QImage("../_temp/preview.jpg")
    self.Image_Frame.setPixmap(QtGui.QPixmap(preview_img))
    os.system("gpicview ../_temp/preview.jpg")
    
    #self.Snapshot.setText("Snapshot")
    #self.Snapshot.setEnabled(True)
