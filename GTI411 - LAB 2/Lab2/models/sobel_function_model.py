import cv2 
import numpy as np

class FilterFunction():
     
    def __init__(self,filtering_method, kernel_size, handling_border_method, range_method):
        # L'attribut kernel_size est défini lors de l'initialisation de l'objet
        self.filtering_method = filtering_method
        self.kernel_size = kernel_size  # Définit l'attribut kernel_size
        self.handling_border_method = handling_border_method
        self.range_method = range_method


    def apply_sobel_y(self, image):
        if self.kernel_size == 0:
            update_ksize = 0
        else:
            update_ksize = max(0, self.kernel_size | 1)
        
        border_methods = {
            "None": cv2.BORDER_CONSTANT,
            "Copy": cv2.BORDER_REPLICATE,
            "Circular": cv2.BORDER_REFLECT,
            "Mirror": cv2.BORDER_REFLECT101,
        }
        update_border_type = border_methods.get(self.handling_border_method, cv2.BORDER_DEFAULT)

        grad_y = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=update_ksize, borderType=update_border_type)
            
            
        if self.range_method == "Abs and normalize to 255":
            sobel_image = np.abs(grad_y)
            sobel_image = cv2.normalize(sobel_image, None, 0, 255, cv2.NORM_MINMAX)
    
        elif self.range_method == "Abs and normalize 0 to 255":
            sobel_image = np.abs(grad_y)
            sobel_image = np.clip(sobel_image, None, 0, 255, cv2.NORM_MINMAX)
        
        elif self.range_method == "Normalize 0 to 255":
            sobel_image = cv2.normalize(grad_y, 0, 255).astype(np.uint8)
        
        elif self.range_method == "Clamp 0 ... 255":
            sobel_image = np.clip(grad_y, 0, 255).astype(np.uint8)


        sobel_image = np.clip(grad_y, 0, 255).astype(np.uint8)
        print("Filtre Sobel applique")
        return sobel_image


    def apply_sobel_x(self, image):
        if self.kernel_size == 0:
            update_ksize = 0
        else:
            update_ksize = max(0, self.kernel_size | 1)
        
        border_methods = {
            "None": cv2.BORDER_CONSTANT,
            "Copy": cv2.BORDER_REPLICATE,
            "Circular": cv2.BORDER_REFLECT,
            "Mirror": cv2.BORDER_REFLECT101,
        }
        update_border_type = border_methods.get(self.handling_border_method, cv2.BORDER_DEFAULT)

        grad_x = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=update_ksize, borderType=update_border_type)
            
        if self.range_method == "Abs and normalize to 255":
            sobel_image = np.abs(grad_x)
            sobel_image = cv2.normalize(sobel_image, None, 0, 255, cv2.NORM_MINMAX)
    
        elif self.range_method == "Abs and normalize 0 to 255":
            sobel_image = np.abs(grad_x)
            sobel_image = np.clip(sobel_image, None, 0, 255, cv2.NORM_MINMAX)
        
        elif self.range_method == "Normalize 0 to 255":
            sobel_image = cv2.normalize(grad_x, 0, 255).astype(np.uint8)
        
        elif self.range_method == "Clamp 0 ... 255":
            sobel_image = np.clip(grad_x, 0, 255).astype(np.uint8)


        sobel_image = np.clip(grad_x, 0, 255).astype(np.uint8)
        print("Filtre Sobel applique")
        return sobel_image

    def apply_sobel(self, image):
        if self.kernel_size == 0:
            update_ksize = 0
        else:
            update_ksize = max(0, self.kernel_size | 1)
        
        border_methods = {
            "None": cv2.BORDER_CONSTANT,
            "Copy": cv2.BORDER_REPLICATE,
            "Circular": cv2.BORDER_REFLECT,
            "Mirror": cv2.BORDER_REFLECT101,
        }
        update_border_type = border_methods.get(self.handling_border_method, cv2.BORDER_DEFAULT)

        grad_x = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=update_ksize, borderType=update_border_type)
        grad_y = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=update_ksize, borderType=update_border_type)
        magnitude_sobel_image = cv2.magnitude(grad_x, grad_y)
        
        if self.range_method == "Abs and normalize to 255":
            sobel_image = cv2.convertScaleAbs(magnitude_sobel_image)
        elif self.range_method == "Abs and normalize 0 to 255":
            sobel_image = cv2.normalize(np.abs(magnitude_sobel_image), None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        elif self.range_method == "Normalize 0 to 255":
            sobel_image = cv2.normalize(magnitude_sobel_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        else:
            sobel_image = np.clip(magnitude_sobel_image, 0, 255).astype(np.uint8)
        
        return sobel_image