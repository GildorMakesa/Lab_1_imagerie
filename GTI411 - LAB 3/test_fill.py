import numpy as np
import cv2
import matplotlib.pyplot as plt


import sys
sys.setrecursionlimit(100000)

boundary_color = np.array([255, 0, 0])  # La couleur de la frontière (par exemple, rouge)
fill_color = np.array([0, 255, 255])  # La couleur de remplissage (par exemple, cyan)

image = cv2.imread("C:/Users/Gildor/Desktop/test.png")  # Charger l'image depuis le fichier
if image is None:
    print("Erreur: L'image n'a pas pu être chargée. Vérifie le chemin du fichier.")
    sys.exit()  # Quitter le programme si l'image n'a pas pu être chargée

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convertir l'image de BGR à RGB


def boundary_fill(x, y):
    """Implémente l'algorithme de Boundary Fill pour remplir une région avec la couleur spécifiée."""
    # Vérifier si les coordonnées (x, y) sont dans l'image
    if x < 0 or y < 0 or x >= image.shape[1] or y >= image.shape[0]:
        return  # Si l'on dépasse les limites de l'image, on arrête
    
    # Vérifier si le pixel actuel est déjà de la couleur de la frontière ou de la couleur de remplissage
    if np.array_equal(image[y, x], boundary_color) or np.array_equal(image[y, x], fill_color):
        return  # Arrêter la récursion si le pixel est une frontière ou déjà rempli
    
    # Remplir ce pixel avec la couleur de remplissage
    image[y, x] = fill_color

    # Appeler récursivement les pixels voisins (haut, bas, gauche, droite)
    boundary_fill(x + 1, y)  # Droit
    boundary_fill(x - 1, y)  # Gauche
    boundary_fill(x, y + 1)  # Bas
    boundary_fill(x, y - 1)  # Haut


def main():
    # Afficher l'image originale
    plt.subplot(1, 2, 1)
    plt.title("Forme initiale")
    plt.imshow(image)
    plt.imshow(image)
    
    # Appeler la fonction de remplissage à partir d'un point à l'intérieur de la forme
    boundary_fill(15, 15)  # Choisir un point à l'intérieur de la forme pour commencer le remplissage

    # Afficher le résultat après le remplissage
    plt.subplot(1, 2, 2)
    plt.title("Résultat Finale")
    plt.imshow(image)
    
    plt.show()


if __name__ == "__main__":
    main()
