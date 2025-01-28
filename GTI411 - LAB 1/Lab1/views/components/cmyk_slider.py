import numpy as np
from PyQt5.QtWidgets import QVBoxLayout

from Lab1.models import color_conversion
from .color_slider import ColorSlider
from .utils import create_slider


def create_cmyk_palette(height: int, width: int, cmykcolor: list[float]):
    """
    Crée une palette pour un canal CMYK donné.
    """
    image = np.zeros((height, width, 3), dtype=np.uint8)
    h, w, _ = image.shape
    for widx in range(w):
        c, m, y, k = cmykcolor
        factor = widx / w  # Facteur de position sur l'axe des couleurs
        rgb = color_conversion.cmyk_2_rgb(c* factor * 100, m * factor * 100, y * factor * 100, k * 100)
        for hidx in range(h):
            image[hidx, widx] = rgb
    return image



class CMYKSlider(ColorSlider):
    def init_ui(self, layout: QVBoxLayout, red: int, green: int, blue: int):
        # Convertir RGB vers CMYK
        c, m, y, k = color_conversion.rgb_2_cmyk(red, green, blue)

        # Cyan channel
        cyan_palette = create_cmyk_palette(self.height, self.width, [1, 0, 0, 0])
        cyan_layout, self.cyan_slider = create_slider(self.parent, "C", minval=0, maxval=100, default_value=c, slider_palette=cyan_palette)
        
        
        # Magenta channel
        magenta_palette = create_cmyk_palette(self.height, self.width, [0, 1, 0, 0])
        magenta_layout, self.magenta_slider = create_slider(self.parent, "M", minval=0, maxval=100, default_value=m, slider_palette=magenta_palette)

        # Yellow channel
        yellow_palette = create_cmyk_palette(self.height, self.width, [0, 0, 1, 0])
        yellow_layout, self.yellow_slider = create_slider(self.parent, "Y", minval=0, maxval=100,default_value=y, slider_palette=yellow_palette)

        # Key (black) channel
        key_palette = create_cmyk_palette(self.height, self.width, [0, 0, 0, 1])
        key_layout, self.key_slider = create_slider(self.parent, "K", minval=0, maxval=100, default_value=k, slider_palette=key_palette)

        # Connecter les sliders au changement de valeur
        self.cyan_slider.valueChanged['int'].connect(self.value_changed)
        self.magenta_slider.valueChanged['int'].connect(self.value_changed)
        self.yellow_slider.valueChanged['int'].connect(self.value_changed)
        self.key_slider.valueChanged['int'].connect(self.value_changed)

        # Ajouter les sliders à l'interface
        layout.addLayout(cyan_layout)
        layout.addLayout(magenta_layout)
        layout.addLayout(yellow_layout)
        layout.addLayout(key_layout)

    def _sliders_to_rgb(self):
        # Récupérer les valeurs des sliders CMYK
        c = self.cyan_slider.value()
        m = self.magenta_slider.value()
        y = self.yellow_slider.value()
        k = self.key_slider.value()

        # Convertir CMYK vers RGB
        r, g, b = color_conversion.cmyk_2_rgb(c, m, y, k)
        return r, g, b
