from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5 import QtWidgets


from Lab1.events import event_manager
from Lab1.draw_utils import draw_shape_as_qpixmap


class ColorConversionWidget(QWidget):

    def __init__(self, parent=None, **kwargs) -> None:
        super().__init__(parent, **kwargs)
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(parent)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(parent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(300, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setObjectName("pushButton_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_9)
        self.horizontalLayout_10.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.frame)
        self.label_2 = QtWidgets.QLabel(parent)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Lab1_Window", "Selected Object Color"))
        self.pushButton_9.clicked.connect(lambda: event_manager.trigger("on_open_interpolation_window"))
        self.pushButton_9.setText(_translate("Lab1_Window", "Color"))
        self.pushButton_9.setEnabled(False)

        self.setLayout(self.verticalLayout_3)

        event_manager.register("on_add_shape_ready", self.update_shape)
        event_manager.register("on_color_update_ready", self.update_shape)



    def update_shape(self, r, g, b, shape:str = "circle"):
        img_height, img_width = self.label_2.height(), self.label_2.width()
        pixmap = draw_shape_as_qpixmap(r, g, b, img_height, img_width, shape)
        self.label_2.setPixmap(pixmap)
        self.pushButton_9.setEnabled(True)
        self.whichForm = False