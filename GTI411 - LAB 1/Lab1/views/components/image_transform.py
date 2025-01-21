from PyQt5.QtCore import Qt
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets, QtGui


from Lab1.events import event_manager


def create_slider(parent: QWidget, name:str,
                  minval:int=0,
                  maxval: int=255,
                  default_value: int = 0):
    horizontal_layout = QtWidgets.QHBoxLayout(parent)

    slider = QtWidgets.QSlider(Qt.Horizontal, parent)
    slider.setMinimum(minval)
    slider.setMaximum(maxval)

    slider.setValue(default_value)

    label = QtWidgets.QLabel(parent)
    value_label = QtWidgets.QLabel(parent)
    value_label.setText(str(default_value))
    label.setText(name)

    slider.valueChanged['int'].connect(value_label.setNum)

    slider.setMinimumSize(QtCore.QSize(267, 22))
    value_label.setMinimumSize(QtCore.QSize(20, 0))

    horizontal_layout.addWidget(label)
    horizontal_layout.addWidget(slider)
    horizontal_layout.addWidget(value_label)
    return horizontal_layout, slider


class ImageTransformWidget(QWidget):

    def __init__(self, parent=None, values: list[int] = None, **kwargs) -> None:
            super().__init__(parent, **kwargs)

            self.gridLayout = QtWidgets.QVBoxLayout(parent)
            contrast_layout, self.contrast_slider = create_slider(parent, "Constraste", maxval=5, default_value=1)
            lum_layout, self.lum_slider = create_slider(parent, "Luminosite", minval=-100, maxval=100, default_value=0)

            self.frame_5 = QtWidgets.QFrame(parent)
            self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_5.setObjectName("frame_5")
            self.label_10 = QtWidgets.QLabel(self.frame_5)
            self.label_10.setFrameShape(QtWidgets.QFrame.Box)
            self.label_10.setText("")

            self.gridLayout.setObjectName("gridLayout")

            self.gridLayout.addWidget(self.label_10, stretch=9)
            self.gridLayout.addLayout(lum_layout, stretch=1)
            self.gridLayout.addLayout(contrast_layout, stretch=1)
            self.setLayout(self.gridLayout)

            event_manager.register("on_image_loaded", self.update_image)
            event_manager.register("on_image_updated", self.update_image)

            self.contrast_slider.valueChanged["int"].connect(self.apply_transform)
            self.lum_slider.valueChanged["int"].connect(self.apply_transform)


    def apply_transform(self):
        contrast = self.contrast_slider.value()
        lum = self.lum_slider.value()
        event_manager.trigger("on_apply_image_transform", contrast, lum)


    def update_image(self, file):
        if isinstance(file, str):
            pixmap = QtGui.QPixmap(file)
        elif isinstance(file, np.ndarray):
            height, width, channel = file.shape
            # Convertir le tableau en QImage
            if channel == 3:  # Si l'image est en RGB
                qimage = QtGui.QImage(file.data, width, height, 3 * width, QtGui.QImage.Format_RGB888)
            elif channel == 4:  # Si l'image est en RGBA
                qimage = QtGui.QImage(file.data, width, height, 4 * width, QtGui.QImage.Format_RGBA888)
            else:
                raise ValueError("Le tableau numpy doit avoir 3 canaux (RGB) ou 4 canaux (RGBA)")

            # Convertir QImage en QPixmap
            pixmap = QtGui.QPixmap.fromImage(qimage)

        self.label_10.setPixmap(pixmap)