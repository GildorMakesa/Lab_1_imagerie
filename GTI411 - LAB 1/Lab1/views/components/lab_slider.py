import numpy as np
from PyQt5.QtWidgets import QVBoxLayout, QLabel

from .color_slider import ColorSlider
from .utils import create_slider
from Lab1.models import color_conversion


def create_lab_palette(height: int, width: int, labcolor: list[int]):
    """
    Crée une palette pour un canal LAB donné.
    """
    image = np.zeros((height, width, 3), dtype=np.uint8)
    l_val, a_val, b_val = labcolor
    for widx in range(width):
        # Applique un facteur d'ajustement pour chaque composant L, A, B en fonction de la position
        factor = widx / width  # Factor for adjusting the color channels
        l_prime = l_val * factor  # Adjust L based on factor
        a_prime = a_val * factor  # Adjust A based on factor
        b_prime = b_val * factor  # Adjust B based on factor

        # Convert LAB to RGB
        rgb = color_conversion.lab_2_rgb(l_prime, a_prime, b_prime)
        
        # Clamp les valeurs RGB dans la plage [0, 255]
        rgb = [max(0, min(255, c)) for c in rgb]
        
        # Remplir chaque colonne de la palette avec la couleur RGB correspondante
        for hidx in range(height):
            image[hidx, widx] = rgb
    return image


class LabSlider(ColorSlider):

    def init_ui(self, layout: QVBoxLayout, red: int, green: int, blue: int):
        
        l, a, b = color_conversion.rgb_2_lab(red, green, blue)

        # Convertir RGB en LAB# Convertir les valeurs LAB en entiers
        l = int(round(l))  # ou int(l)
        a = int(round(a))  # ou int(a)
        b = int(round(b))  # ou int(b)
        

        # Créer les palettes de couleurs pour L, A, B
        l_palette = create_lab_palette(self.height, self.width, [l, 0, 0])
        l_layout, self.l_slider = create_slider(self.parent, "L", minval=0, maxval=100, default_value=l, slider_palette=l_palette)

        a_palette = create_lab_palette(self.height, self.width, [0, a, 0])
        a_layout, self.a_slider = create_slider(self.parent, "A", minval=-128, maxval=128, default_value=a, slider_palette=a_palette)

        b_palette = create_lab_palette(self.height, self.width, [0, 0, b])
        b_layout, self.b_slider = create_slider(self.parent, "B", minval=-128, maxval=128, default_value=b, slider_palette=b_palette)

        # Connecter les sliders aux changements de valeurs
        self.l_slider.valueChanged['int'].connect(self.value_changed)
        self.a_slider.valueChanged['int'].connect(self.value_changed)
        self.b_slider.valueChanged['int'].connect(self.value_changed)

        # Ajouter les sliders à l'interface
        layout.addLayout(l_layout)
        layout.addLayout(a_layout)
        layout.addLayout(b_layout)

    def _sliders_to_rgb(self):
        # Récupérer les valeurs des sliders L, A, B
        l = self.l_slider.value()
        a = self.a_slider.value()
        b = self.b_slider.value()

        # Convertir LAB vers RGB
        r, g, b = color_conversion.lab_2_rgb(l, a, b)
        return r, g, b
