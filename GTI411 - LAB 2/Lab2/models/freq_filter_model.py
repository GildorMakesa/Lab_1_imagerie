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
    
    tf_channels = []
    for channel in channels:
        tf = np.fft.fft2(channel)
        tf_shift = np.fft.fftshift(tf)
        tf_channels.append(tf_shift)
    
    return tf_channels

def apply_filtre(tf_shift_channels, filtre):
    tf_shift_filtered = [tf_shift * filtre for tf_shift in tf_shift_channels]
    return tf_shift_filtered

def calculer_spectre_magnitude(tf_shift_filtered_channels):
    magnitude_spectra = []

    for tf_shift_filtered in tf_shift_filtered_channels:
        magnitude_spectrum = np.abs(tf_shift_filtered)
        magnitude_spectrum = np.log(magnitude_spectrum + 1)
        magnitude_spectrum = np.uint8(255 * magnitude_spectrum / np.max(magnitude_spectrum))
        magnitude_spectra.append(magnitude_spectrum)
    
    return cv2.merge(magnitude_spectra)

def transforme_de_fourier_inverse(tf_shift_filtered_channels):
    image_filtree_channels = []
    
    for tf_shift_filtered in tf_shift_filtered_channels:
        tf_filtered = np.fft.ifftshift(tf_shift_filtered)
        image_filtree = np.fft.ifft2(tf_filtered)
        image_filtree = np.abs(image_filtree)
        image_filtree = np.uint8(255 * (image_filtree / np.max(image_filtree)))
        image_filtree_channels.append(image_filtree)
    
    return cv2.merge(image_filtree_channels)


def butterworth_lowpass_filter(image, cutoff_freq, n_params_butter):
    rows, cols, _ = image.shape

    y, x = np.ogrid[:rows, :cols]
    center_row, center_col = rows // 2, cols // 2
    distance = np.sqrt((y - center_row) ** 2 + (x - center_col) ** 2)
    
    return 1 / (1 + (distance / cutoff_freq) ** (2 * n_params_butter))

def butterworth_highpass_filter(image, cutoff_freq, n_params_butter):
    rows, cols, _ = image.shape

    y, x = np.ogrid[:rows, :cols]
    center_row, center_col = rows // 2, cols // 2
    distance = np.sqrt((y - center_row) ** 2 + (x - center_col) ** 2)
    
    return 1 / (1 + (cutoff_freq / np.maximum(distance, 1e-6)) ** (2 * n_params_butter))

def ideal_lowpass_filter(image, cutoff_freq):
    rows, cols, _ = image.shape

    y, x = np.ogrid[:rows, :cols]
    center_row, center_col = rows // 2, cols // 2
    distance = np.sqrt((y - center_row) ** 2 + (x - center_col) ** 2)
    
    return (distance <= cutoff_freq).astype(np.float32)

def ideal_highpass_filter(image, cutoff_freq):
    return 1 - ideal_lowpass_filter(image, cutoff_freq)