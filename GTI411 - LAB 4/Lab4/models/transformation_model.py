import numpy as np
import cv2


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
        current_type = type(getattr(self, param))
        setattr(self, param, current_type(value))



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
        for (x, y) in points:
            cv2.circle(image, (int(x), int(y)), radius=5, color=(0, 0, 255), thickness=-1)

        for (start_idx, end_idx) in self.connections:
            pt1 = tuple(points[start_idx])
            pt2 = tuple(points[end_idx])
            cv2.line(image, (int(pt1[0]), int(pt1[1])), (int(pt2[0]), int(pt2[1])), color=(0, 255, 0), thickness=2)

        return image


    # TODO
    def apply_transformation(self, transformation: str):
        assert transformation in ('translate', 'scale', 'shear', 'rotate')
        if self.image is None:
            return None

        print(f"Applying {transformation}")
        image = self.image.copy()
        points = self.points.copy()

        if transformation == 'translate':
            M, points = self.translate_img(points)
        elif transformation == 'scale':
            M, points = self.scale_img(points)
        elif transformation == 'shear':
            M, points = self.shear_img(points)
        elif transformation == 'rotate':
            return self.rotate_img(image, points) #Retourne directement l'image comme on la place au milieux de l'écran contrairement aux autres fonctions
            
        transformed_image = cv2.warpAffine(image, M, (self.width, self.height), flags=cv2.INTER_LINEAR, borderValue=(255, 255, 255))
        transformed_image = self.draw_points(transformed_image, points)

        return transformed_image

    def translate_img(self, points):
        M = np.array([
            [1, 0, self.trans_x],
            [0, 1, self.trans_y]
        ], dtype=np.float32)
        return M, points + np.array([self.trans_x, self.trans_y])
    

    def scale_img(self, points):
        M = np.array([
            [self.scale_x, 0, 0],
            [0, self.scale_y, 0]
        ], dtype=np.float32)
        return M, points * np.array([self.scale_x, self.scale_y])
    
    def shear_img(self, points):
        M = np.array([
            [1, self.shear, 0],
            [0, 1, 0]
        ], dtype=np.float32)

        ones = np.ones((points.shape[0], 1))
        points_h = np.hstack([points, ones])
        sheared_points = np.dot(points_h, M.T)

        return M, sheared_points
    

    def rotate_img(self, image, points):
        h, w = self.base_image_shape
        cx, cy = self.width // 2, self.height // 2 #centering
        
        M_center = np.array([
            [1, 0, cx - w//2],
            [0, 1, cy - h//2]
        ], dtype=np.float32)
        
        centered_image = cv2.warpAffine(image, M_center, (self.width, self.height), borderValue=(255, 255, 255))
        M_rotate = cv2.getRotationMatrix2D((cx, cy), self.rot_angle, 1.0)
        transformed_image = cv2.warpAffine(centered_image, M_rotate, (self.width, self.height), borderValue=(255, 255, 255))
        centered_points = self.points.copy() + np.array([cx - w//2, cy - h//2])
  
        ones = np.ones((centered_points.shape[0], 1))
        points_h = np.hstack([centered_points, ones])
        points = np.dot(points_h, M_rotate.T)
        
        transformed_image = self.draw_points(transformed_image, points)
        return transformed_image