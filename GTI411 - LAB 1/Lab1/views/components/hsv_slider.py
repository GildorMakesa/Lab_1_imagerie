import numpy as np
from PyQt5.QtWidgets import QVBoxLayout, QLabel

from .color_slider import ColorSlider
from .utils import create_slider




class HSVSlider(ColorSlider):

    def init_ui(self, layout: QVBoxLayout, red: int, green: int, blue: int):
        # TODO
        label = QLabel()
        label.setText("TODO HSV")

        layout.addWidget(label)


    def _sliders_to_rgb(self):
        # TODO
        pass



