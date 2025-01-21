from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5 import QtWidgets, QtGui


from Lab1.events import event_manager


class ImageDecompositionWidget(QWidget):

    def __init__(self, parent=None, values: list[int] = None, **kwargs) -> None:
        super().__init__(parent, **kwargs)

        self.gridLayout = QtWidgets.QVBoxLayout(parent)

        dropdown = QtWidgets.QComboBox()
        dropdown.addItems(["rgb", "hsv", "cmyk", "lab"])
        decomp_btn = QtWidgets.QPushButton(text="Decompose image")
        decomp_btn.clicked.connect(lambda: event_manager.trigger("on_decompose_image"))
        self.frame_5 = QtWidgets.QFrame(parent)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setText("")
        self.gridLayout.setObjectName("gridLayout")

        # pixmap = QPixmap("Lab1/Cube.JPG")
        # self.label_10.setPixmap(pixmap)
        self.gridLayout.addWidget(self.label_10)
        self.gridLayout.addWidget(dropdown)
        self.gridLayout.addWidget(decomp_btn)

        self.setLayout(self.gridLayout)

        event_manager.register("on_imagefile_loaded", self.update_image)

        dropdown.currentTextChanged.connect(lambda x: event_manager.trigger("on_update_decomp_method", x))


    def update_image(self, filename:str):
        pixmap = QtGui.QPixmap(filename)
        self.label_10.setPixmap(pixmap)