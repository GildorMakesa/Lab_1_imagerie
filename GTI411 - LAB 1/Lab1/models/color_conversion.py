"""A faire: implémenter la conversion HSV, CMYK et Lab vers et depuis RGB"""


def rgb_2_rgb(r, g, b):
    """Cette fonction ne fait rien, elle sert uniquement pour illustrer"""
    return r, g, b



def rgb_2_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0  # Normalisation des valeurs RGB dans la plage [0, 1]
    
    c_max = max(r, g, b)
    c_min = min(r, g, b)
    delta = c_max - c_min
    
    # Calcul de la teinte (hue)
    if delta == 0:
        h = 0
    elif c_max == r:
        h = (60 * ((g - b) / delta) + 360) % 360
    elif c_max == g:
        h = (60 * ((b - r) / delta) + 120) % 360
    else:
        h = (60 * ((r - g) / delta) + 240) % 360
    
    # Calcul de la saturation (saturation)
    if c_max == 0:
        s = 0
    else:
        s = delta / c_max
    
    # Calcul de la valeur (value)
    v = c_max
    
    return int(h), int(s * 100), int(v * 100)  # Renvoi des valeurs de HSV (hue en degrés, saturation et valeur en pourcentage)




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

# Exemple d'utilisation
h, s, v = 360, 100, 100  # Rouge
r, g, b = hsv_2_rgb(h, s, v)




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

# Conversion de RGB en LAB
def rgb_2_lab(r, g, b):
    x, y, z = rgb_2_xyz(r, g, b)
    return xyz_2_lab(x, y, z)



# Fonction pour normaliser RGB [0, 255] en [0, 1]
def normalize_rgb(r, g, b):
    return r / 255.0, g / 255.0, b / 255.0

# Fonction pour dénormaliser les valeurs RGB [0, 1] en [0, 255]
def denormalize_rgb(r, g, b):
    return int(r * 255), int(g * 255), int(b * 255)

# Conversion de RGB en XYZ
def rgb_2_xyz(r, g, b):
    r, g, b = normalize_rgb(r, g, b)
    
    print(f"\nR: {r} // G: {g} // B {b} normalisation")

    # Application de la matrice de transformation RGB -> XYZ (espace de couleur sRGB)
    r = r / 12.92 if r <= 0.04045 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.04045 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.04045 else ((b + 0.055) / 1.055) ** 2.4
    
    # Matrice de transformation RGB -> XYZ
    x = 0.4124 * r + 0.3576 * g + 0.1805 * b
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = 0.0193 * r + 0.1192 * g + 0.9505 * b
    print(f"\nX: {x} // Y: {y} // Z {z} XYZ")

    return x, y, z

# Conversion de XYZ en LAB
def xyz_2_lab(x, y, z):
    # Valeurs des points de référence de XYZ (D65)
    x_ref, y_ref, z_ref = 0.95047, 1.00000, 1.08883

    # Normalisation des valeurs X, Y, Z par rapport aux références
    x /= x_ref
    y /= y_ref
    z /= z_ref

    # Fonction de transformation f(t)
    def f(t):
        delta = 6 / 29  # Définition de la constante delta

        # Si t > delta^3, appliquer t^(1/3)
        if t > delta**3:
            return t**(1/3)
        # Sinon appliquer la formule alternative
        else:
            return (t / (29**2)) + 4 / 29
    
    # Application de la fonction f(t) pour chaque composant
    x = f(x)
    y = f(y)
    z = f(z)

    # Calcul des valeurs L, A, B en utilisant les formules de conversion
    l = 116 * y - 16
    a = 500 * (x - y)
    b = 200 * (y - z)

    return l, a, b




# Conversion de LAB en RGB
def lab_2_rgb(l, a, b):
    x, y, z = lab_2_xyz(l, a, b)
    return xyz_2_rgb(x, y, z)


# Conversion de LAB en XYZ
def lab_2_xyz(l, a, b):
    # Valeurs des points de référence de XYZ (D65)
    x_ref, y_ref, z_ref = 0.95047, 1.00000, 1.08883
    
    y = (l + 16) / 116
    x = a / 500 + y
    z = y - b / 200
    

    def f_inv(t):
        delta = 6 / 29
        # Si t > delta^3, appliquer t^(1/3)
        if t > delta:
            return t**3
        # Sinon appliquer la formule alternative
        else:
            return (t - (16 / 116)) / 7.787
    
    #x = max(0, min(1, f_inv(x) * x_ref))
    #y = max(0, min(1, f_inv(y) * y_ref))
    #z = max(0, min(1, f_inv(z) * z_ref))

    # Application de f_inverse pour retrouver XYZ
    x = f_inv(x) * x_ref
    y = f_inv(y) * y_ref
    z = f_inv(z) * z_ref
    return x, y, z

# Conversion de XYZ en RGB
def xyz_2_rgb(x, y, z):
    # Matrice de transformation XYZ -> RGB
    r = 3.2406 * x - 1.5372 * y - 0.4986 * z
    g = -0.9689 * x + 1.8758 * y + 0.0415 * z
    b = 0.0556 * x - 0.2040 * y + 1.0570 * z
    
    r = r * 12.92 if r <= 0.0031308 else 1.055 * r ** (1 / 2.4) - 0.055
    g = g * 12.92 if g <= 0.0031308 else 1.055 * g ** (1 / 2.4) - 0.055
    b = b * 12.92 if b <= 0.0031308 else 1.055 * b ** (1 / 2.4) - 0.055
    
    # Gamma correction
    def gamma_correction(c):
        return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055

    r = gamma_correction(r)
    g = gamma_correction(g)
    b = gamma_correction(b)

    # Correction : Contraindre RGB à la plage [0, 255]
    r = int(max(0, min(255, r * 255)))
    g = int(max(0, min(255, g * 255)))
    b = int(max(0, min(255, b * 255)))

    
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