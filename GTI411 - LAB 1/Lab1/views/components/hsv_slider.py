import numpy as np
from PyQt5.QtWidgets import QVBoxLayout, QLabel

from .color_slider import ColorSlider
from .utils import create_slider
from Lab1.models import color_conversion


def create_hsv_palette(height: int, width: int, hsv_color: list[float]):
    """
    Crée une image représentant une palette HSV, donnée par un canal constant.
    """
    image = np.zeros((height, width, 3), dtype=np.uint8)
    h, w, _ = image.shape

    for widx in range(w):
        color = color_conversion.hsv_2_rgb(hsv_color[0], hsv_color[1], widx / w)
        for hidx in range(h):
            image[hidx, widx] = color
    return image


class HSVSlider(ColorSlider):

    def init_ui(self, layout: QVBoxLayout, red: int, green: int, blue: int):
        """
        Initialise l'interface avec les sliders pour Hue, Saturation et Value.
        """
        # Convert RGB en HSV
        h, s, v = color_conversion.rgb_2_hsv(red, green, blue)

        # Hue slider
        hue_palette = create_hsv_palette(self.height, self.width, [0, 1, 1])
        hue_layout, self.hue_slider = create_slider(self.parent, "H", minval=0, maxval=360, default_value=120, slider_palette=hue_palette)

        # Saturation slider
        saturation_palette = create_hsv_palette(self.height, self.width, [h, 0, 1])
        saturation_layout, self.saturation_slider = create_slider(self.parent, "S", minval=0, maxval=100, default_value=s * 100, slider_palette=saturation_palette)

        # Value slider
        value_palette = create_hsv_palette(self.height, self.width, [h, s, 0])
        value_layout, self.value_slider = create_slider(self.parent, "V", minval=0, maxval=100, default_value=v * 100, slider_palette=value_palette)

        # Écouter les mouvements des sliders et appeler la fonction 'value_changed'
        self.hue_slider.valueChanged['int'].connect(self.value_changed)
        self.saturation_slider.valueChanged['int'].connect(self.value_changed)
        self.value_slider.valueChanged['int'].connect(self.value_changed)

        # Ajouter les sliders à l'interface
        layout.addLayout(hue_layout)
        layout.addLayout(saturation_layout)
        layout.addLayout(value_layout)

    def _sliders_to_rgb(self):
        """
        Convertit les valeurs des sliders HSV en une couleur RGB.
        """
        h = self.hue_slider.value()
        s = self.saturation_slider.value() / 100  # Conversion de 0-100 à 0-1
        v = self.value_slider.value() / 100  # Conversion de 0-100 à 0-1

        # Conversion HSV -> RGB
        r, g, b = color_conversion.hsv_2_rgb(h, s, v)
        return r, g, b
