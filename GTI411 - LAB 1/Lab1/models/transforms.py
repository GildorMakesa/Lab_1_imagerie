

class Lab1ImageTransformsModel:
    
    def __init__(self) -> None:
        self.luminosity = 0
        self.contrast = 1
        self.image = None


    def set_image(self, image):
        self.image = image


    def transform_image(self, contrast, luminosity):
        # TODO
        return self.image