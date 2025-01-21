

import numpy as np
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout


from Lab1.events import event_manager



class ColorSlider(QWidget):
    """Base class for the slider"""

    width: int = 267
    height: int = 22
    def __init__(self, parent=None, values: list[int] = None, **kwargs) -> None:
        super().__init__(parent, **kwargs)
        layout = QVBoxLayout(parent)
        self.parent = parent

        if values:
            r, g, b = values
        else:
            r, g, b = 0, 0, 0

        self.init_ui(layout, r, g, b)

        self.setLayout(layout)


    def init_ui(self, layout:QVBoxLayout, red:int, green:int, blue:int):
        """Setup ui by creating sliders and adding them to the main layout

        Args:
            layout (QVBoxLayout): Main layout containing sliders
            red (int): Red channel value [0: 255]
            green (int): Green channel value [0: 255]
            blue (int): Blue channel value [0: 255]
        """
        pass



    def _sliders_to_rgb(self) -> tuple[int, int, int]:
        """Get current sliders values, convert them if needed
        then returns rgb code

        Returns:
            tuple[int, int, int]: RGB values after conversion
        """
        pass

    
    def value_changed(self):
        """Triggers event to update UI"""
        r, g, b = self._sliders_to_rgb()
        event_manager.trigger("on_color_update", [r, g, b], "rgb")