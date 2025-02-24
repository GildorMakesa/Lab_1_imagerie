
import numpy as np
import cv2 
from .filter_function_model import FilterFunction



class SpatialFilterModel:
    def __init__(self) -> None:
        self.source_image = None
        self.range_method = "Clamp 0 ... 255"
        self.filtering_method = "Mean"
        self.handling_border_method = "0"
        self.kernel_size = 0

    
    def update_kernel_size(self, kernel:int):
        self.kernel_size = kernel

    def update_range_method(self, mtd:str):
        self.range_method = mtd

    def update_filtering_method(self, mtd:str):
        self.filtering_method = mtd


    def update_handling_border_method(self, mtd:str):
        self.handling_border_method = mtd

    
    

    def apply_filter(self):
        if self.source_image is None:
            return None
        image = self.source_image.copy()

        print(f"Applying with {self.filtering_method}")
        print(f"Applying with {self.kernel_size}")
        print(f"Applying with {self.handling_border_method}")
        print(f"Applying with {self.range_method}")

         # Crée une instance de FilterFunction
        filter_function_instance = FilterFunction(self.filtering_method,self.kernel_size,self.handling_border_method,self.range_method)

        # Dictionnaire des filtres
        filters = {
            "Sobel": filter_function_instance.apply_sobel,
            "Sobel x-axis": filter_function_instance.apply_sobel_x,
            "Sobel y-axis": filter_function_instance.apply_sobel_y,
            "Gaussian": filter_function_instance.apply_gaussian,
            "Median ": filter_function_instance.apply_median,

        }

         # Vérifiez si le filtre existe dans le dictionnaire et l'utiliser
        filter_func = filters.get(self.filtering_method)
        if filter_func:
            return filter_func(image)
        else:
            print(f"Filter '{self.filtering_method}' not recognized.")
            return image  # Retourne l'image 