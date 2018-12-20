# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clinostat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../_image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 29, 310, 310))
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(3)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../_image/Background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 421, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.BRT_spinBox = QtWidgets.QSpinBox(self.tab)
        self.BRT_spinBox.setGeometry(QtCore.QRect(30, 360, 61, 22))
        self.BRT_spinBox.setMinimum(1)
        self.BRT_spinBox.setMaximum(255)
        self.BRT_spinBox.setProperty("value", 50)
        self.BRT_spinBox.setObjectName("BRT_spinBox")
        self.BRT_lable = QtWidgets.QLabel(self.tab)
        self.BRT_lable.setGeometry(QtCore.QRect(30, 330, 81, 31))
        self.BRT_lable.setObjectName("BRT_lable")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(10, 10, 391, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.coreImage = QtWidgets.QLabel(self.frame)
        self.coreImage.setGeometry(QtCore.QRect(20, -40, 350, 350))
        self.coreImage.setText("")
        self.coreImage.setPixmap(QtGui.QPixmap("../_image/Core.png"))
        self.coreImage.setScaledContents(True)
        self.coreImage.setObjectName("coreImage")
        self.bottomColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.bottomColor_comboBox.setGeometry(QtCore.QRect(280, 30, 91, 21))
        self.bottomColor_comboBox.setObjectName("bottomColor_comboBox")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.IR_pushButton = QtWidgets.QPushButton(self.frame)
        self.IR_pushButton.setGeometry(QtCore.QRect(10, 260, 141, 31))
        self.IR_pushButton.setObjectName("IR_pushButton")
        self.rightColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.rightColor_comboBox.setGeometry(QtCore.QRect(280, 230, 91, 21))
        self.rightColor_comboBox.setObjectName("rightColor_comboBox")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.leftColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.leftColor_comboBox.setGeometry(QtCore.QRect(10, 220, 91, 21))
        self.leftColor_comboBox.setObjectName("leftColor_comboBox")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.topColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.topColor_comboBox.setGeometry(QtCore.QRect(20, 30, 91, 21))
        self.topColor_comboBox.setObjectName("topColor_comboBox")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(200, 310, 141, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(270, 340, 21, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(170, 340, 21, 21))
        self.label_10.setObjectName("label_10")
        self.G_spinBox = QtWidgets.QSpinBox(self.tab)
        self.G_spinBox.setGeometry(QtCore.QRect(290, 340, 61, 22))
        self.G_spinBox.setMaximum(255)
        self.G_spinBox.setObjectName("G_spinBox")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(170, 370, 21, 21))
        self.label_11.setObjectName("label_11")
        self.B_spinBox = QtWidgets.QSpinBox(self.tab)
        self.B_spinBox.setGeometry(QtCore.QRect(190, 370, 61, 22))
        self.B_spinBox.setMaximum(255)
        self.B_spinBox.setObjectName("B_spinBox")
        self.R_spinBox = QtWidgets.QSpinBox(self.tab)
        self.R_spinBox.setGeometry(QtCore.QRect(190, 340, 61, 22))
        self.R_spinBox.setMaximum(255)
        self.R_spinBox.setObjectName("R_spinBox")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(270, 370, 21, 21))
        self.label_12.setObjectName("label_12")
        self.W_spinBox = QtWidgets.QSpinBox(self.tab)
        self.W_spinBox.setGeometry(QtCore.QRect(290, 370, 61, 22))
        self.W_spinBox.setMaximum(255)
        self.W_spinBox.setObjectName("W_spinBox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.inner_verticalSlider = QtWidgets.QSlider(self.tab_2)
        self.inner_verticalSlider.setGeometry(QtCore.QRect(49, 10, 21, 291))
        self.inner_verticalSlider.setMinimum(3)
        self.inner_verticalSlider.setMaximum(15)
        self.inner_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.inner_verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.inner_verticalSlider.setTickInterval(1)
        self.inner_verticalSlider.setObjectName("inner_verticalSlider")
        self.outer_verticalSlider = QtWidgets.QSlider(self.tab_2)
        self.outer_verticalSlider.setGeometry(QtCore.QRect(170, 10, 21, 291))
        self.outer_verticalSlider.setMinimum(3)
        self.outer_verticalSlider.setMaximum(15)
        self.outer_verticalSlider.setTracking(True)
        self.outer_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.outer_verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.outer_verticalSlider.setTickInterval(1)
        self.outer_verticalSlider.setObjectName("outer_verticalSlider")
        self.inner_spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.inner_spinBox.setGeometry(QtCore.QRect(10, 340, 101, 31))
        self.inner_spinBox.setMinimum(3)
        self.inner_spinBox.setMaximum(15)
        self.inner_spinBox.setObjectName("inner_spinBox")
        self.outer_spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.outer_spinBox.setGeometry(QtCore.QRect(130, 340, 101, 31))
        self.outer_spinBox.setMinimum(3)
        self.outer_spinBox.setMaximum(15)
        self.outer_spinBox.setObjectName("outer_spinBox")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(160, 300, 51, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(40, 300, 51, 21))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(93, 190, 51, 141))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(250, 20, 141, 361))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_3.setGeometry(QtCore.QRect(20, 70, 101, 22))
        self.spinBox_3.setPrefix("")
        self.spinBox_3.setMinimum(-200)
        self.spinBox_3.setMaximum(200)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.label_2.setObjectName("label_2")
        self.spinBox_4 = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_4.setGeometry(QtCore.QRect(20, 120, 101, 22))
        self.spinBox_4.setPrefix("")
        self.spinBox_4.setMinimum(100)
        self.spinBox_4.setMaximum(1000)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_5.setGeometry(QtCore.QRect(20, 170, 101, 22))
        self.spinBox_5.setMaximum(500)
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 111, 21))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 111, 21))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(15, 20, 111, 21))
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(10, 200, 111, 21))
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 310, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(10, 250, 111, 21))
        self.label_14.setObjectName("label_14")
        self.spinBox_7 = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_7.setGeometry(QtCore.QRect(20, 270, 101, 22))
        self.spinBox_7.setObjectName("spinBox_7")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 220, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_link = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_link.setGeometry(QtCore.QRect(102, 155, 30, 30))
        self.pushButton_link.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../_image/Link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_link.setIcon(icon1)
        self.pushButton_link.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_link.setObjectName("pushButton_link")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(93, 10, 51, 141))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 265, 30, 30))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../_image/Reversal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 260, 30, 30))
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 391, 331))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Image_Title = QtWidgets.QLabel(self.layoutWidget_2)
        self.Image_Title.setObjectName("Image_Title")
        self.verticalLayout.addWidget(self.Image_Title)
        self.IST_Editor = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.IST_Editor.setEnabled(True)
        self.IST_Editor.setObjectName("IST_Editor")
        self.verticalLayout.addWidget(self.IST_Editor)
        self.Image_Interval = QtWidgets.QLabel(self.layoutWidget_2)
        self.Image_Interval.setObjectName("Image_Interval")
        self.verticalLayout.addWidget(self.Image_Interval)
        self.ICI_spinBox = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.ICI_spinBox.setEnabled(False)
        self.ICI_spinBox.setMaximum(9999999)
        self.ICI_spinBox.setObjectName("ICI_spinBox")
        self.verticalLayout.addWidget(self.ICI_spinBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Image_Duration = QtWidgets.QLabel(self.layoutWidget_2)
        self.Image_Duration.setObjectName("Image_Duration")
        self.verticalLayout_2.addWidget(self.Image_Duration)
        self.ISD_spinBox = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.ISD_spinBox.setEnabled(False)
        self.ISD_spinBox.setMaximum(9999999)
        self.ISD_spinBox.setObjectName("ISD_spinBox")
        self.verticalLayout_2.addWidget(self.ISD_spinBox)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        spacerItem = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 350, 411, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Progress_Label = QtWidgets.QLabel(self.layoutWidget)
        self.Progress_Label.setObjectName("Progress_Label")
        self.verticalLayout_6.addWidget(self.Progress_Label)
        self.Progress_Bar = QtWidgets.QProgressBar(self.layoutWidget)
        self.Progress_Bar.setEnabled(False)
        self.Progress_Bar.setProperty("value", 0)
        self.Progress_Bar.setObjectName("Progress_Bar")
        self.verticalLayout_6.addWidget(self.Progress_Bar)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(470, 350, 131, 91))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.JPG = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.JPG.setChecked(True)
        self.JPG.setObjectName("JPG")
        self.verticalLayout_12.addWidget(self.JPG)
        self.PNG = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.PNG.setObjectName("PNG")
        self.verticalLayout_12.addWidget(self.PNG)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(620, 350, 161, 51))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Snapshot = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.Snapshot.setEnabled(True)
        self.Snapshot.setObjectName("Snapshot")
        self.verticalLayout_13.addWidget(self.Snapshot)
        self.Cooling = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.Cooling.setEnabled(True)
        self.Cooling.setObjectName("Cooling")
        self.verticalLayout_13.addWidget(self.Cooling)
        self.startImaging_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startImaging_pushButton.setEnabled(False)
        self.startImaging_pushButton.setGeometry(QtCore.QRect(609, 410, 171, 31))
        self.startImaging_pushButton.setObjectName("startImaging_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Directory.setEnabled(False)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCreate_Timelapse = QtWidgets.QAction(MainWindow)
        self.actionCreate_Timelapse.setObjectName("actionCreate_Timelapse")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlashLapse Commad Point"))
        self.BRT_lable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Brightness:</span></p></body></html>"))
        self.bottomColor_comboBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.bottomColor_comboBox.setItemText(1, _translate("MainWindow", "RED"))
        self.bottomColor_comboBox.setItemText(2, _translate("MainWindow", "GREEN"))
        self.bottomColor_comboBox.setItemText(3, _translate("MainWindow", "BLUE"))
        self.bottomColor_comboBox.setItemText(4, _translate("MainWindow", "WHITE"))
        self.bottomColor_comboBox.setItemText(5, _translate("MainWindow", "CUSTOM"))
        self.IR_pushButton.setText(_translate("MainWindow", "INFRARED:OFF"))
        self.rightColor_comboBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.rightColor_comboBox.setItemText(1, _translate("MainWindow", "RED"))
        self.rightColor_comboBox.setItemText(2, _translate("MainWindow", "GREEN"))
        self.rightColor_comboBox.setItemText(3, _translate("MainWindow", "BLUE"))
        self.rightColor_comboBox.setItemText(4, _translate("MainWindow", "WHITE"))
        self.rightColor_comboBox.setItemText(5, _translate("MainWindow", "CUSTOM"))
        self.leftColor_comboBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.leftColor_comboBox.setItemText(1, _translate("MainWindow", "RED"))
        self.leftColor_comboBox.setItemText(2, _translate("MainWindow", "GREEN"))
        self.leftColor_comboBox.setItemText(3, _translate("MainWindow", "BLUE"))
        self.leftColor_comboBox.setItemText(4, _translate("MainWindow", "WHITE"))
        self.leftColor_comboBox.setItemText(5, _translate("MainWindow", "CUSTOM"))
        self.topColor_comboBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.topColor_comboBox.setItemText(1, _translate("MainWindow", "RED"))
        self.topColor_comboBox.setItemText(2, _translate("MainWindow", "GREEN"))
        self.topColor_comboBox.setItemText(3, _translate("MainWindow", "BLUE"))
        self.topColor_comboBox.setItemText(4, _translate("MainWindow", "WHITE"))
        self.topColor_comboBox.setItemText(5, _translate("MainWindow", "CUSTOM"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Custom RGBW:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">G:</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">R:</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">B:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">W:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "LIGHTING"))
        self.inner_spinBox.setSuffix(_translate("MainWindow", " RPM"))
        self.outer_spinBox.setSuffix(_translate("MainWindow", " RPM"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">OUTER</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">INNER</span></p></body></html>"))
        self.spinBox_3.setSuffix(_translate("MainWindow", " ma"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Current Delta:</p></body></html>"))
        self.spinBox_4.setSuffix(_translate("MainWindow", " ms"))
        self.spinBox_5.setSuffix(_translate("MainWindow", " ms"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Pulse Width:</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Pause Interval:</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Expert Controls</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Set Microstep:</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "APPLY"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Manual RPM:</p></body></html>"))
        self.spinBox_7.setSuffix(_translate("MainWindow", " RPM"))
        self.comboBox.setItemText(0, _translate("MainWindow", "FULL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1/2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "1/4"))
        self.comboBox.setItemText(3, _translate("MainWindow", "1/8"))
        self.comboBox.setItemText(4, _translate("MainWindow", "1/16"))
        self.comboBox.setItemText(5, _translate("MainWindow", "1/32"))
        self.comboBox.setItemText(6, _translate("MainWindow", "1/64"))
        self.comboBox.setItemText(7, _translate("MainWindow", "1/128"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "MOTION"))
        self.Image_Title.setText(_translate("MainWindow", "Image Sequence Title"))
        self.Image_Interval.setText(_translate("MainWindow", "Image Capture Interval"))
        self.ICI_spinBox.setSuffix(_translate("MainWindow", " s"))
        self.Image_Duration.setText(_translate("MainWindow", "Image Sequence Duration"))
        self.ISD_spinBox.setSuffix(_translate("MainWindow", " min"))
        self.Progress_Label.setText(_translate("MainWindow", "Progress:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "IMAGING"))
        self.JPG.setText(_translate("MainWindow", "JPG"))
        self.PNG.setText(_translate("MainWindow", "PNG"))
        self.Snapshot.setText(_translate("MainWindow", "SNAPSHOT"))
        self.Cooling.setText(_translate("MainWindow", "COOLING:OFF"))
        self.startImaging_pushButton.setText(_translate("MainWindow", "START IMAGING"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCreate_Timelapse.setText(_translate("MainWindow", "Create Timelapse"))

