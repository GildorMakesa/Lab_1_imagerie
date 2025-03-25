import numpy as np



class TransformationModel:
    width = 1245
    height = 480

    points = np.array([
        [71, 136],  # RIGHT-HIP
        [63, 200],  # RIGHT-KNEE
        [40, 269],  # RIGHT-ANKLE
    ])

    connections = [(0, 1), (1, 2)]

    def __init__(self) -> None:
        self.image = None
        self.base_image_shape = None

        # Translation parameters
        self.trans_x = 0
        self.trans_y = 0

        # Scale parameters
        self.scale_x = 1.0
        self.scale_y = 1.0

        # Shear parameters
        self.shear = 1.0

        # Rotation parameters
        self.rot_angle = 0



    def update_param(self, value, param):
        assert hasattr(self, param)
        setattr(self, param, value)


    def set_image(self, image):
        self.image = np.ones((self.height, self.width, 3), dtype=np.uint8) * np.array([255, 255, 255], dtype=np.uint8)
        h, w, _ = image.shape
        if h >= self.height:
            h = self.height
        if w >= self.width:
            w = self.width
        self.image[:h, :w] = image[:h, :w]
        self.base_image_shape = (h, w)
        image = self.image.copy()
        image = self.draw_points(image, self.points)
        return image


    # TODO
    def draw_points(self, image, points):
        # /!\ Attention à modifier uniquement image et pas self.image!
        return image


    # TODO
    def apply_transformation(self, transformation:str):
        assert transformation in ('translate', 'scale', 'shear', 'rotate')
        if self.image is None:
            return None

        print(f"Applying {transformation}")

        image = self.image.copy() # <- /!\ Modifier image et pas self.image
        points = self.points.copy()
        
        image = self.draw_points(image, points)
        return image
