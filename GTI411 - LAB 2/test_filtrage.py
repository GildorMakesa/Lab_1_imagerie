import cv2
import numpy as np
import matplotlib.pyplot as plt

# Charger une image en niveaux de gris
image = cv2.imread('C:/Users/Gildor/Desktop/Capture_aaa.png', cv2.IMREAD_GRAYSCALE)

# Fonction pour calculer la transformée de Fourier et centrer le spectre
def fourier_transform(image):
    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)
    return dft, dft_shift

# Fonction pour appliquer un filtre passe-bas/passe-haut idéal
def ideal_filter(shape, D0, filter_type='low'):
    rows, cols = shape
    center = (rows // 2, cols // 2)
    mask = np.zeros((rows, cols), dtype=np.float32)
    for u in range(rows):
        for v in range(cols):
            D = np.sqrt((u - center[0])**2 + (v - center[1])**2)
            if filter_type == 'low':
                mask[u, v] = 1 if D <= D0 else 0
            elif filter_type == 'high':
                mask[u, v] = 0 if D <= D0 else 1
    return mask

# Fonction pour appliquer un filtre Butterworth
def butterworth_filter(shape, D0, n, filter_type='low'):
    rows, cols = shape
    center = (rows // 2, cols // 2)
    mask = np.zeros((rows, cols), dtype=np.float32)
    for u in range(rows):
        for v in range(cols):
            D = np.sqrt((u - center[0])**2 + (v - center[1])**2)
            if filter_type == 'low':
                mask[u, v] = 1 / (1 + (D / D0)**(2 * n))
            elif filter_type == 'high':
                mask[u, v] = 1 / (1 + (D0 / D)**(2 * n)) if D != 0 else 0
    return mask

# Fonction pour appliquer un filtre gaussien
def gaussian_filter(shape, D0, filter_type='low'):
    rows, cols = shape
    center = (rows // 2, cols // 2)
    mask = np.zeros((rows, cols), dtype=np.float32)
    for u in range(rows):
        for v in range(cols):
            D = np.sqrt((u - center[0])**2 + (v - center[1])**2)
            if filter_type == 'low':
                mask[u, v] = np.exp(-(D**2) / (2 * (D0**2)))
            elif filter_type == 'high':
                mask[u, v] = 1 - np.exp(-(D**2) / (2 * (D0**2)))
    return mask

# Appliquer un filtre au spectre
def apply_filter(dft_shift, filter_mask):
    filtered_dft = dft_shift * filter_mask
    return filtered_dft

# Reconstruction de l'image depuis le spectre filtré
def inverse_fourier(filtered_dft):
    idft_shift = np.fft.ifftshift(filtered_dft)
    image_reconstructed = np.fft.ifft2(idft_shift)
    return np.abs(image_reconstructed)

# Paramètres
D0 = 50  # Rayon de coupure
n = 2    # Ordre pour Butterworth

# Transformée de Fourier
dft, dft_shift = fourier_transform(image)

# Création des filtres
ideal_low = ideal_filter(image.shape, D0, 'low')
ideal_high = ideal_filter(image.shape, D0, 'high')
butterworth_low = butterworth_filter(image.shape, D0, n, 'low')
butterworth_high = butterworth_filter(image.shape, D0, n, 'high')
gaussian_high = gaussian_filter(image.shape, D0, 'high')

# Application des filtres
filtered_ideal_low = apply_filter(dft_shift, ideal_low)
filtered_ideal_high = apply_filter(dft_shift, ideal_high)
filtered_butterworth_low = apply_filter(dft_shift, butterworth_low)
filtered_butterworth_high = apply_filter(dft_shift, butterworth_high)
filtered_gaussian_high = apply_filter(dft_shift, gaussian_high)

# Reconstruction des images
reconstructed_ideal_low = inverse_fourier(filtered_ideal_low)
reconstructed_ideal_high = inverse_fourier(filtered_ideal_high)
reconstructed_butterworth_low = inverse_fourier(filtered_butterworth_low)
reconstructed_butterworth_high = inverse_fourier(filtered_butterworth_high)
reconstructed_gaussian_high = inverse_fourier(filtered_gaussian_high)

# Affichage des résultats
filters = {
    'Original': image,
    'Ideal Low': reconstructed_ideal_low,
    'Ideal High': reconstructed_ideal_high,
    'Butterworth Low': reconstructed_butterworth_low,
    'Butterworth High': reconstructed_butterworth_high,
    'Gaussian High': reconstructed_gaussian_high,
}

plt.figure(figsize=(8, 6))
for i, (title, img) in enumerate(filters.items()):
    plt.subplot(3, 2, i + 1)
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
plt.tight_layout()
plt.show()
