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
        MainWindow.resize(799, 480)
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
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 421, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.from_spinBox = QtWidgets.QTimeEdit(self.tab)
        self.from_spinBox.setEnabled(False)
        self.from_spinBox.setGeometry(QtCore.QRect(260, 325, 101, 25))
        self.from_spinBox.setObjectName("from_spinBox")
        self.lgtSchedule_pushButton = QtWidgets.QPushButton(self.tab)
        self.lgtSchedule_pushButton.setEnabled(False)
        self.lgtSchedule_pushButton.setGeometry(QtCore.QRect(365, 330, 40, 40))
        self.lgtSchedule_pushButton.setCheckable(False)
        self.lgtSchedule_pushButton.setAutoDefault(False)
        self.lgtSchedule_pushButton.setDefault(True)
        self.lgtSchedule_pushButton.setFlat(False)
        self.lgtSchedule_pushButton.setObjectName("lgtSchedule_pushButton")
        self.to_spinBox = QtWidgets.QTimeEdit(self.tab)
        self.to_spinBox.setEnabled(False)
        self.to_spinBox.setGeometry(QtCore.QRect(260, 355, 101, 25))
        self.to_spinBox.setObjectName("to_spinBox")
        self.BRT_spinBox = QtWidgets.QSpinBox(self.tab)
        self.BRT_spinBox.setGeometry(QtCore.QRect(10, 345, 61, 22))
        self.BRT_spinBox.setMinimum(1)
        self.BRT_spinBox.setMaximum(255)
        self.BRT_spinBox.setProperty("value", 50)
        self.BRT_spinBox.setObjectName("BRT_spinBox")
        self.BRT_lable = QtWidgets.QLabel(self.tab)
        self.BRT_lable.setGeometry(QtCore.QRect(10, 320, 81, 21))
        self.BRT_lable.setObjectName("BRT_lable")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(100, 325, 101, 51))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.constantLGT_radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_11)
        self.constantLGT_radioButton.setChecked(True)
        self.constantLGT_radioButton.setObjectName("constantLGT_radioButton")
        self.verticalLayout_5.addWidget(self.constantLGT_radioButton)
        self.scheduleLGT_radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_11)
        self.scheduleLGT_radioButton.setEnabled(False)
        self.scheduleLGT_radioButton.setObjectName("scheduleLGT_radioButton")
        self.verticalLayout_5.addWidget(self.scheduleLGT_radioButton)
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
        self.topColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.topColor_comboBox.setGeometry(QtCore.QRect(280, 30, 91, 21))
        self.topColor_comboBox.setObjectName("topColor_comboBox")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.IR_pushButton = QtWidgets.QPushButton(self.frame)
        self.IR_pushButton.setGeometry(QtCore.QRect(10, 260, 141, 31))
        self.IR_pushButton.setObjectName("IR_pushButton")
        self.rightColor__comboBox = QtWidgets.QComboBox(self.frame)
        self.rightColor__comboBox.setGeometry(QtCore.QRect(280, 230, 91, 21))
        self.rightColor__comboBox.setObjectName("rightColor__comboBox")
        self.rightColor__comboBox.addItem("")
        self.rightColor__comboBox.addItem("")
        self.rightColor__comboBox.addItem("")
        self.rightColor__comboBox.addItem("")
        self.rightColor__comboBox.addItem("")
        self.rightColor__comboBox.addItem("")
        self.bottomColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.bottomColor_comboBox.setGeometry(QtCore.QRect(10, 220, 91, 21))
        self.bottomColor_comboBox.setObjectName("bottomColor_comboBox")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.leftColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.leftColor_comboBox.setGeometry(QtCore.QRect(20, 30, 91, 21))
        self.leftColor_comboBox.setObjectName("leftColor_comboBox")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 320, 61, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.to_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.to_label.setObjectName("to_label")
        self.verticalLayout.addWidget(self.to_label)
        self.from_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.from_label.setObjectName("from_label")
        self.verticalLayout.addWidget(self.from_label)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.inner_verticalSlider = QtWidgets.QSlider(self.tab_2)
        self.inner_verticalSlider.setGeometry(QtCore.QRect(49, 10, 21, 291))
        self.inner_verticalSlider.setMaximum(10)
        self.inner_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.inner_verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.inner_verticalSlider.setTickInterval(1)
        self.inner_verticalSlider.setObjectName("inner_verticalSlider")
        self.outer_verticalSlider = QtWidgets.QSlider(self.tab_2)
        self.outer_verticalSlider.setGeometry(QtCore.QRect(170, 10, 21, 291))
        self.outer_verticalSlider.setMaximum(10)
        self.outer_verticalSlider.setTracking(True)
        self.outer_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.outer_verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.outer_verticalSlider.setTickInterval(1)
        self.outer_verticalSlider.setObjectName("outer_verticalSlider")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(260, 330, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setGeometry(QtCore.QRect(20, 340, 81, 31))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setGeometry(QtCore.QRect(140, 340, 81, 31))
        self.spinBox_2.setObjectName("spinBox_2")
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
        self.frame_2.setGeometry(QtCore.QRect(250, 20, 141, 291))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(102, 155, 30, 30))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../_image/Link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(93, 10, 51, 141))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget.addTab(self.tab_2, "")
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
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(630, 350, 151, 41))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Snapshot = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.Snapshot.setEnabled(True)
        self.Snapshot.setObjectName("Snapshot")
        self.verticalLayout_13.addWidget(self.Snapshot)
        self.startImaging_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startImaging_pushButton.setGeometry(QtCore.QRect(609, 400, 171, 41))
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlashLapse Commad Point"))
        self.lgtSchedule_pushButton.setText(_translate("MainWindow", "OK"))
        self.BRT_lable.setText(_translate("MainWindow", "Brightness:"))
        self.constantLGT_radioButton.setText(_translate("MainWindow", "Constant"))
        self.scheduleLGT_radioButton.setText(_translate("MainWindow", "Scheduled"))
        self.topColor_comboBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.topColor_comboBox.setItemText(1, _translate("MainWindow", "WHITE"))
        self.topColor_comboBox.setItemText(2, _translate("MainWindow", "PURPLE"))
        self.topColor_comboBox.setItemText(3, _translate("MainWindow", "RED"))
        self.topColor_comboBox.setItemText(4, _translate("MainWindow", "GREEN"))
        self.topColor_comboBox.setItemText(5, _translate("MainWindow", "BLUE"))
        self.IR_pushButton.setText(_translate("MainWindow", "INFRARED:OFF"))
        self.rightColor__comboBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.rightColor__comboBox.setItemText(1, _translate("MainWindow", "WHITE"))
        self.rightColor__comboBox.setItemText(2, _translate("MainWindow", "PURPLE"))
        self.rightColor__comboBox.setItemText(3, _translate("MainWindow", "RED"))
        self.rightColor__comboBox.setItemText(4, _translate("MainWindow", "GREEN"))
        self.rightColor__comboBox.setItemText(5, _translate("MainWindow", "BLUE"))
        self.bottomColor_comboBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.bottomColor_comboBox.setItemText(1, _translate("MainWindow", "WHITE"))
        self.bottomColor_comboBox.setItemText(2, _translate("MainWindow", "PURPLE"))
        self.bottomColor_comboBox.setItemText(3, _translate("MainWindow", "RED"))
        self.bottomColor_comboBox.setItemText(4, _translate("MainWindow", "GREEN"))
        self.bottomColor_comboBox.setItemText(5, _translate("MainWindow", "BLUE"))
        self.leftColor_comboBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.leftColor_comboBox.setItemText(1, _translate("MainWindow", "WHITE"))
        self.leftColor_comboBox.setItemText(2, _translate("MainWindow", "PURPLE"))
        self.leftColor_comboBox.setItemText(3, _translate("MainWindow", "RED"))
        self.leftColor_comboBox.setItemText(4, _translate("MainWindow", "GREEN"))
        self.leftColor_comboBox.setItemText(5, _translate("MainWindow", "BLUE"))
        self.to_label.setText(_translate("MainWindow", "TO:"))
        self.from_label.setText(_translate("MainWindow", "FROM:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "LIGHTING"))
        self.pushButton.setText(_translate("MainWindow", "CONFIRM"))
        self.spinBox.setSuffix(_translate("MainWindow", " RPM"))
        self.spinBox_2.setSuffix(_translate("MainWindow", " RPM"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">OUTER</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">INNER</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "MOTION"))
        self.JPG.setText(_translate("MainWindow", "JPG"))
        self.PNG.setText(_translate("MainWindow", "PNG"))
        self.Snapshot.setText(_translate("MainWindow", "SNAPSHOT"))
        self.startImaging_pushButton.setText(_translate("MainWindow", "START IMAGING"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCreate_Timelapse.setText(_translate("MainWindow", "Create Timelapse"))

