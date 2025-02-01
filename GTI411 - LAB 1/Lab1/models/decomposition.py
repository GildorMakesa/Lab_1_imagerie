import numpy as np
import matplotlib.pyplot as plt
import cv2

from Lab1.models.color_conversion import *

class Lab1DecompositionModel:
    def __init__(self) -> None:
        self.color_space: str = "rgb"
        self.image: np.ndarray = None

    
    def set_color_space(self, space:str):
        self.color_space = space


    def set_image(self, image):
        self.image = image


    def _decompose_rgb(self):
        if self.image is None:
            return
        fig = plt.figure()
        plt.subplot(2, 3, 1)
        plt.imshow(self.image)
        plt.title("Base")

        channels = ["Reds", "Greens", "Blues"]
        for idx, c in enumerate(channels):
            plt.subplot(2, 3, 4+idx)
            plt.title(c)

            im = plt.imshow(self.image[:, :, idx], cmap=c)
            plt.colorbar(im)

        plt.tight_layout()
        plt.show()


    def _decompose_cmyk(self):
        if self.image is None:
            return

        height, width, _ = self.image.shape
        cmyk_image = np.zeros((height, width, 4))

        for i in range(height):
            for j in range(width):
                r, g, b = self.image[i, j]
                cmyk_image[i, j] = rgb_2_cmyk(r, g, b)

        fig = plt.figure()

        plt.subplot(2, 4, 1)
        plt.imshow(self.image)
        plt.title("Base")

        channel_names = ["Cyan", "Magenta", "Yellow", "Black"]
        colormaps = ["GnBu", "RdPu", "YlOrRd", "gray"]

        for idx, (name, cmap) in enumerate(zip(channel_names, colormaps)):
            plt.subplot(2, 4, 4 + idx)
            plt.title(name)

            im = plt.imshow(cmyk_image[:, :, idx], cmap=cmap)
            plt.colorbar(im)

        plt.tight_layout()
        plt.show()



    def _decompose_lab(self):
        if self.image is None:
            return 
        
        height, width, _ = self.image.shape
        lab_image = np.zeros((height, width, 3))

        for i in range(height):
            for j in range(width):
                r, g, b = self.image[i, j]
                lab_image[i, j] = rgb_2_lab(r, g, b)

        fig = plt.figure()

        plt.subplot(2, 4, 1)
        plt.imshow(self.image)
        plt.title("Base")

        channel_names = ["Luminance", "Green-Red", "Blue-Yellow"]
        colormaps = ["gray", "PiYG", "BrBG"]

        for idx, (name, cmap) in enumerate(zip(channel_names, colormaps)):
            plt.subplot(2, 4, 4 + idx)
            plt.title(name)
            
            im = plt.imshow(lab_image[:, :, idx], cmap=cmap)
            plt.colorbar(im)

        plt.tight_layout()
        plt.show()


    def _decompose_hsv(self):
        if self.image is None:
            return

        height, width, _ = self.image.shape
        hsv_image = np.zeros((height, width, 3))

        for i in range(height):
            for j in range(width):
                r, g, b = self.image[i, j]
                hsv_image[i, j] = rgb_2_hsv(r, g, b)

        fig = plt.figure()

        plt.subplot(2, 4, 1)
        plt.imshow(self.image)
        plt.title("Base")

        channel_names = ["Hue", "Saturation", "Value"]
        colormaps = ["hsv", "viridis", "gray"]

        for idx, (name, cmap) in enumerate(zip(channel_names, colormaps)):
            plt.subplot(2, 4, 4 + idx)
            plt.title(name)

            im = plt.imshow(hsv_image[:, :, idx], cmap=cmap)
            plt.colorbar(im)

        plt.tight_layout()
        plt.show()


    def decompose_image(self):
        if self.color_space == "rgb":
            self._decompose_rgb()

        elif self.color_space == "hsv":
            self._decompose_hsv()

        elif self.color_space == "cmyk":
            self._decompose_cmyk()

        elif self.color_space == "lab":
            self._decompose_lab()

        else:
            raise NotImplementedError(f"{self.color_space} is not implemented")
        
    
