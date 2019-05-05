import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

def snap_complete(self):
    snap_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
    self.Image_Frame.setPixmap(QtGui.QPixmap(snap_img))
    #self.Snapshot.setText("Snapshot")
    #self.Snapshot.setEnabled(True)
