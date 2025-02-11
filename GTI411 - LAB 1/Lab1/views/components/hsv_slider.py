import numpy as np
from PyQt5.QtWidgets import QVBoxLayout, QLabel

from .color_slider import ColorSlider
from .utils import create_slider
from Lab1.models import color_conversion


def create_hsv_palette(height: int, width: int, hsvcolor: list[float]):
    """
    Crée une palette pour un canal HSV donné.
    """
    image = np.zeros((height, width, 3), dtype=np.uint8)
    h, w, _ = image.shape
    for widx in range(w):
        h_val, s_val, v_val = hsvcolor
        factor = widx / w  # Position factor for color adjustment
        h_prime = h_val * factor  # Adjust Hue based on factor
        s_prime = s_val * factor  # Adjust Saturation based on factor
        v_prime = v_val * factor  # Adjust Value based on factor
        
        # Convert adjusted HSV to RGB
        rgb = color_conversion.hsv_2_rgb(h_prime, s_prime, v_prime)
        
        # Assign RGB values to each pixel in the image column
        for hidx in range(h):
            image[hidx, widx] = rgb
    return image



class HSVSlider(ColorSlider):
    ############################################################################################################
    ############################################################################################################
    def init_ui(self, layout: QVBoxLayout, red: int, green: int, blue: int):
        # Convertir RGB vers CMYK
        h, s, v = color_conversion.rgb_2_hsv(red, green, blue)

        h_palette = create_hsv_palette(self.height, self.width, [360, 100, 100])
        h_layout, self.h_slider = create_slider(self.parent, "H", minval=0, maxval=360, default_value=h, slider_palette=h_palette)
        
        s_palette = create_hsv_palette(self.height, self.width, [0, 0, 100])
        s_layout, self.s_slider = create_slider(self.parent, "S", minval=0, maxval=100, default_value=s, slider_palette=s_palette)

        v_palette = create_hsv_palette(self.height, self.width, [0, 0, 100])
        v_layout, self.v_slider = create_slider(self.parent, "V", minval=0, maxval=100,default_value=v, slider_palette=v_palette)

        # Connecter les sliders au changement de valeur
        self.h_slider.valueChanged['int'].connect(self.value_changed)
        self.s_slider.valueChanged['int'].connect(self.value_changed)
        self.v_slider.valueChanged['int'].connect(self.value_changed)

        # Ajouter les sliders à l'interface
        layout.addLayout(h_layout)
        layout.addLayout(s_layout)
        layout.addLayout(v_layout)

    def _sliders_to_rgb(self):
        # Récupérer les valeurs des sliders CMYK
        h = self.h_slider.value()
        s = self.s_slider.value()
        v = self.v_slider.value()
        # Récupérer les valeurs des sliders CMYK
        h = self.h_slider.value()
        s = self.s_slider.value()
        v = self.v_slider.value()

        # Convertir CMYK vers RGB
        r, g, b = color_conversion.hsv_2_rgb(h, s, v)
        return r, g, b
        # Convertir CMYK vers RGB
        r, g, b = color_conversion.hsv_2_rgb(h, s, v)
        return r, g, b