from PyQt5 import QtWidgets, QtCore

from Lab4.events import event_manager
from Lab4.utils import np_array_to_pixmap



class InterpolationWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self.last_mouse_btn_clicked = "left"

        sizeX = 1245
        sizeY = 440

        self.interpolation_tab = QtWidgets.QWidget()
        self.interpolation_tab.setObjectName("tab_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.interpolation_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_10 = QtWidgets.QFrame(self.interpolation_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_9 = QtWidgets.QFrame(self.frame_10)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.interpolation_method = QtWidgets.QComboBox(self.frame_9)
        self.interpolation_method.setObjectName("comboBox_4")
        self.interpolation_method.addItem("")
        self.interpolation_method.addItem("")
        self.interpolation_method.addItem("")
        self.interpolation_method.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.interpolation_method)
        self.interpolation_method_label = QtWidgets.QLabel(self.frame_9)
        self.interpolation_method_label.setObjectName("label_16")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.interpolation_method_label)
        self.horizontalLayout_5.addLayout(self.formLayout_3)
        self.reset_button = QtWidgets.QPushButton(self.frame_9)
        self.reset_button.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.reset_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.frame_4 = QtWidgets.QFrame(self.frame_10)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
    
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.interpolation_tab)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.canvas_label = QtWidgets.QLabel(self.frame_11)
        self.canvas_label.setText("")
        self.canvas_label.setObjectName("label")
        self.canvas_label.setMinimumSize(QtCore.QSize(sizeX, sizeY))
        self.canvas_label.setMaximumSize(QtCore.QSize(sizeX, sizeY))


        self.canvas_label.mousePressEvent = self.mouse_press
        self.canvas_label.mouseMoveEvent = self.mouse_move
        self.canvas_label.mouseReleaseEvent = lambda event: self.mouse_release(event, released=True)

        self.interpolation_method.currentTextChanged.connect(lambda x: event_manager.trigger("on_curve_type_changed", x))
        self.retranslateUi()
        self.verticalLayout_2.addWidget(self.frame_11)
        self.setLayout(self.verticalLayout_2)

        self.reset_button.clicked.connect(lambda x: event_manager.trigger("on_reset_canvas"))

        event_manager.register("on_draw_canvas", self.update_canvas)


    def mouse_press(self, event):
        if event.button() == QtCore.Qt.LeftButton:
             self.last_mouse_btn_clicked = "left"
        elif event.button() == QtCore.Qt.RightButton:
            self.last_mouse_btn_clicked = "right"


    def mouse_move(self, event):
        if self.last_mouse_btn_clicked == "right":
            event_manager.trigger("on_mouse_click_move", event.pos().x(), event.pos().y())


    def mouse_release(self, event, released):
        if event.button() == QtCore.Qt.LeftButton:
            self.last_mouse_btn_clicked = "left"
            event_manager.trigger("on_canvas_click", event.pos().x(), event.pos().y())

        if event.button() == QtCore.Qt.RightButton:
            self.last_mouse_btn_clicked = "right"
            event_manager.trigger("on_mouse_click_released")



    def update_canvas(self, image):
        if image is None:
            return
        pixmap = np_array_to_pixmap(image)
        self.canvas_label.setPixmap(pixmap)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.interpolation_method.setItemText(0, _translate("Lab4_Window", "Linear"))
        self.interpolation_method.setItemText(1, _translate("Lab4_Window", "Bezier"))
        self.interpolation_method.setItemText(2, _translate("Lab4_Window", "Hermite"))
        self.interpolation_method.setItemText(3, _translate("Lab4_Window", "BSpline"))
        self.interpolation_method_label.setText(_translate("Lab4_Window", "Curve type"))
        self.reset_button.setText(_translate("Lab4_Window", "Reset"))