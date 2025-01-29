# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lab1_Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PIL import Image
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np
from PyQt5.QtWidgets import QFileDialog

from .components import ImageTransformWidget, ImageDecompositionWidget, ColorConversionWidget
from .Lab1_Interpolation import Ui_Lab1_Interpolation
from Lab1.events import event_manager



def openImage(self):
    # read image from file dialog window
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self.centralwidget, "Open Image", "", "Images (*.jpg);;Images (*.png);;All Files (*)", options=options)
    if fileName:
        print(fileName)
        src = cv2.imread(fileName, cv2.IMREAD_UNCHANGED)
        #afficher l'image originale
        pixmap = QPixmap(fileName)
        self.label_10.setPixmap(pixmap)
        # # afficher l'image R
        # red_channel = src[:, :, 2] #extract red channel
        # cv2.imwrite('red_img.jpg', red_channel)
        # pixmap = QPixmap('red_img.jpg')
        # self.label_7.setPixmap(pixmap)

        # # afficher l'image G
        # green_channel = src[:, :, 1]  # extract green channel
        # cv2.imwrite('green_img.jpg', green_channel)
        # pixmap = QPixmap('green_img.jpg')
        # self.label_8.setPixmap(pixmap)

        # # afficher l'image B
        # blue_channel = src[:, :, 0]  # extract blue channel
        # cv2.imwrite('blue_img.jpg', blue_channel)
        # pixmap = QPixmap('blue_img.jpg')
        # self.label_9.setPixmap(pixmap)

def closeWindow(self):
    pass


class Lab1_UI(object):

    whichForm = False  # false : disc est affiché, true : rectangle est affiché

    def openWindowInterpolation(self, r, g, b):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Lab1_Interpolation()
        self.ui.setupUi(self.window, r, g, b)
        self.window.show()


    def setupUi(self, Lab1_Window):
        Lab1_Window.setObjectName("Lab1_Window")
        Lab1_Window.setEnabled(True)
        Lab1_Window.setMinimumSize(QtCore.QSize(800, 600))
        Lab1_Window.setMaximumSize(QtCore.QSize(1300, 900))
        self.centralwidget = QtWidgets.QWidget(Lab1_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.tabWidget.blockSignals(True)  # just for not showing the initial message
        self.tabWidget.currentChanged.connect(self.onChange)  # changed!

        self.partie1 = ColorConversionWidget()
        self.partie1.setObjectName("partie1")
        self.tabWidget.addTab(self.partie1, "")

        ## PARTIE 2: IMAGE DECOMP
        self.partie2 = ImageDecompositionWidget()
        self.tabWidget.addTab(self.partie2, "")
        self.partie2.setObjectName("partie2")


        self.partie3 = ImageTransformWidget()
        self.partie3.setObjectName("partie3")
        self.tabWidget.addTab(self.partie3, "")

        self.verticalLayout_6.addWidget(self.tabWidget)


        Lab1_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Lab1_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAdd = QtWidgets.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Lab1_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Lab1_Window)
        self.statusbar.setObjectName("statusbar")
        Lab1_Window.setStatusBar(self.statusbar)
        self.actionDis = QtWidgets.QAction(Lab1_Window)
        self.actionDis.setObjectName("actionDis")
        self.actionRectangle = QtWidgets.QAction(Lab1_Window)
        self.actionRectangle.setObjectName("actionRectangle")
        self.actionImage = QtWidgets.QAction(Lab1_Window)
        self.actionImage.setObjectName("actionImage")
        self.actionExit = QtWidgets.QAction(Lab1_Window)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(Lab1_Window)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuAdd.addAction(self.actionDis)
        self.menuAdd.addAction(self.actionRectangle)
        self.menuAdd.addAction(self.actionImage)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionDis.setDisabled(False)
        self.actionRectangle.setDisabled(False)
        self.actionImage.setDisabled(True)
        self.actionDis.triggered.connect(lambda: event_manager.trigger("on_add_shape", "circle"))
        self.actionRectangle.triggered.connect(lambda: event_manager.trigger("on_add_shape", "rectangle"))
        self.actionImage.triggered.connect(self.open_file)
        self.actionExit.triggered.connect(lambda: closeWindow(self))

        event_manager.register("on_confirm_color_change", lambda x: self.window.close())
        self.tabWidget.blockSignals(False)  # now listen the currentChanged signal

        self.retranslateUi(Lab1_Window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Lab1_Window)


    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self.centralwidget,
                                                  "Open Image", "", "Images (*.jpg);;Images (*.png);;All Files (*)",
                                                  options=options)
        if filename:
            image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            event_manager.trigger("on_image_loaded", image)
            event_manager.trigger("on_imagefile_loaded", filename)


    def onChange(self, i):  # changed!
        if self.tabWidget.currentIndex() in [1, 2]:
            self.actionDis.setDisabled(True)
            self.actionRectangle.setDisabled(True)
            self.actionImage.setDisabled(False)
        else:
            self.actionDis.setDisabled(False)
            self.actionRectangle.setDisabled(False)
            self.actionImage.setDisabled(True)


    def retranslateUi(self, Lab1_Window):
        _translate = QtCore.QCoreApplication.translate
        Lab1_Window.setWindowTitle(_translate("Lab1_Window", "Lab1_Window"))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.partie1), _translate("Lab1_Window", "Color Interpolation"))
        # self.label_4.setText(_translate("Lab1_Window", "R Image"))
        # self.label_5.setText(_translate("Lab1_Window", "G Image"))
        # self.label_6.setText(_translate("Lab1_Window", "B Image"))
        # self.label_3.setText(_translate("Lab1_Window", "Original Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.partie2), _translate("Lab1_Window", "Image Decomposition"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.partie3), _translate("Lab1_Window", "Contrast and Brightness"))
        self.menuFile.setTitle(_translate("Lab1_Window", "File"))
        self.menuAdd.setTitle(_translate("Lab1_Window", "Add"))
        self.menuHelp.setTitle(_translate("Lab1_Window", "Help"))
        self.actionDis.setText(_translate("Lab1_Window", "Disc"))
        self.actionRectangle.setText(_translate("Lab1_Window", "Rectangle"))
        self.actionImage.setText(_translate("Lab1_Window", "Image"))
        self.actionExit.setText(_translate("Lab1_Window", "Exit"))
        self.actionAbout.setText(_translate("Lab1_Window", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Lab1_Window = QtWidgets.QMainWindow()
    ui = Ui_Lab1_Window()
    ui.setupUi(Lab1_Window)
    Lab1_Window.show()
    sys.exit(app.exec_())
