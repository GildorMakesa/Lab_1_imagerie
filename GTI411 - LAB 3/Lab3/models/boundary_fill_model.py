import numpy as np

import sys
sys.setrecursionlimit(100000)



class BoundaryFillModel:
    def __init__(self) -> None:
        self.fill_color = np.array([255, 0, 0])
        self.boundary_color = np.array([255, 0, 0])
        self.image = None

    

    def boundary_fill(self, image, x, y):
        self.image = image
        try:
            self.fill(x, y)
        except RecursionError:
            print("Maximum recursion reached, skipping flooding")
        return self.image
    
    
    # TODO 
    # A implémenter manuellement
    def fill(self, x, y):
        pass
    

    def set_fill_color(self, color):
        self.fill_color = np.array(color)


    def set_boundary_color(self, color):
        self.boundary_color = np.array(color)