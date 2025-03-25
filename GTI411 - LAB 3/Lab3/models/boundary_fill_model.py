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
    
    
    
    def fill(self, x, y):
        
        """Implémente l'algorithme Boundary Fill en utilisant la récursion."""

        # Vérifier si les coordonnées (x, y) sont dans l'image
        if x < 0 or y < 0 or x >= self.image.shape[1] or y >= self.image.shape[0]:
            return  # Si l'on dépasse les limites de l'image, on arrête
        
        # Vérifier si le pixel actuel est déjà de la couleur de la frontière ou de la couleur de remplissage
        # Comparer pixel à pixel avec les couleurs de la frontière et de remplissage
        if np.array_equal(self.image[y, x], self.boundary_color) or np.array_equal(self.image[y, x], self.fill_color):
            return  # Arrêter la récursion si le pixel est une frontière ou déjà rempli
        
        # Remplir ce pixel avec la couleur de remplissage
        self.image[y, x] = self.fill_color

        # Appeler récursivement les pixels voisins (haut, bas, gauche, droite)
        self.fill(x + 1, y)  # Droit
        self.fill(x - 1, y)  # Gauche
        self.fill(x, y + 1)  # Bas
        self.fill(x, y - 1)  # Haut

    def set_fill_color(self, color):
        self.fill_color = np.array(color)


    def set_boundary_color(self, color):
        self.boundary_color = np.array(color)