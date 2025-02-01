from color_conversion import hsv_2_rgb
from color_conversion import rgb_2_hsv
from color_conversion import hsv_2_rgb, rgb_2_hsv, rgb_2_lab, lab_2_rgb


# Test de la fonction rgb_2_hsv
rgb_values = (255, 0, 0)  # Couleur rouge en RGB
hsv_values = rgb_2_hsv(*rgb_values)
print(f"\nRGB {rgb_values} converti en HSV : {hsv_values}")

# Test de la fonction hsv_2_rgb
hsv_values = (0, 100, 100)  # Valeur HSV pour le rouge pur (H=0, S=1, V=1)
rgb_values_converted = hsv_2_rgb(*hsv_values)
print(f"\nHSV {hsv_values} converti en RGB : {rgb_values_converted}")

# Test inverse, pour vérifier si les deux conversions sont cohérentes
rgb_values = (0, 255, 0)  # Couleur verte en RGB
hsv_values = rgb_2_hsv(*rgb_values)
rgb_values_converted = hsv_2_rgb(*hsv_values)
print(f"\nRGB {rgb_values} converti en HSV puis reconverti en RGB : {rgb_values_converted}")

# Test avec une autre couleur (bleu)
rgb_values = (0, 0, 255)  # Bleu pur en RGB
hsv_values = rgb_2_hsv(*rgb_values)
rgb_values_converted = hsv_2_rgb(*hsv_values)
print(f"\nRGB {rgb_values} converti en HSV puis reconverti en RGB : {rgb_values_converted}")







print(f"\n\n\n --- Tests pour RGB <-> LAB ---")


# Test avec une couleur RGB (rouge pur)
print(f"Test couleur rouge RGB")
rgb_values = (255, 0, 0)
lab_values = rgb_2_lab(*rgb_values)
print(f"\n\nRGB {rgb_values} converti en LAB : {lab_values}\n\n\n")

# Test inverse : convertir LAB vers RGB
lab_values = (97.14, -21.56, 94.482)  # Valeurs attendues pour le rouge
rgb_values_converted = lab_2_rgb(*lab_values)
print(f"\n\nLAB {lab_values} converti en RGB : {rgb_values_converted}")

# Test avec une couleur RGB (verte)
rgb_values = (0, 255, 0)
lab_values = rgb_2_lab(*rgb_values)
print(f"\n\nRGB {rgb_values} converti en LAB : {lab_values}")

lab_values = (87.7347, -86.1825, 83.1793)  # Valeurs attendues pour le vert
rgb_values_converted = lab_2_rgb(*lab_values)
print(f"\n\nLAB {lab_values} converti en RGB : {rgb_values_converted}")

# Test avec une couleur RGB (bleu)
rgb_values = (0, 0, 255)
lab_values = rgb_2_lab(*rgb_values)
print(f"\n\nRGB {rgb_values} converti en LAB : {lab_values}")

lab_values = (32.3026, 79.1965, -107.8637)  # Valeurs attendues pour le bleu
rgb_values_converted = lab_2_rgb(*lab_values)
print(f"\n\nLAB {lab_values} converti en RGB : {rgb_values_converted}")

