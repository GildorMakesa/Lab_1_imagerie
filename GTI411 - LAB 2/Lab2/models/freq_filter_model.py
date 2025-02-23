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

        original_image_spectrum = visualize_spectrum(get_image_spectrum(image))
        ideal_filter_spectrum = visualize_spectrum(ideal_lowpass_filter(get_image_spectrum(image), self.cutoff_freq))
        ideal_filter_recons = create_fake_image(image, "Ideal recons") 

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

def get_image_spectrum(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)
    
    magnitude_spectrum = 20 * np.log(np.abs(dft_shift) + 1)  # Adding 1 to avoid log(0)

    spectrum_image = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    
    #Create an RGB image by stacking the grayscale image across three channels
    #rgb_spectrum_image = cv2.merge([spectrum_image, spectrum_image, spectrum_image])
    
    return spectrum_image


def visualize_spectrum(spectrum_image):
    return cv2.merge([spectrum_image, spectrum_image, spectrum_image])



def ideal_lowpass_filter(spectrum_image, cutoff_freq):
    height, width = spectrum_image.shape[:2]

    x = np.arange(-width // 2, width // 2)
    y = np.arange(-height // 2, height // 2)
    X, Y = np.meshgrid(x, y)

    D = np.sqrt(X**2 + Y**2)
    H = np.zeros((height, width))
    H[D <= cutoff_freq] = 1

    dft = np.fft.fft2(spectrum_image)
    dft_shift = np.fft.fftshift(dft)
    filtered_spectrum = dft_shift * H

    filtered_image = np.fft.ifft2(np.fft.ifftshift(filtered_spectrum))

    filtered_image_magnitude = np.abs(filtered_image)
    filtered_image_normalized = cv2.normalize(filtered_image_magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    return filtered_image_normalized