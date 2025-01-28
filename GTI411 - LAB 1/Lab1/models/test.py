from color_conversion import hsv_2_rgb
from color_conversion import rgb_2_hsv

# Test de la fonction rgb_2_hsv
rgb_values = (255, 0, 0)  # Couleur rouge en RGB
hsv_values = rgb_2_hsv(*rgb_values)
print(f"\n\nRGB {rgb_values} converti en HSV : {hsv_values}")

# Test de la fonction hsv_2_rgb
hsv_values = (0, 100, 100)  # Valeur HSV pour le rouge pur (H=0, S=1, V=1)
rgb_values_converted = hsv_2_rgb(*hsv_values)
print(f"\n\nHSV {hsv_values} converti en RGB : {rgb_values_converted}")

# Test inverse, pour vérifier si les deux conversions sont cohérentes
rgb_values = (0, 255, 0)  # Couleur verte en RGB
hsv_values = rgb_2_hsv(*rgb_values)
rgb_values_converted = hsv_2_rgb(*hsv_values)
print(f"\n\nRGB {rgb_values} converti en HSV puis reconverti en RGB : {rgb_values_converted}")

# Test avec une autre couleur (bleu)
rgb_values = (0, 0, 255)  # Bleu pur en RGB
hsv_values = rgb_2_hsv(*rgb_values)
rgb_values_converted = hsv_2_rgb(*hsv_values)
print(f"\n\nRGB {rgb_values} converti en HSV puis reconverti en RGB : {rgb_values_converted}")
