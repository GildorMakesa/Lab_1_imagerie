import cv2
from PyQt5.QtGui import QPixmap, QImage
import numpy as np


def draw_shape_as_qpixmap(r: int, g: int, b: int, height: int, width: int, shape:str = "circle") -> QPixmap:
    image = np.zeros((height - 2, width - 2, 4), dtype="uint8")
    if shape == "circle":
        # paramètres du cercle
        center_coordinates = (int(width/2), int(height/2))
        radius = int(height/2) - 120 #ne doit pas dépasser min(height, width)/2
        #valeurs initiales des couleurs R G B
        color = (r, g, b, 255) #r g b alpha
        thickness = -1  #remplir la forme géométrique par la couleur
        cv2.circle(image, center_coordinates, radius, color, thickness)
    elif shape == "rectangle":
        start_point = (int(width/2) - 300, int(height/2) - 200) #top left corner
        end_point = (int(width/2) + 300, int(height/2) + 200) #bottom right corner, ne doit pas dépasser (img_width, img_height)
        color = (r, g, b, 255) #r g b alpha
        thickness = 3
        cv2.rectangle(image, start_point, end_point, color, thickness)

    return np_array_to_pixmap(image)



def np_array_to_pixmap(array):
    height, width, channel = array.shape
    # Convertir le tableau en QImage
    if channel == 3:  # Si l'image est en RGB
        qimage = QImage(array.data, width, height, 3 * width, QImage.Format_RGB888)
    elif channel == 4:  # Si l'image est en RGBA
        qimage = QImage(array.data, width, height, 4 * width, QImage.Format.Format_RGBA8888)
    else:
        raise ValueError("Le tableau numpy doit avoir 3 canaux (RGB) ou 4 canaux (RGBA)")

    # Convertir QImage en QPixmap
    qpixmap = QPixmap.fromImage(qimage)
    return qpixmap