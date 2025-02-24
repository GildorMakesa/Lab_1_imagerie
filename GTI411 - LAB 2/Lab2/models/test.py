import cv2
import numpy as np
import matplotlib.pyplot as plt

# Charger une image (par exemple, une image de votre choix)
image = cv2.imread('C:/Users/Gildor/Desktop/GG.png')

# Appliquer les différents types de bordures
border_types = [
    cv2.BORDER_REPLICATE,  # Réplique les valeurs du bord
    cv2.BORDER_CONSTANT,   # Remplie avec une couleur constante
    cv2.BORDER_REFLECT,    # Réfléchit les bords
    cv2.BORDER_REFLECT_101, # Réfléchit les bords, mais différemment
    cv2.BORDER_WRAP        # Effectue un "wrap around" sur les bords
]

# Appliquer le traitement "abs and normalize to 255"
def abs_and_normalize_to_255(img):
    abs_img = cv2.absdiff(img, 0)  # Valeurs absolues
    norm_img = cv2.normalize(abs_img, None, 0, 255, cv2.NORM_MINMAX)  # Normalisation entre 0 et 255
    return norm_img

# Appliquer le traitement "abs and normalize 0 to 255"
def abs_and_normalize_0_to_255(img):
    abs_img = cv2.absdiff(img, 0)  # Valeurs absolues
    abs_img_clamped = np.clip(abs_img, 0, 255)  # Limiter entre 0 et 255
    return abs_img_clamped

# Appliquer le traitement "normalize 0 to 255"
def normalize_0_to_255(img):
    norm_img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)  # Normalisation entre 0 et 255
    return norm_img

# Appliquer le traitement "clamp 0...255"
def clamp_0_to_255(img):
    return np.clip(img, 0, 255)  # Limiter les valeurs entre 0 et 255

# Fonction pour ajouter un texte dans l'image (pour le titre de chaque bordure)
def add_title_to_border(image, title):
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(title, font, 1, 2)[0]
    text_x = (image.shape[1] - text_size[0]) // 2
    text_y = (image.shape[0] + text_size[1]) // 2
    cv2.putText(image, title, (text_x, text_y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    return image

# Affichage des résultats
fig, axes = plt.subplots(3, len(border_types) + 1, figsize=(15, 10))

# Affichage des bordures avec les titres
for i, border_type in enumerate(border_types):
    bordered_image = cv2.copyMakeBorder(image, 50, 50, 50, 50, border_type)
    bordered_image_with_title = add_title_to_border(bordered_image.copy(), f"Border {border_type}")
    axes[0, i].imshow(bordered_image_with_title, cmap='gray')
    axes[0, i].axis('off')

# Appliquer et afficher les différentes méthodes de traitement
processed_image_1 = abs_and_normalize_to_255(image)
processed_image_2 = abs_and_normalize_0_to_255(image)
processed_image_3 = normalize_0_to_255(image)
processed_image_4 = clamp_0_to_255(image)

# Affichage des images traitées
axes[1, 0].imshow(processed_image_1, cmap='gray')
axes[1, 0].set_title("Abs and Normalize to 255")
axes[1, 0].axis('off')

axes[1, 1].imshow(processed_image_2, cmap='gray')
axes[1, 1].set_title("Abs and Normalize 0 to 255")
axes[1, 1].axis('off')

axes[1, 2].imshow(processed_image_3, cmap='gray')
axes[1, 2].set_title("Normalize 0 to 255")
axes[1, 2].axis('off')

axes[1, 3].imshow(processed_image_4, cmap='gray')
axes[1, 3].set_title("Clamp 0...255")
axes[1, 3].axis('off')

# Pour chaque bordure et chaque traitement, afficher l'original avec les modifications
axes[2, 0].imshow(image, cmap='gray')
axes[2, 0].set_title("Original Image")
axes[2, 0].axis('off')

plt.tight_layout()
plt.show()
