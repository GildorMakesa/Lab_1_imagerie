import cv2
import numpy as np
from .sobel_function_model import FilterFunction

class SpatialFilterModel:
    def __init__(self) -> None:
        self.source_image = None
        self.range_method = "Clamp 0 ... 255"
        self.filtering_method = "Mean"
        self.handling_border_method = "0"
        self.kernel_size = 0

    def update_kernel_size(self, kernel: int):
        self.kernel_size = kernel

    def update_range_method(self, mtd: str):
        self.range_method = mtd

    def update_filtering_method(self, mtd: str):
        self.filtering_method = mtd

    def update_handling_border_method(self, mtd: str):
        self.handling_border_method = mtd
    
    
    def apply_gaussian(self, image):
        if self.kernel_size <= 0 or self.kernel_size % 2 == 0:
            print("Kernel size is invalid, using default kernel size + 1.")
            self.kernel_size += 1
        
        border_methods = {
            "None": cv2.BORDER_CONSTANT,
            "Copy": cv2.BORDER_REPLICATE,
            "Circular": cv2.BORDER_REFLECT,
            "Mirror": cv2.BORDER_REFLECT101,
        }
        update_border_type = border_methods.get(self.handling_border_method, cv2.BORDER_DEFAULT)

        gaussian_image = cv2.GaussianBlur(image, (self.kernel_size, self.kernel_size), 0, borderType=update_border_type)
        
        if self.range_method == "Abs and normalize to 255":
            gaussian_image = cv2.convertScaleAbs(gaussian_image)
        elif self.range_method == "Abs and normalize 0 to 255":
            gaussian_image = cv2.normalize(np.abs(gaussian_image), None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        elif self.range_method == "Normalize 0 to 255":
            gaussian_image = cv2.normalize(gaussian_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        else:
            gaussian_image = np.clip(gaussian_image, 0, 255).astype(np.uint8)
        
        print("Gaussian filter applied.")
        return gaussian_image
    

    def apply_median(self, image):
        if self.kernel_size <= 0 or self.kernel_size % 2 == 0:
            print("Kernel size is invalid, using default kernel size + 1.")
            self.kernel_size += 1
        
        median_image = cv2.medianBlur(image, self.kernel_size)
        
        if self.range_method == "Abs and normalize to 255":
            median_image = cv2.convertScaleAbs(median_image)
        elif self.range_method == "Abs and normalize 0 to 255":
            median_image = cv2.normalize(np.abs(median_image), None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        elif self.range_method == "Normalize 0 to 255":
            median_image = cv2.normalize(median_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        else:
            median_image = np.clip(median_image, 0, 255).astype(np.uint8)
        
        print("Median filter applied.")
        return median_image
    

    def apply_filter(self):
        if self.source_image is None:
            return None
        image = self.source_image.copy()

        sobel_func = FilterFunction(self.filtering_method,self.kernel_size,self.handling_border_method,self.range_method)
        print(f"Applying with Filtre : {self.filtering_method}")
        print(f"Applying with Kernel : {self.kernel_size}")
        print(f"Applying with Bordure : {self.handling_border_method}")
        print(f"Applying with Range : {self.range_method}")

        filters = {
            "Sobel": sobel_func.apply_sobel,
            "Sobel y-axis" : sobel_func.apply_sobel_y,
            "Sobel x-axis" : sobel_func.apply_sobel_x,
            "Gaussian": self.apply_gaussian,
            "Median ": self.apply_median,
            
        }

        filter_func = filters.get(self.filtering_method)
        if filter_func:
            return filter_func(image)
        else:
            print(f"Filter '{self.filtering_method}' not recognized by the dictionnary.")
            return image
