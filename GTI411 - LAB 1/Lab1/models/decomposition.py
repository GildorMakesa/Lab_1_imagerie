import numpy as np
import matplotlib.pyplot as plt


class Lab1DecompositionModel:
    def __init__(self) -> None:
        self.color_space: str = "rgb"
        self.image: np.ndarray = None

    
    def set_color_space(self, space:str):
        self.color_space = space


    def set_image(self, image):
        self.image = image


    def _decompose_rgb(self):
        # TODO
        if self.image is None:
            return
        fig = plt.figure()
        plt.subplot(2, 3, 1)
        plt.imshow(self.image)
        plt.title("Base")

        channels = ["red", "green", "blue"]
        for idx, c in enumerate(channels):
            plt.subplot(2, 3, 4+idx)
            plt.title(c)
            im = plt.imshow(self.image[:, :, idx], cmap="gray")
            plt.colorbar(im)

        plt.tight_layout()
        plt.show()


    def _decompose_cmyk(self):
        if self.image is None:
            return
        #TODO


    def _decompose_lab(self):
        if self.image is None:
            return
        #TODO


    def _decompose_hsv(self):
        if self.image is None:
            return
        #TODO


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
        
    
