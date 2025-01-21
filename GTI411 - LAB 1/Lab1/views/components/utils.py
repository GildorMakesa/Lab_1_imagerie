import numpy as np
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap, QPainter, QImage



def np_array_to_pixmap(array):
    height, width, channel = array.shape
    # Convertir le tableau en QImage
    if channel == 3:  # Si l'image est en RGB
        qimage = QImage(array.data, width, height, 3 * width, QImage.Format_RGB888)
    elif channel == 4:  # Si l'image est en RGBA
        qimage = QImage(array.data, width, height, 4 * width, QImage.Format_RGBA888)
    else:
        raise ValueError("Le tableau numpy doit avoir 3 canaux (RGB) ou 4 canaux (RGBA)")

    # Convertir QImage en QPixmap
    qpixmap = QPixmap.fromImage(qimage)
    return qpixmap


class SliderWithImage(QtWidgets.QSlider):
    def __init__(self, image, parent):
        super().__init__(QtCore.Qt.Horizontal, parent)
        self.image = image


    def paintEvent(self, event):
        if self.image is None:
            super().paintEvent(event)
            return
        # Création du QPainter pour dessiner l'image de fond
        painter = QPainter(self)

        height, width, channel = self.image.shape
        # Convertir le tableau en QImage
        if channel == 3:  # Si l'image est en RGB
            qimage = QImage(self.image.data, width, height, 3 * width, QImage.Format_RGB888)
        elif channel == 4:  # Si l'image est en RGBA
            qimage = QImage(self.image.data, width, height, 4 * width, QImage.Format_RGBA888)
        else:
            raise ValueError("Le tableau numpy doit avoir 3 canaux (RGB) ou 4 canaux (RGBA)")

        # Convertir QImage en QPixmap
        qpixmap = QPixmap.fromImage(qimage)

        painter.drawPixmap(self.rect(), qpixmap)
        
        # Appel de la méthode paintEvent de la classe de base pour dessiner le reste du slider
        super().paintEvent(event)


def create_slider(parent: QWidget, name:str,
                  minval:int=0,
                  maxval: int=255,
                  default_value: int = 0,
                  slider_palette: np.ndarray = None
                  ):
    """Helper function to generate a 

    Parameters
    ----------
    parent : QWidget
        _description_
    name : str
        _description_
    minval : int, optional
        _description_, by default 0
    maxval : int, optional
        _description_, by default 255
    rgbcolor : list[int], optional
        _description_, by default [0, 0, 0]

    Returns
    -------
    _type_
        _description_
    """
    horizontal_layout = QtWidgets.QHBoxLayout(parent)

    slider = SliderWithImage(slider_palette, parent)
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
    
