import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread

from .components import RGBSlider, CMYKSlider, HSVSlider, LabSlider
from Lab1.events import event_manager


class Ui_Lab1_Interpolation(QThread):
    okClicked = False
    
    def setupUi(self, Lab1_Interpolation, r, g, b):
        Lab1_Interpolation.setObjectName("Lab1_Interpolation")
        Lab1_Interpolation.resize(350, 220)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Lab1_Interpolation.sizePolicy().hasHeightForWidth())
        Lab1_Interpolation.setSizePolicy(sizePolicy)
        Lab1_Interpolation.setMinimumSize(QtCore.QSize(350, 300))
        Lab1_Interpolation.setMaximumSize(QtCore.QSize(350, 300))
        self.centralwidget = QtWidgets.QWidget(Lab1_Interpolation)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")


        # SLIDERS
        rgbslider = RGBSlider(self.tab, [r, g, b])
        cmykslider = CMYKSlider(self.tab_2, [r, g, b])

        # cmykslider = Slider(self.tab_2, [r, g, b])

        hsvslider = HSVSlider(self.tab_3, [r, g, b])
        labslider = LabSlider(self.tab_4, [r, g, b])

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.OK_Button = QtWidgets.QPushButton(self.centralwidget)
        self.OK_Button.setObjectName("OK_Button")
        self.horizontalLayout.addWidget(self.OK_Button)
        self.Cancel_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.horizontalLayout.addWidget(self.Cancel_Button)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        Lab1_Interpolation.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Lab1_Interpolation)
        self.statusbar.setObjectName("statusbar")
        Lab1_Interpolation.setStatusBar(self.statusbar)

        self.OK_Button.clicked.connect(lambda: self.Button_clicked(self.OK_Button))
        self.Cancel_Button.clicked.connect(lambda: self.Button_clicked(self.Cancel_Button))

        self.retranslateUi(Lab1_Interpolation)
        self.tabWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(Lab1_Interpolation)


    def Button_clicked(self, b):
        confirm = b.text() == "OK"
        event_manager.trigger("on_confirm_color_change", confirm)


    def retranslateUi(self, Lab1_Interpolation):
        _translate = QtCore.QCoreApplication.translate
        Lab1_Interpolation.setWindowTitle(_translate("Lab1_Interpolation", "Color Interpolation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Lab1_Interpolation", "RGB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Lab1_Interpolation", "CMYK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Lab1_Interpolation", "HSV"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Lab1_Interpolation", "Lab"))
        self.OK_Button.setText(_translate("Lab1_Interpolation", "OK"))
        self.Cancel_Button.setText(_translate("Lab1_Interpolation", "Cancel"))

