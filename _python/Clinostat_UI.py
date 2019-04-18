# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clinostat.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../_image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Image_Frame = QtWidgets.QLabel(self.centralwidget)
        self.Image_Frame.setGeometry(QtCore.QRect(659, 10, 350, 350))
        self.Image_Frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.Image_Frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Image_Frame.setLineWidth(3)
        self.Image_Frame.setText("")
        self.Image_Frame.setPixmap(QtGui.QPixmap("../_image/Background.png"))
        self.Image_Frame.setScaledContents(True)
        self.Image_Frame.setObjectName("Image_Frame")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 631, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.Lighting_tab = QtWidgets.QWidget()
        self.Lighting_tab.setObjectName("Lighting_tab")
        self.BRT_spinBox = QtWidgets.QSpinBox(self.Lighting_tab)
        self.BRT_spinBox.setGeometry(QtCore.QRect(50, 480, 61, 22))
        self.BRT_spinBox.setMinimum(1)
        self.BRT_spinBox.setMaximum(255)
        self.BRT_spinBox.setProperty("value", 50)
        self.BRT_spinBox.setObjectName("BRT_spinBox")
        self.BRT_lable = QtWidgets.QLabel(self.Lighting_tab)
        self.BRT_lable.setGeometry(QtCore.QRect(50, 450, 81, 31))
        self.BRT_lable.setObjectName("BRT_lable")
        self.frame = QtWidgets.QFrame(self.Lighting_tab)
        self.frame.setGeometry(QtCore.QRect(30, 10, 581, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.coreImage = QtWidgets.QLabel(self.frame)
        self.coreImage.setGeometry(QtCore.QRect(100, -20, 401, 411))
        self.coreImage.setText("")
        self.coreImage.setPixmap(QtGui.QPixmap("../_image/Core.png"))
        self.coreImage.setScaledContents(True)
        self.coreImage.setObjectName("coreImage")
        self.bottomColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.bottomColor_comboBox.setGeometry(QtCore.QRect(420, 40, 91, 21))
        self.bottomColor_comboBox.setObjectName("bottomColor_comboBox")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.IR_pushButton = QtWidgets.QPushButton(self.frame)
        self.IR_pushButton.setGeometry(QtCore.QRect(30, 360, 141, 31))
        self.IR_pushButton.setObjectName("IR_pushButton")
        self.rightColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.rightColor_comboBox.setGeometry(QtCore.QRect(420, 290, 91, 21))
        self.rightColor_comboBox.setObjectName("rightColor_comboBox")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.leftColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.leftColor_comboBox.setGeometry(QtCore.QRect(80, 280, 91, 21))
        self.leftColor_comboBox.setObjectName("leftColor_comboBox")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.topColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.topColor_comboBox.setGeometry(QtCore.QRect(100, 50, 91, 21))
        self.topColor_comboBox.setObjectName("topColor_comboBox")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.custom_label = QtWidgets.QLabel(self.Lighting_tab)
        self.custom_label.setGeometry(QtCore.QRect(310, 430, 141, 31))
        self.custom_label.setObjectName("custom_label")
        self.G_label = QtWidgets.QLabel(self.Lighting_tab)
        self.G_label.setGeometry(QtCore.QRect(380, 460, 21, 21))
        self.G_label.setObjectName("G_label")
        self.R_label = QtWidgets.QLabel(self.Lighting_tab)
        self.R_label.setGeometry(QtCore.QRect(280, 460, 21, 21))
        self.R_label.setObjectName("R_label")
        self.G_spinBox = QtWidgets.QSpinBox(self.Lighting_tab)
        self.G_spinBox.setGeometry(QtCore.QRect(400, 460, 61, 22))
        self.G_spinBox.setMaximum(255)
        self.G_spinBox.setObjectName("G_spinBox")
        self.B_label = QtWidgets.QLabel(self.Lighting_tab)
        self.B_label.setGeometry(QtCore.QRect(280, 490, 21, 21))
        self.B_label.setObjectName("B_label")
        self.B_spinBox = QtWidgets.QSpinBox(self.Lighting_tab)
        self.B_spinBox.setGeometry(QtCore.QRect(300, 490, 61, 22))
        self.B_spinBox.setMaximum(255)
        self.B_spinBox.setObjectName("B_spinBox")
        self.R_spinBox = QtWidgets.QSpinBox(self.Lighting_tab)
        self.R_spinBox.setGeometry(QtCore.QRect(300, 460, 61, 22))
        self.R_spinBox.setMaximum(255)
        self.R_spinBox.setObjectName("R_spinBox")
        self.W_label = QtWidgets.QLabel(self.Lighting_tab)
        self.W_label.setGeometry(QtCore.QRect(380, 490, 21, 21))
        self.W_label.setObjectName("W_label")
        self.W_spinBox = QtWidgets.QSpinBox(self.Lighting_tab)
        self.W_spinBox.setGeometry(QtCore.QRect(400, 490, 61, 22))
        self.W_spinBox.setMaximum(255)
        self.W_spinBox.setObjectName("W_spinBox")
        self.tabWidget.addTab(self.Lighting_tab, "")
        self.Frame_tab = QtWidgets.QWidget()
        self.Frame_tab.setObjectName("Frame_tab")
        self.frame_verticalSlider = QtWidgets.QSlider(self.Frame_tab)
        self.frame_verticalSlider.setGeometry(QtCore.QRect(160, 40, 61, 421))
        self.frame_verticalSlider.setMinimum(3)
        self.frame_verticalSlider.setMaximum(150)
        self.frame_verticalSlider.setTracking(True)
        self.frame_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.frame_verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.frame_verticalSlider.setTickInterval(10)
        self.frame_verticalSlider.setObjectName("frame_verticalSlider")
        self.frameReverse_pushButton = QtWidgets.QPushButton(self.Frame_tab)
        self.frameReverse_pushButton.setGeometry(QtCore.QRect(230, 420, 41, 41))
        self.frameReverse_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../_image/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frameReverse_pushButton.setIcon(icon1)
        self.frameReverse_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.frameReverse_pushButton.setObjectName("frameReverse_pushButton")
        self.frame_3 = QtWidgets.QFrame(self.Frame_tab)
        self.frame_3.setGeometry(QtCore.QRect(380, 40, 201, 361))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frameCD_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.frameCD_spinBox.setGeometry(QtCore.QRect(40, 50, 121, 22))
        self.frameCD_spinBox.setPrefix("")
        self.frameCD_spinBox.setMinimum(-200)
        self.frameCD_spinBox.setMaximum(200)
        self.frameCD_spinBox.setObjectName("frameCD_spinBox")
        self.frameCD_label = QtWidgets.QLabel(self.frame_3)
        self.frameCD_label.setGeometry(QtCore.QRect(40, 30, 121, 21))
        self.frameCD_label.setObjectName("frameCD_label")
        self.framePW_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.framePW_spinBox.setGeometry(QtCore.QRect(40, 100, 121, 22))
        self.framePW_spinBox.setPrefix("")
        self.framePW_spinBox.setMinimum(1)
        self.framePW_spinBox.setMaximum(1000)
        self.framePW_spinBox.setProperty("value", 2)
        self.framePW_spinBox.setObjectName("framePW_spinBox")
        self.framePI_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.framePI_spinBox.setGeometry(QtCore.QRect(40, 150, 121, 22))
        self.framePI_spinBox.setMinimum(1)
        self.framePI_spinBox.setMaximum(10000000)
        self.framePI_spinBox.setProperty("value", 380)
        self.framePI_spinBox.setObjectName("framePI_spinBox")
        self.framePW_label = QtWidgets.QLabel(self.frame_3)
        self.framePW_label.setGeometry(QtCore.QRect(40, 80, 121, 21))
        self.framePW_label.setObjectName("framePW_label")
        self.framePI_label = QtWidgets.QLabel(self.frame_3)
        self.framePI_label.setGeometry(QtCore.QRect(40, 130, 121, 21))
        self.framePI_label.setObjectName("framePI_label")
        self.frameEC_label = QtWidgets.QLabel(self.frame_3)
        self.frameEC_label.setGeometry(QtCore.QRect(40, 10, 121, 21))
        self.frameEC_label.setObjectName("frameEC_label")
        self.frameMS_label = QtWidgets.QLabel(self.frame_3)
        self.frameMS_label.setGeometry(QtCore.QRect(40, 180, 121, 21))
        self.frameMS_label.setObjectName("frameMS_label")
        self.frameApply_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.frameApply_pushButton.setGeometry(QtCore.QRect(30, 280, 141, 21))
        self.frameApply_pushButton.setObjectName("frameApply_pushButton")
        self.frameMS_comboBox = QtWidgets.QComboBox(self.frame_3)
        self.frameMS_comboBox.setGeometry(QtCore.QRect(40, 200, 121, 22))
        self.frameMS_comboBox.setObjectName("frameMS_comboBox")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameReset_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.frameReset_pushButton.setGeometry(QtCore.QRect(30, 250, 141, 21))
        self.frameReset_pushButton.setObjectName("frameReset_pushButton")
        self.frame_label = QtWidgets.QLabel(self.Frame_tab)
        self.frame_label.setGeometry(QtCore.QRect(90, 430, 71, 21))
        self.frame_label.setObjectName("frame_label")
        self.frame_spinBox = QtWidgets.QDoubleSpinBox(self.Frame_tab)
        self.frame_spinBox.setGeometry(QtCore.QRect(140, 480, 101, 31))
        self.frame_spinBox.setDecimals(1)
        self.frame_spinBox.setMinimum(0.3)
        self.frame_spinBox.setMaximum(15.0)
        self.frame_spinBox.setSingleStep(0.1)
        self.frame_spinBox.setObjectName("frame_spinBox")
        self.frameErgz_pushButton = QtWidgets.QPushButton(self.Frame_tab)
        self.frameErgz_pushButton.setGeometry(QtCore.QRect(400, 440, 161, 61))
        self.frameErgz_pushButton.setObjectName("frameErgz_pushButton")
        self.frameLink_pushButton = QtWidgets.QPushButton(self.Frame_tab)
        self.frameLink_pushButton.setGeometry(QtCore.QRect(570, 450, 41, 41))
        self.frameLink_pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../_image/Link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frameLink_pushButton.setIcon(icon2)
        self.frameLink_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.frameLink_pushButton.setObjectName("frameLink_pushButton")
        self.tabWidget.addTab(self.Frame_tab, "")
        self.core_tab = QtWidgets.QWidget()
        self.core_tab.setObjectName("core_tab")
        self.coreReverse_pushButton = QtWidgets.QPushButton(self.core_tab)
        self.coreReverse_pushButton.setGeometry(QtCore.QRect(230, 420, 41, 41))
        self.coreReverse_pushButton.setText("")
        self.coreReverse_pushButton.setIcon(icon1)
        self.coreReverse_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.coreReverse_pushButton.setObjectName("coreReverse_pushButton")
        self.core_verticalSlider = QtWidgets.QSlider(self.core_tab)
        self.core_verticalSlider.setGeometry(QtCore.QRect(160, 40, 61, 421))
        self.core_verticalSlider.setMinimum(3)
        self.core_verticalSlider.setMaximum(150)
        self.core_verticalSlider.setTracking(True)
        self.core_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.core_verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.core_verticalSlider.setTickInterval(5)
        self.core_verticalSlider.setObjectName("core_verticalSlider")
        self.core_label = QtWidgets.QLabel(self.core_tab)
        self.core_label.setGeometry(QtCore.QRect(90, 430, 71, 21))
        self.core_label.setObjectName("core_label")
        self.coreErgz_pushButton = QtWidgets.QPushButton(self.core_tab)
        self.coreErgz_pushButton.setGeometry(QtCore.QRect(400, 440, 161, 61))
        self.coreErgz_pushButton.setObjectName("coreErgz_pushButton")
        self.core_spinBox = QtWidgets.QDoubleSpinBox(self.core_tab)
        self.core_spinBox.setGeometry(QtCore.QRect(140, 480, 101, 31))
        self.core_spinBox.setDecimals(1)
        self.core_spinBox.setMinimum(0.3)
        self.core_spinBox.setMaximum(15.0)
        self.core_spinBox.setSingleStep(0.1)
        self.core_spinBox.setObjectName("core_spinBox")
        self.coreLink_pushButton = QtWidgets.QPushButton(self.core_tab)
        self.coreLink_pushButton.setGeometry(QtCore.QRect(570, 450, 41, 41))
        self.coreLink_pushButton.setText("")
        self.coreLink_pushButton.setIcon(icon2)
        self.coreLink_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.coreLink_pushButton.setObjectName("coreLink_pushButton")
        self.frame_4 = QtWidgets.QFrame(self.core_tab)
        self.frame_4.setGeometry(QtCore.QRect(380, 40, 201, 361))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.coreCD_spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.coreCD_spinBox.setGeometry(QtCore.QRect(40, 50, 121, 22))
        self.coreCD_spinBox.setPrefix("")
        self.coreCD_spinBox.setMinimum(-200)
        self.coreCD_spinBox.setMaximum(200)
        self.coreCD_spinBox.setObjectName("coreCD_spinBox")
        self.coreCD_label = QtWidgets.QLabel(self.frame_4)
        self.coreCD_label.setGeometry(QtCore.QRect(40, 30, 121, 21))
        self.coreCD_label.setObjectName("coreCD_label")
        self.corePW_spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.corePW_spinBox.setGeometry(QtCore.QRect(40, 100, 121, 22))
        self.corePW_spinBox.setPrefix("")
        self.corePW_spinBox.setMinimum(1)
        self.corePW_spinBox.setMaximum(1000)
        self.corePW_spinBox.setProperty("value", 2)
        self.corePW_spinBox.setObjectName("corePW_spinBox")
        self.corePI_spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.corePI_spinBox.setGeometry(QtCore.QRect(40, 150, 121, 22))
        self.corePI_spinBox.setMinimum(1)
        self.corePI_spinBox.setMaximum(10000000)
        self.corePI_spinBox.setProperty("value", 380)
        self.corePI_spinBox.setObjectName("corePI_spinBox")
        self.corePW_label = QtWidgets.QLabel(self.frame_4)
        self.corePW_label.setGeometry(QtCore.QRect(40, 80, 121, 21))
        self.corePW_label.setObjectName("corePW_label")
        self.corePI_label = QtWidgets.QLabel(self.frame_4)
        self.corePI_label.setGeometry(QtCore.QRect(40, 130, 121, 21))
        self.corePI_label.setObjectName("corePI_label")
        self.coreEC_label = QtWidgets.QLabel(self.frame_4)
        self.coreEC_label.setGeometry(QtCore.QRect(40, 10, 121, 21))
        self.coreEC_label.setObjectName("coreEC_label")
        self.coreMS_label = QtWidgets.QLabel(self.frame_4)
        self.coreMS_label.setGeometry(QtCore.QRect(40, 180, 121, 21))
        self.coreMS_label.setObjectName("coreMS_label")
        self.coreApply_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.coreApply_pushButton.setGeometry(QtCore.QRect(30, 280, 141, 21))
        self.coreApply_pushButton.setObjectName("coreApply_pushButton")
        self.coreMS_comboBox = QtWidgets.QComboBox(self.frame_4)
        self.coreMS_comboBox.setGeometry(QtCore.QRect(40, 200, 121, 22))
        self.coreMS_comboBox.setObjectName("coreMS_comboBox")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.frameReset_pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.frameReset_pushButton_2.setGeometry(QtCore.QRect(30, 250, 141, 21))
        self.frameReset_pushButton_2.setObjectName("frameReset_pushButton_2")
        self.tabWidget.addTab(self.core_tab, "")
        self.Imaging_tab = QtWidgets.QWidget()
        self.Imaging_tab.setObjectName("Imaging_tab")
        self.layoutWidget_2 = QtWidgets.QWidget(self.Imaging_tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 611, 411))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Image_Title = QtWidgets.QLabel(self.layoutWidget_2)
        self.Image_Title.setObjectName("Image_Title")
        self.verticalLayout.addWidget(self.Image_Title)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.title_lineEdit.setEnabled(True)
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.horizontalLayout_2.addWidget(self.title_lineEdit)
        self.add_Date_pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.add_Date_pushButton.setEnabled(False)
        self.add_Date_pushButton.setObjectName("add_Date_pushButton")
        self.horizontalLayout_2.addWidget(self.add_Date_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
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
        self.layoutWidget = QtWidgets.QWidget(self.Imaging_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 440, 611, 71))
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
        self.tabWidget.addTab(self.Imaging_tab, "")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(840, 360, 161, 91))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.snapshot_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.snapshot_pushButton.setEnabled(True)
        self.snapshot_pushButton.setObjectName("snapshot_pushButton")
        self.verticalLayout_13.addWidget(self.snapshot_pushButton)
        self.Cooling = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.Cooling.setEnabled(True)
        self.Cooling.setObjectName("Cooling")
        self.verticalLayout_13.addWidget(self.Cooling)
        self.startImaging_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startImaging_pushButton.setEnabled(False)
        self.startImaging_pushButton.setGeometry(QtCore.QRect(700, 470, 311, 81))
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
        self.frameMS_comboBox.setCurrentIndex(7)
        self.coreMS_comboBox.setCurrentIndex(7)
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
        self.custom_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Custom RGBW:</span></p></body></html>"))
        self.G_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">G:</span></p></body></html>"))
        self.R_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">R:</span></p></body></html>"))
        self.B_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">B:</span></p></body></html>"))
        self.W_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">W:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Lighting_tab), _translate("MainWindow", "LIGHTING"))
        self.frameCD_spinBox.setSuffix(_translate("MainWindow", " mA"))
        self.frameCD_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Current Offset:</p></body></html>"))
        self.framePW_spinBox.setSuffix(_translate("MainWindow", " ms"))
        self.framePI_spinBox.setSuffix(_translate("MainWindow", " ms"))
        self.framePW_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Pulse Width:</p></body></html>"))
        self.framePI_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Pulse Interval:</p></body></html>"))
        self.frameEC_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Expert Controls</span></p></body></html>"))
        self.frameMS_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Microstepping:</p></body></html>"))
        self.frameApply_pushButton.setText(_translate("MainWindow", "APPLY"))
        self.frameMS_comboBox.setCurrentText(_translate("MainWindow", "128"))
        self.frameMS_comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.frameMS_comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.frameMS_comboBox.setItemText(2, _translate("MainWindow", "4"))
        self.frameMS_comboBox.setItemText(3, _translate("MainWindow", "8"))
        self.frameMS_comboBox.setItemText(4, _translate("MainWindow", "16"))
        self.frameMS_comboBox.setItemText(5, _translate("MainWindow", "32"))
        self.frameMS_comboBox.setItemText(6, _translate("MainWindow", "64"))
        self.frameMS_comboBox.setItemText(7, _translate("MainWindow", "128"))
        self.frameReset_pushButton.setText(_translate("MainWindow", "RESET"))
        self.frame_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">FRAME</span></p></body></html>"))
        self.frameErgz_pushButton.setText(_translate("MainWindow", "ENERGIZE COILS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Frame_tab), _translate("MainWindow", "FRAME"))
        self.core_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CORE</span></p></body></html>"))
        self.coreErgz_pushButton.setText(_translate("MainWindow", "ENERGIZE COILS"))
        self.coreCD_spinBox.setSuffix(_translate("MainWindow", " mA"))
        self.coreCD_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Current Offset:</p></body></html>"))
        self.corePW_spinBox.setSuffix(_translate("MainWindow", " ms"))
        self.corePI_spinBox.setSuffix(_translate("MainWindow", " ms"))
        self.corePW_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Pulse Width:</p></body></html>"))
        self.corePI_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Pulse Interval:</p></body></html>"))
        self.coreEC_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Expert Controls</span></p></body></html>"))
        self.coreMS_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Microstepping:</p></body></html>"))
        self.coreApply_pushButton.setText(_translate("MainWindow", "APPLY"))
        self.coreMS_comboBox.setCurrentText(_translate("MainWindow", "128"))
        self.coreMS_comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.coreMS_comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.coreMS_comboBox.setItemText(2, _translate("MainWindow", "4"))
        self.coreMS_comboBox.setItemText(3, _translate("MainWindow", "8"))
        self.coreMS_comboBox.setItemText(4, _translate("MainWindow", "16"))
        self.coreMS_comboBox.setItemText(5, _translate("MainWindow", "32"))
        self.coreMS_comboBox.setItemText(6, _translate("MainWindow", "64"))
        self.coreMS_comboBox.setItemText(7, _translate("MainWindow", "128"))
        self.frameReset_pushButton_2.setText(_translate("MainWindow", "RESET"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.core_tab), _translate("MainWindow", "CORE"))
        self.Image_Title.setText(_translate("MainWindow", "Image Sequence Title"))
        self.add_Date_pushButton.setText(_translate("MainWindow", "Add Date"))
        self.Image_Interval.setText(_translate("MainWindow", "Image Capture Interval"))
        self.ICI_spinBox.setSuffix(_translate("MainWindow", " s"))
        self.Image_Duration.setText(_translate("MainWindow", "Image Sequence Duration"))
        self.ISD_spinBox.setSuffix(_translate("MainWindow", " min"))
        self.Progress_Label.setText(_translate("MainWindow", "Progress:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Imaging_tab), _translate("MainWindow", "IMAGING"))
        self.snapshot_pushButton.setText(_translate("MainWindow", "SNAPSHOT"))
        self.Cooling.setText(_translate("MainWindow", "COOLING:OFF"))
        self.startImaging_pushButton.setText(_translate("MainWindow", "START IMAGING"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCreate_Timelapse.setText(_translate("MainWindow", "Create Timelapse"))


