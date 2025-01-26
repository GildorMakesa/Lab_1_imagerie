import numpy as np
from PyQt5.QtWidgets import QVBoxLayout


from Lab1.models import color_conversion
from .color_slider import ColorSlider
from .utils import create_slider


def create_rgb_palette(height:int, width: int, rgbcolor:list[int]):
    image = np.zeros((height, width, 3), dtype=np.uint8)
    h, w, _ = image.shape

    for widx in range(w):
        color = 255*(widx/ w) * np.array(rgbcolor)
        for hidx in range(h):
            image[hidx, widx] = color
            
    return image



class RGBSlider(ColorSlider):


    def init_ui(self, layout: QVBoxLayout, red: int, green: int, blue: int):

        # Convert to RGB
        r, g, b = color_conversion.rgb_2_rgb(red, green, blue)

        # Red channel
        red_palette = create_rgb_palette(self.height, self.width, [1, 0, 0])
        red_layout, self.red_slider = create_slider(self.parent, "R", default_value=r, slider_palette=red_palette)

        # Green channel
        green_palette = create_rgb_palette(self.height, self.width, [0, 1, 0])
        green_layout, self.green_slider = create_slider(self.parent, "G", default_value=g, slider_palette=green_palette)

        # Blue channel
        blue_palette = create_rgb_palette(self.height, self.width, [0, 0, 1])
        blue_layout, self.blue_slider = create_slider(self.parent, "B", default_value=b, slider_palette=blue_palette)

        # Ecouter les mouvements du slider et appelle la fonction 'value_changed'
        self.red_slider.valueChanged['int'].connect(self.value_changed)
        self.green_slider.valueChanged['int'].connect(self.value_changed)
        self.blue_slider.valueChanged['int'].connect(self.value_changed)

        # Ajoute les sliders à l'interface
        layout.addLayout(red_layout)
        layout.addLayout(green_layout)
        layout.addLayout(blue_layout)


    def _sliders_to_rgb(self):
        r = self.red_slider.value()
        g = self.green_slider.value()
        b = self.blue_slider.value()

        red, green, blue = color_conversion.rgb_2_rgb(r, g, b)
        return red, green, blue
