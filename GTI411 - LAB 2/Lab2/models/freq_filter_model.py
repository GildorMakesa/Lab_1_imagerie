import cv2
import numpy as np


def create_fake_image(image, text:str):
    fake_image = np.zeros_like(image, dtype=np.uint8)
    height = image.shape[0]

    font_size = 1
    color = (0, 255, 0)
    font_weight = 2
    fake_image = cv2.putText(fake_image, text, (20, round(height//2)), cv2.FONT_HERSHEY_SIMPLEX, font_size, color, font_weight)

    return fake_image


class FrequencyFilterModel:
    def __init__(self) -> None:
        self.source_image = None
        self.cutoff_freq:int = 0
        self.n_params_butter:int = 0


    def update_cutoff(self, value:int):
        self.cutoff_freq = int(value)
        

    def update_n_params_butter(self, value:int):
        self.n_params_butter = int(value)

    
    def apply_ideal_lowpass_filter(self):
        if self.source_image is None:
            return None
        image = self.source_image.copy()

        print(f"Applying with ideal lowpass with:  {self.cutoff_freq}")

        imge_2_tf = transforme_de_fourier(image)
        filtre = ideal_lowpass_filter(image, self.cutoff_freq)
        tf_2_filtre = apply_filtre(imge_2_tf, filtre)

   
        original_image_spectrum = calculer_spectre_magnitude(imge_2_tf)
        ideal_filter_spectrum = calculer_spectre_magnitude(tf_2_filtre)
        ideal_filter_recons = transforme_de_fourier_inverse(tf_2_filtre)

        images = {
            'original_spectrum': original_image_spectrum,
            'ideal_spectrum': ideal_filter_spectrum,
            'ideal_recons': ideal_filter_recons,
        }
        return images
    

    def apply_ideal_highpass_filter(self):
        if self.source_image is None:
            return None
        image = self.source_image.copy()

        print(f"Applying with ideal highpass with: {self.cutoff_freq}")

        imge_2_tf = transforme_de_fourier(image)
        filtre = ideal_highpass_filter(image, self.cutoff_freq)
        tf_2_filtre = apply_filtre(imge_2_tf, filtre)

   
        original_image_spectrum = calculer_spectre_magnitude(imge_2_tf)
        ideal_filter_spectrum = calculer_spectre_magnitude(tf_2_filtre)
        ideal_filter_recons = transforme_de_fourier_inverse(tf_2_filtre)

        images = {
            'original_spectrum': original_image_spectrum,
            'ideal_spectrum': ideal_filter_spectrum,
            'ideal_recons': ideal_filter_recons,
        }
        return images

        
    def apply_butterworth_lowpass_filter(self):
        if self.source_image is None:
            return None
        image = self.source_image.copy()

        print(f"Applying with Butter lowpass with: {self.n_params_butter}")

        imge_2_tf = transforme_de_fourier(image)
        filtre = butterworth_lowpass_filter(image, self.cutoff_freq, self.n_params_butter)
        tf_2_filtre = apply_filtre(imge_2_tf, filtre)

        original_image_spectrum = calculer_spectre_magnitude(imge_2_tf)
        butter_filter_spectrum = calculer_spectre_magnitude(tf_2_filtre)
        butter_filter_recons = transforme_de_fourier_inverse(tf_2_filtre)

        images = {
            'original_spectrum': original_image_spectrum,
            'butter_spectrum': butter_filter_spectrum,
            'butter_recons': butter_filter_recons,
        }
        return images
    

    def apply_butterworth_highpass_filter(self):
        if self.source_image is None:
            return None
        image = self.source_image.copy()

        print(f"Applying with Butter highpass with: {self.n_params_butter}")

        imge_2_tf = transforme_de_fourier(image)
        filtre = butterworth_highpass_filter(image, self.cutoff_freq, self.n_params_butter)
        tf_2_filtre = apply_filtre(imge_2_tf, filtre)

        original_image_spectrum = calculer_spectre_magnitude(imge_2_tf)
        butter_filter_spectrum = calculer_spectre_magnitude(tf_2_filtre)
        butter_filter_recons = transforme_de_fourier_inverse(tf_2_filtre)

        images = {
            'original_spectrum': original_image_spectrum,
            'butter_spectrum': butter_filter_spectrum,
            'butter_recons': butter_filter_recons,
        }
        return images
    

def transforme_de_fourier(image):
    channels = cv2.split(image)
    
    dft_channels = []
    for channel in channels:
        dft = np.fft.fft2(channel)
        dft_shift = np.fft.fftshift(dft)
        dft_channels.append(dft_shift)
    
    return dft_channels

def apply_filtre(dft_shift_channels, filtre):
    dft_shift_filtered = [dft_shift * filtre for dft_shift in dft_shift_channels]
    return dft_shift_filtered

def calculer_spectre_magnitude(dft_shift_filtered_channels):
    magnitude_spectra = []

    for dft_shift_filtered in dft_shift_filtered_channels:
        magnitude_spectrum = np.abs(dft_shift_filtered)
        magnitude_spectrum = np.log(magnitude_spectrum + 1)
        magnitude_spectrum = np.uint8(255 * magnitude_spectrum / np.max(magnitude_spectrum))
        magnitude_spectra.append(magnitude_spectrum)
    
    return cv2.merge(magnitude_spectra)

def ideal_lowpass_filter(image, cutoff_freq):
    rows, cols, _ = image.shape
    filtre = np.zeros((rows, cols), dtype=np.float32)
    crow, ccol = rows // 2, cols // 2
    
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - crow)**2 + (j - ccol)**2)
            if distance <= cutoff_freq:
                filtre[i, j] = 1
    
    return filtre

def ideal_highpass_filter(image, cutoff_freq):
    rows, cols, _ = image.shape
    filtre = np.ones((rows, cols), dtype=np.float32)
    crow, ccol = rows // 2, cols // 2
    
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - crow)**2 + (j - ccol)**2)
            if distance <= cutoff_freq:
                filtre[i, j] = 0
    
    return filtre

def transforme_de_fourier_inverse(dft_shift_filtered_channels):
    image_filtree_channels = []
    
    for dft_shift_filtered in dft_shift_filtered_channels:
        dft_filtered = np.fft.ifftshift(dft_shift_filtered)
        image_filtree = np.fft.ifft2(dft_filtered)
        image_filtree = np.abs(image_filtree)
        image_filtree = np.uint8(255 * (image_filtree / np.max(image_filtree)))
        image_filtree_channels.append(image_filtree)
    
    return cv2.merge(image_filtree_channels)


def butterworth_lowpass_filter(image, cutoff_freq, n_params_butter):
    rows, cols, _ = image.shape
    filtre = np.zeros((rows, cols), dtype=np.float32)
    crow, ccol = rows // 2, cols // 2
    
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - crow)**2 + (j - ccol)**2)
            filtre[i, j] = 1 / (1 + (distance / cutoff_freq)**(2 * n_params_butter))
    
    return filtre

def butterworth_highpass_filter(image, cutoff_freq, n_params_butter):
    rows, cols, _ = image.shape
    filtre = np.ones((rows, cols), dtype=np.float32)
    crow, ccol = rows // 2, cols // 2
    
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - crow)**2 + (j - ccol)**2)
            filtre[i, j] = 1 / (1 + (cutoff_freq / distance)**(2 * n_params_butter)) if distance != 0 else 1
    
    return filtre