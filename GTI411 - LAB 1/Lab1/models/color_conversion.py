"""A faire: implémenter la conversion HSV, CMYK et Lab vers et depuis RGB"""


def rgb_2_rgb(r, g, b):
    """Cette fonction ne fait rien, elle sert uniquement pour illustrer"""
    return r, g, b



def rgb_2_hsv(r, g, b):
    return ...


def hsv_2_rgb(h, s, v):
    
    #Normalise en 1-0 
    r_prime = h / 255
    g_prime = s / 255
    b_prime = v / 255



    return ...


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