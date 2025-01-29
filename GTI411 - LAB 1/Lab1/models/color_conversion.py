"""A faire: implémenter la conversion HSV, CMYK et Lab vers et depuis RGB"""


def rgb_2_rgb(r, g, b):
    """Cette fonction ne fait rien, elle sert uniquement pour illustrer"""
    return r, g, b



def rgb_2_hsv(r, g, b):
    # Normalisation des valeurs RGB dans la plage [0, 1]
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0 
    
    M = max(r, g ,b)
    m = min(r, g, b)
    C = M - m

    h = 0 #if C = 0

 # Calcul de la teinte (hue)
    if M == r:
        h = ((g-b)/C) % 6
    elif M == g:
        h = ((b-r)/C) + 2
    elif M == b:
        h = ((r-g)/C) + 4
        
    h *= 60

    # Calcul de la valeur (value)
    v = M

    # Calcul de la saturation (saturation)
    s = 0 if C == 0 else C / v

    return int(h), int(s * 100), int(v * 100)


def hsv_2_rgb(h, s, v):
    # Normalisation de s et v de [0, 100] à [0, 1]
    s = s / 100.0
    v = v / 100.0
    
    # Normalisation de h de [0, 360] à [0, 1]
    h = h / 360.0
    
    c = v * s  # Chroma
    x = c * (1 - abs(((h * 6) % 2) - 1))  # Composant intermédiaire
    m = v - c  # Ajustement à la luminosité
    
    # Définir les valeurs RGB en fonction de l'angle h
    if 0 <= h < 1 / 6:
        r, g, b = c, x, 0
    elif 1 / 6 <= h < 2 / 6:
        r, g, b = x, c, 0
    elif 2 / 6 <= h < 3 / 6:
        r, g, b = 0, c, x
    elif 3 / 6 <= h < 4 / 6:
        r, g, b = 0, x, c
    elif 4 / 6 <= h < 5 / 6:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    
    # Appliquer le décalage m et passer les valeurs à l'échelle [0, 255]
    r = int((r + m) * 255)
    g = int((g + m) * 255)
    b = int((b + m) * 255)
    
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
