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


class CannyFilterModel:
    def __init__(self) -> None:
        self.source_image = None
        self.gaussian_filter_size = 0
        self.min_threshold = 0
        self.max_threshold = 0

    
    def update_min_threshold(self, value:int):
        self.min_threshold = int(value)
        

    def update_max_threshold(self, value:int):
        self.max_threshold = int(value)


    def update_gaussian_filter_size(self, value:int):
        self.gaussian_filter_size = int(value)


    
    def apply_filter(self):
        if self.source_image is None:
            return None
        image = self.source_image.copy()

        print(f"Applying with {self.gaussian_filter_size}")
        print(f"Applying with {self.min_threshold}")
        print(f"Applying with {self.max_threshold}")


        # TODO: Replace these with correct images
        smoothed_image = create_fake_image(image, "smoothed")
        gradx_image = create_fake_image(image, "gradient_x")
        grady_image = create_fake_image(image, "gradient_y")
        locmax_image = self.locmax_image(image, 3)
        final_image = create_fake_image(image, "final")


        images = {
            'smoothed': smoothed_image,
            'gradient_x': gradx_image,
            'gradient_y': grady_image,
            'local_maxima': locmax_image,
            'final': final_image,
        }


        return images
    

    def locmax_image(self, image, neighborhood_size=3):
        #convert to grayscale
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #reflection des bords
        pad_size = neighborhood_size // 2
        padded_image = cv2.copyMakeBorder(image, pad_size, pad_size, pad_size, pad_size, cv2.BORDER_REFLECT)

        locmax = np.zeros_like(image, dtype=np.uint8)

        #trouve les maximums
        for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                neighborhood = padded_image[y:y + neighborhood_size, x:x + neighborhood_size]

                if image[y, x] == np.max(neighborhood) and image[y, x] != np.min(neighborhood):
                    locmax[y, x] = 255

        #back to rgb
        locmax_rgb = cv2.cvtColor(locmax, cv2.COLOR_GRAY2BGR)

        return locmax_rgb

