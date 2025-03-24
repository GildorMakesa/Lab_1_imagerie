import cv2
import numpy as np

class FloodFillModel:
    def __init__(self) -> None:
        self.low_threshold = 0
        self.high_treshold = 10

        self.fill_color = [255, 0, 0]


    
    def fill(self, image, x, y):
        # Convertir en niveaux de gris pour déterminer la région
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

          
        seed_value = gray[y, x]

        
        lower_bound = max(0, seed_value - self.low_threshold)
        upper_bound = min(255, seed_value + self.high_threshold)

        
        h, w = image.shape[:2]
        mask = np.zeros((h+2, w+2), dtype=np.uint8)

        
        cv2.floodFill(
            image, mask, (x, y), self.fill_color,
            (self.low_threshold,) * 3,  
            (self.high_threshold,) * 3,  
            cv2.FLOODFILL_FIXED_RANGE
        )

        return image

    
    def set_fill_color(self, color):
        self.fill_color = color


    def set_low_threshold(self, val):
        self.low_threshold = val
        print(f"New low threshold = {val}")


    def set_high_threshold(self, val):
        self.high_threshold = val
        print(f"New high threshold = {val}")
