
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from Lab3.events import event_manager
from Lab3.utils import np_array_to_pixmap
from Lab3.views.rgb_color_picker import RGBColorPicker


class Lab3_Window(object):
    def openWindowFillColor(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = RGBColorPicker()
        # self.ui.my_signal.connect(lambda x: self.window.close())
        self.ui.setup_ui(self.window, "on_fill_color_changed")
        self.window.show()

    def openWindowBoundaryColor(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = RGBColorPicker()
        # self.ui.my_signal.connect(lambda x: self.window.close())
        self.ui.setup_ui(self.window, "on_boundary_color_changed")
        self.window.show()

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle('Missing value')
        msg.setText('Enter the radius of the circle to draw')
        msg.exec_()


    def open_image(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Open Image", "", "Images (*.png)", options=options)
        event_manager.trigger("on_load_image", filename)


    def closeFillColorWindow(self, r, g, b, boolbutton):
        if boolbutton: #ok button
            self.R = r
            self.G = g
            self.B = b
        self.window.close()

    def closeBoundaryColorWindow(self):
       self.window.close()


    def open_rgb_picker(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = RGBColorPicker()
        # self.ui.my_signal.connect(lambda x: self.window.close())
        self.ui.setup_ui(self.window, "on_shape_color_changed")
        self.window.show()


    def setupUi(self, Lab3_Window):
        Lab3_Window.setObjectName("Lab3_Window")
        Lab3_Window.resize(1300, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Lab3_Window.sizePolicy().hasHeightForWidth())
        Lab3_Window.setSizePolicy(sizePolicy)
        Lab3_Window.setMinimumSize(QtCore.QSize(1300, 700))
        Lab3_Window.setMaximumSize(QtCore.QSize(1300, 700))
        self.centralwidget = QtWidgets.QWidget(Lab3_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        sizeX = 1250
        sizeY = 490
        self.frame_8.setMinimumSize(QtCore.QSize(1275, 510))
        self.frame_8.setMaximumSize(QtCore.QSize(1275, 510))
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.canvas_label = QtWidgets.QLabel(self.frame_8)
        self.canvas_label.setText("")
        self.canvas_label.setObjectName("label")
        self.canvas_label.setMinimumSize(QtCore.QSize(sizeX, sizeY))
        self.canvas_label.setMaximumSize(QtCore.QSize(sizeX, sizeY))
        self.gridLayout_4.addWidget(self.canvas_label, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_8, 1, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        #self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        #self.pushButton_3.setSizePolicy(sizePolicy)
        #self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        #self.pushButton_3.setObjectName("pushButton_3")
        #self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.gridLayout_6.addWidget(self.frame_2, 1, 0, 1, 1)

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.shape_type = QtWidgets.QComboBox(self.groupBox_4)
        self.shape_type.addItems(["Circle", "Line", "Rectangle", "Ellispis"])
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shape_type.sizePolicy().hasHeightForWidth())
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.shape_type)
        self.gridLayout_6.addLayout(self.formLayout, 0, 0, 1, 1)


        # Color picker
        self.shape_color_form = QtWidgets.QFormLayout()
        self.shape_color_form.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.shape_color_form.setObjectName("shape_color_form")
        self.shape_color_label = QtWidgets.QLabel("Color", self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shape_color_label.sizePolicy().hasHeightForWidth())
        self.shape_color_label.setSizePolicy(sizePolicy)
        self.shape_color_label.setMinimumSize(QtCore.QSize(74, 0))
        self.shape_color_label.setObjectName("label_8")
        self.shape_color_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.shape_color_label)
        self.shape_color_btn = QtWidgets.QPushButton("Color", self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shape_color_btn.sizePolicy().hasHeightForWidth())
        self.shape_color_btn.setSizePolicy(sizePolicy)
        self.shape_color_btn.setObjectName("pushButton")
        self.shape_color_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.shape_color_btn)
        self.gridLayout_6.addLayout(self.shape_color_form, 1, 0, 1, 1)

        self.horizontalLayout_3.addWidget(self.groupBox_4)


        self.boundaryFillGroupBox = QtWidgets.QGroupBox(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boundaryFillGroupBox.sizePolicy().hasHeightForWidth())
        self.boundaryFillGroupBox.setSizePolicy(sizePolicy)
        self.boundaryFillGroupBox.setMinimumSize(QtCore.QSize(250, 0))
        self.boundaryFillGroupBox.setObjectName("groupBox")
        self.boundaryFillVerticalLayout = QtWidgets.QVBoxLayout(self.boundaryFillGroupBox)
        self.boundaryFillVerticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.floodfill_low_label = QtWidgets.QLabel(self.boundaryFillGroupBox)
        self.floodfill_low_label.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.floodfill_low_label)
        self.floodfill_low_slider = QtWidgets.QSlider(self.boundaryFillGroupBox)
        self.floodfill_low_slider.setMaximum(50)
        self.floodfill_low_slider.setOrientation(QtCore.Qt.Horizontal)
        self.floodfill_low_slider.setObjectName("horizontalSlider")
        self.horizontalLayout_4.addWidget(self.floodfill_low_slider)
        self.lowthresh_label = QtWidgets.QLabel(self.boundaryFillGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowthresh_label.sizePolicy().hasHeightForWidth())
        self.lowthresh_label.setSizePolicy(sizePolicy)
        self.lowthresh_label.setMinimumSize(QtCore.QSize(20, 0))
        self.lowthresh_label.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.lowthresh_label)
        self.boundaryFillVerticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.boundaryFillGroupBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.floodfill_high_slider = QtWidgets.QSlider(self.boundaryFillGroupBox)
        self.floodfill_high_slider.setMaximum(200)
        self.floodfill_high_slider.setOrientation(QtCore.Qt.Horizontal)
        self.floodfill_high_slider.setObjectName("horizontalSlider_2")
        self.horizontalLayout.addWidget(self.floodfill_high_slider)
        self.highthresh_label = QtWidgets.QLabel(self.boundaryFillGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.highthresh_label.sizePolicy().hasHeightForWidth())
        self.highthresh_label.setSizePolicy(sizePolicy)
        self.highthresh_label.setMinimumSize(QtCore.QSize(20, 0))
        self.highthresh_label.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.highthresh_label)
        self.boundaryFillVerticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_15 = QtWidgets.QLabel(self.boundaryFillGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(20, 0))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.boundaryFillVerticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.boundaryFillGroupBox)

        # FLOOD FILL GROUP
        self.floodFillGroupBox = QtWidgets.QGroupBox(self.frame_7)
        self.floodFillGroupBox.setObjectName("groupBox_2")
        self.floodFillVerticalLayout = QtWidgets.QVBoxLayout(self.floodFillGroupBox)
        self.floodFillVerticalLayout.setObjectName("verticalLayout_2")
        self.boundaryFillRadioButton = QtWidgets.QRadioButton(self.floodFillGroupBox)
        self.boundaryFillRadioButton.setChecked(True)
        self.boundaryFillRadioButton.setObjectName("radioButton")
        self.floodFillVerticalLayout.addWidget(self.boundaryFillRadioButton)
        self.floodFillRadioButton = QtWidgets.QRadioButton(self.floodFillGroupBox)
        self.floodFillRadioButton.setObjectName("radioButton_2")
        self.floodFillVerticalLayout.addWidget(self.floodFillRadioButton)
        self.horizontalLayout_3.addWidget(self.floodFillGroupBox)


        # BOUNDARY FILL GROUP
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_7)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(74, 0))
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.fillColorBtn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillColorBtn.sizePolicy().hasHeightForWidth())
        self.fillColorBtn.setSizePolicy(sizePolicy)
        self.fillColorBtn.setObjectName("pushButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fillColorBtn)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.boundaryColorBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.boundaryColorBtn.setObjectName("pushButton_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.boundaryColorBtn)
        self.gridLayout.addLayout(self.formLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout_2.addWidget(self.frame_7, 0, 0, 1, 1)
        Lab3_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Lab3_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Lab3_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Lab3_Window)
        self.statusbar.setObjectName("statusbar")
        Lab3_Window.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(Lab3_Window)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.actionExit.triggered.connect(self.open_image)
        self.menubar.addAction(self.menuFile.menuAction())

        self.shape_type.currentTextChanged.connect(lambda x: event_manager.trigger("on_shape_type_changed", x))
        self.canvas_label.mouseMoveEvent = lambda event: event_manager.trigger("on_mouse_click_move", event.pos().x(), event.pos().y())

        self.floodFillRadioButton.clicked.connect(lambda x: event_manager.trigger("set_fill_method", 'Flood'))
        self.boundaryFillRadioButton.clicked.connect(lambda x: event_manager.trigger("set_fill_method", 'Boundary'))
        self.canvas_label.mouseReleaseEvent = lambda event: self.mouse_click(event, released=True)
        self.shape_color_btn.clicked.connect(self.open_rgb_picker)

        self.fillColorBtn.clicked.connect(self.openWindowFillColor)
        self.boundaryColorBtn.clicked.connect(self.openWindowBoundaryColor)

        self.retranslateUi(Lab3_Window)
        self.floodfill_low_slider.valueChanged['int'].connect(self.update_low_threshold)
        self.floodfill_high_slider.valueChanged['int'].connect(self.update_high_threshold)
        QtCore.QMetaObject.connectSlotsByName(Lab3_Window)


    def update_low_threshold(self, val):
        self.lowthresh_label.setNum(val)
        event_manager.trigger("on_floodfill_low_update", val)


    def update_high_threshold(self, val):
        self.highthresh_label.setNum(val)
        event_manager.trigger("on_floodfill_high_update", val)


    def update_canvas(self, image):
        if image is None:
            return
        pixmap = np_array_to_pixmap(image)
        self.canvas_label.setPixmap(pixmap)


    def mouse_click(self, event, released):

        if event.button() == Qt.LeftButton:
            if released:
                event_manager.trigger("on_mouse_click_released")

        if event.button() == Qt.RightButton:
            event_manager.trigger("on_fill_color", event.pos().x(), event.pos().y())



    def retranslateUi(self, Lab3_Window):
        _translate = QtCore.QCoreApplication.translate
        Lab3_Window.setWindowTitle(_translate("Lab3_Window", "Lab3_Window"))
        self.groupBox_4.setTitle(_translate("Lab3_Window", "Shape Parameters"))
        #self.pushButton_3.setText(_translate("Lab3_Window", "OK"))
        self.label_2.setText(_translate("Lab3_Window", "Shape type"))
        self.boundaryFillGroupBox.setTitle(_translate("Lab3_Window", "Flood fill options"))
        self.floodfill_low_label.setText(_translate("Lab3_Window", "Floodfill Low"))
        self.lowthresh_label.setText(_translate("Lab3_Window", "0"))
        self.label_11.setText(_translate("Lab3_Window", "Floodfill High"))
        self.highthresh_label.setText(_translate("Lab3_Window", "0"))
        self.floodFillGroupBox.setTitle(_translate("Lab3_Window", "Fill method"))
        self.boundaryFillRadioButton.setText(_translate("Lab3_Window", "Boundary fill"))
        self.floodFillRadioButton.setText(_translate("Lab3_Window", "Flood fill"))
        self.groupBox_3.setTitle(_translate("Lab3_Window", "Color Type"))
        self.label_8.setText(_translate("Lab3_Window", "Fill Color"))
        self.fillColorBtn.setText(_translate("Lab3_Window", "Color"))
        self.label_9.setText(_translate("Lab3_Window", "Boundary Color"))
        self.boundaryColorBtn.setText(_translate("Lab3_Window", "Color"))
        self.menuFile.setTitle(_translate("Lab3_Window", "File"))
        self.actionExit.setText(_translate("Lab3_Window", "Open image"))
