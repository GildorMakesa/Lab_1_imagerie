import numpy as np
import cv2

import sys
sys.setrecursionlimit(100000)


def is_close(vec1, vec2):
    max_diff = np.max(np.abs(vec1 - vec2))
    return max_diff < 50


class DrawShapeModel:
    def __init__(self) -> None:
        w, h = 1250, 490
        self.shape_type = 'Circle'
        self.color = [255, 0, 0]
        self.line_thickness = 3
        self.image = np.ones((h, w, 3)) * np.array([255, 255, 255])
        self.image = self.image.astype(np.uint8)
        self.fill_color = np.array([255, 255, 0])
        self.boundary_color = np.array([255, 0, 0])
    
    def update_shape_type(self, shape_type:str):
        print(f"New shape type {shape_type}")
        self.shape_type = shape_type


    def update_color(self, r, g, b):
        self.color = [r, g, b]

    def draw_line_manual(self, start_point: tuple[int], end_point: tuple[int]):
        x1, y1 = start_point
        x2, y2 = end_point

        # Assurez-vous que x1 <= x2
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            
        m = (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')  # S'assurer de ne pas diviser par zéro
        y = y1
        for x in range(x1, x2 + 1):
            if m == float('inf'):
                # Cas spécial où la ligne est verticale
                self.image[int(y1), x] = self.color
            else:
                # Ici on arrondit les valeurs de y pour obtenir des indices entiers
                self.image[int(round(y)), x] = self.color
                y += m


    def draw_shape(self, start_point:tuple[int], end_point:tuple[int]):
        """Draw shape at the desired location based on the starting point and end point.

        You can use self.color to get the color selected with the picker
        Implement the logic for 'Line', 'Circle' and 'Rectangle'

        Args:
            start_point (tuple[int]): Coordinates (x,y) of the click point
            end_point (tuple[int]): Coordinates (x,y) of the released point

        Returns:
            np.ndarray: Image with the shape on it
        """
        if start_point is None or end_point is None or len(start_point) == 0 or len(end_point) == 0:
            return
        print(f"Drawing shape {self.shape_type} at p1={start_point} p2={end_point}")

        # TODO 
        if self.shape_type == "Line":
            self.draw_line_manual(start_point, end_point)
        
        return self.image