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




        dft_shift = transforme_de_fourier(image)
        masque = creer_masque_passe_bas(image, self.cutoff_freq)
        dft_shift_filtered = appliquer_masque(dft_shift, masque)

   
        original_image_spectrum = calculer_spectre_magnitude(dft_shift)
        ideal_filter_spectrum = calculer_spectre_magnitude(dft_shift_filtered)


        ideal_filter_recons = appliquer_filtre(dft_shift_filtered)





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

        original_image_spectrum = create_fake_image(image, "Orig spectrum")
        ideal_filter_spectrum = create_fake_image(image, "Ideal spectrum") 
        ideal_filter_recons = create_fake_image(image, "Ideal recons") 

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

        original_image_spectrum = create_fake_image(image, "Orig spectrum")
        butter_filter_spectrum = create_fake_image(image, "Butter spectrum") 
        butter_filter_recons = create_fake_image(image, "Butter recons") 

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

        original_image_spectrum = create_fake_image(image, "Orig spectrum")
        butter_filter_spectrum = create_fake_image(image, "Butter spectrum") 
        butter_filter_recons = create_fake_image(image, "Butter recons") 

        images = {
            'original_spectrum': original_image_spectrum,
            'butter_spectrum': butter_filter_spectrum,
            'butter_recons': butter_filter_recons,
        }
        return images
    
################################################################################



def transforme_de_fourier(image):
    spectre_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    dft = np.fft.fft2(spectre_gray)
    dft_shift = np.fft.fftshift(dft)
    
    return dft_shift

def appliquer_masque(dft_shift, masque):
    return dft_shift * masque

def calculer_spectre_magnitude(dft_shift_filtered):
    magnitude_spectrum = np.abs(dft_shift_filtered)
    magnitude_spectrum = np.log(magnitude_spectrum + 1)
    magnitude_spectrum = np.uint8(255 * magnitude_spectrum / np.max(magnitude_spectrum))
    
    return cv2.merge([magnitude_spectrum, magnitude_spectrum, magnitude_spectrum])

def creer_masque_passe_bas(image, cutoff_freq):
    rows, cols, _ = image.shape

    masque = np.zeros((rows, cols), dtype=np.float32)
    crow, ccol = rows // 2, cols // 2
    
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - crow)**2 + (j - ccol)**2)
            if distance <= cutoff_freq:
                masque[i, j] = 1 
    
    return masque

def creer_masque_passe_haut(rows, cols, cutoff_freq):
    masque = np.ones((rows, cols), dtype=np.float32)
    crow, ccol = rows // 2, cols // 2
    
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - crow)**2 + (j - ccol)**2)
            if distance <= cutoff_freq:
                masque[i, j] = 0
    
    return masque


def appliquer_filtre(dft_shift_filtered):
    dft_filtered = np.fft.ifftshift(dft_shift_filtered)
    image_filtree = np.fft.ifft2(dft_filtered)
    image_filtree = np.abs(image_filtree)
    
    image_filtree = np.uint8(255 * (image_filtree / np.max(image_filtree))) #normalize
    
    return cv2.merge([image_filtree, image_filtree, image_filtree])