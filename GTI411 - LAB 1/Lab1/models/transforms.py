import numpy as np
import matplotlib.pyplot as plt
import cv2

class Lab1ImageTransformsModel:
    
    def __init__(self) -> None:
        self.luminosity = 0
        self.contrast = 1
        self.image = None


    def set_image(self, image):
        self.image = image


    def transform_image(self, contrast, luminosity):
        hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV) #so opencv can play with the image
        
        hsv_image = hsv_image.astype(np.float32) #opencv arithmetic conversion
        
        hsv_image[..., 1] = hsv_image[..., 1] * contrast #Apply contrast to S (saturation of HSV)
        hsv_image[..., 1] = np.clip(hsv_image[..., 1], 0, 255)

        hsv_image[..., 2] = hsv_image[..., 2] + luminosity #Apply luminosity to v (value of HSV)
        hsv_image[..., 2] = np.clip(hsv_image[..., 2], 0, 255)
        
        hsv_image = hsv_image.astype(np.uint8) #opencv arithmetic conversion
        
        transformed_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR) #RGB conversion
        
        return transformed_image