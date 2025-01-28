"""A faire: implémenter la conversion HSV, CMYK et Lab vers et depuis RGB"""
import math

def rgb_2_rgb(r, g, b):
    """Cette fonction ne fait rien, elle sert uniquement pour illustrer"""
    return r, g, b



def rgb_2_hsv(r, g, b):
    """
    Convertir une couleur RGB (0-255) en HSV (0-360 pour H, 0-1 pour S et V).
    """
    # Normalisation des valeurs en 0-1
    r_prime = r / 255.0
    g_prime = g / 255.0
    b_prime = b / 255.0

    # Trouver les valeurs max et min
    c_max = max(r_prime, g_prime, b_prime)
    c_min = min(r_prime, g_prime, b_prime)
    delta = c_max - c_min

    # Calcul de la teinte (H)
    if delta == 0:
        h = 0
    elif c_max == r_prime:
        h = 60 * (((g_prime - b_prime) / delta) % 6)
    elif c_max == g_prime:
        h = 60 * (((b_prime - r_prime) / delta) + 2)
    elif c_max == b_prime:
        h = 60 * (((r_prime - g_prime) / delta) + 4)

    # Calcul de la saturation (S)
    s = 0 if c_max == 0 else delta / c_max

    # Calcul de la valeur (V)
    v = c_max

    return round(h, 2), round(s, 2), round(v, 2)


def hsv_2_rgb(h, s, v):
    """
    Convertir une couleur HSV (0-360 pour H, 0-1 pour S et V) en RGB (0-255).
    """
    c = v * s  # Chroma
    x = c * (1 - abs((h / 60) % 2 - 1))  # Valeur intermédiaire
    m = v - c  # Ajustement

    # Identifier la région de la teinte
    if 0 <= h < 60:
        r_prime, g_prime, b_prime = c, x, 0
    elif 60 <= h < 120:
        r_prime, g_prime, b_prime = x, c, 0
    elif 120 <= h < 180:
        r_prime, g_prime, b_prime = 0, c, x
    elif 180 <= h < 240:
        r_prime, g_prime, b_prime = 0, x, c
    elif 240 <= h < 300:
        r_prime, g_prime, b_prime = x, 0, c
    elif 300 <= h < 360:
        r_prime, g_prime, b_prime = c, 0, x
    else:
        r_prime, g_prime, b_prime = 0, 0, 0

    # Conversion en 0-255
    r = round((r_prime + m) * 255)
    g = round((g_prime + m) * 255)
    b = round((b_prime + m) * 255)

    return r, g, b


def rgb_2_cmyk(r: int, g: int, b: int):
    """
    Convertir une couleur RGB (0-255) en CMYK (0-100).
    """
    if r == 0 and g == 0 and b == 0:
        return 0, 0, 0, 100  # Cas spécial : noir pur

    #Normalise en 1-0 
    r_prime = r / 255
    g_prime = g / 255
    b_prime = b / 255

    k = 1 - max(r_prime, g_prime, b_prime)


    c = (1 - r_prime - k) / (1 - k) if k < 1 else 0
    m = (1 - g_prime - k) / (1 - k) if k < 1 else 0
    y = (1 - b_prime - k) / (1 - k) if k < 1 else 0

    return int(c * 100), int(m * 100), int(y * 100), int(k * 100)


def cmyk_2_rgb(c: int, m: int, y: int, k: int):
    """
    Convertir une couleur CMYK (0-100) en RGB (0-255).
    
    """
    c_prime, m_prime, y_prime, k_prime = c / 100, m / 100, y / 100, k / 100
    r = 255 * (1 - c_prime) * (1 - k_prime)
    g = 255 * (1 - m_prime) * (1 - k_prime)
    b = 255 * (1 - y_prime) * (1 - k_prime)

    # Assurer les valeurs dans la plage [0, 255]
    r, g, b = [max(0, min(255, int(v))) for v in (r, g, b)]

    return r, g, b


""" 
A faire: implémenter la conversion HSV, CMYK et Lab vers et depuis RGB


def rgb_2_rgb(r, g, b):
    Cette fonction ne fait rien, elle sert uniquement pour illustrer
    return r, g, b



def rgb_2_hsv(r, g, b):
    return ...


def hsv_2_rgb(h, s, v):
    
    #Normalise en 1-0 
    r_prime = h / 255
    g_prime = s / 255
    b_prime = v / 255



    return ...
"""