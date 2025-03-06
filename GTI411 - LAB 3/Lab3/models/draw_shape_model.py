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
    
    def update_shape_type(self, shape_type: str):
        print(f"New shape type {shape_type}")
        self.shape_type = shape_type

    def update_color(self, r, g, b):
        self.color = [r, g, b]

    def draw_line_bresenham(self, start_point: tuple[int, int], end_point: tuple[int, int]):
        x1, y1 = start_point
        x2, y2 = end_point

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            self.image[y1, x1] = self.color  # Place le pixel

            if x1 == x2 and y1 == y2:
                break  # Stop quand on atteint la fin

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy
    def draw_circle_bresenham(self, center: tuple[int, int], radius: int):
        x0, y0 = center
        x, y = radius, 0  # Premier point (radius, 0)
        d = 3 - 2 * radius  # Décision initiale

        while x >= y:
            # Tracer les 8 symétries
            self.image[y0 + y, x0 + x] = self.color
            self.image[y0 + y, x0 - x] = self.color
            self.image[y0 - y, x0 + x] = self.color
            self.image[y0 - y, x0 - x] = self.color
            self.image[y0 + x, x0 + y] = self.color
            self.image[y0 + x, x0 - y] = self.color
            self.image[y0 - x, x0 + y] = self.color
            self.image[y0 - x, x0 - y] = self.color

            y += 1  # On avance en hauteur

            # Vérification de l'erreur et mise à jour
            if d > 0:
                x -= 1  # Réduire x si on dépasse
                d += 4 * (y - x) + 10
            else:
                d += 4 * y + 6  # Continuer sans réduire x


    def draw_shape(self, start_point: tuple[int, int], end_point: tuple[int, int]):
        """Draw shape at the desired location based on the starting point and end point.

        You can use self.color to get the color selected with the picker
        Implement the logic for 'Line', 'Circle' and 'Rectangle'

        Args:
            start_point (tuple[int, int]): Coordinates (x,y) of the click point
            end_point (tuple[int, int]): Coordinates (x,y) of the released point

        Returns:
            np.ndarray: Image with the shape on it
        """
        if start_point is None or end_point is None or len(start_point) == 0 or len(end_point) == 0:
            return
        print(f"Drawing shape {self.shape_type} at p1={start_point} p2={end_point}")

        if self.shape_type == "Line":
            self.draw_line_bresenham(start_point, end_point)

        if self.shape_type == "Circle":
            center_x = (start_point[0] + end_point[0]) // 2
            center_y = (start_point[1] + end_point[1]) // 2
            radius = int(((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2) ** 0.5) // 2
            self.draw_circle_bresenham((center_x, center_y), radius)

        return self.image
