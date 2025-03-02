import numpy as np
import cv2
import matplotlib.pyplot as plt

import sys
sys.setrecursionlimit(100000)



boundary_color = np.array([255, 0, 0])
# boundary_color = [0, 0, 0]
fill_color = np.array([0, 255, 255])

image = cv2.imread("images/test.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)



# TODO: IMPLEMENTER CETTE FONCTION
def boundary_fill(x, y):
    return


def main():
    plt.subplot(1, 2, 1)
    plt.title("Forme initiale")
    plt.imshow(image)
    boundary_fill(15, 15)
    # boundary_fill(559, 258)
    plt.subplot(1, 2, 2)
    plt.title("Résultat attendu")
    plt.imshow(image)
    plt.show()
    



if __name__ == "__main__":
    main()