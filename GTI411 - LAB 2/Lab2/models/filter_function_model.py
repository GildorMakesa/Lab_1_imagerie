import cv2 
import numpy as np

class FilterFunction():
     
    def __init__(self,filtering_method, kernel_size, handling_border_method, range_method):
        # L'attribut kernel_size est défini lors de l'initialisation de l'objet
        self.filtering_method = filtering_method
        self.kernel_size = kernel_size  # Définit l'attribut kernel_size
        self.handling_border_method = handling_border_method
        self.range_method = range_method

    def apply_sobel_x(self, image):
            # Vérifie que le kernel est bien un entier impair incluant le 0
            if (self.kernel_size == 0):
                update_ksize = 0
            else:    
                update_ksize = max(0, self.kernel_size | 1)  # Assure que c'est impair et ≥ 3



            if self.handling_border_method == "Copy":
                update_border_type = cv2.BORDER_REPLICATE
            elif self.handling_border_method == "Circular":
                update_border_type = cv2.BORDER_WRAP 
            elif self.handling_border_method == "Mirror":
                update_border_type = cv2.BORDER_REFLECT
            elif self.handling_border_method == "None":
                update_border_type = cv2.BORDER_CONSTANT
            else:
                update_border_type = cv2.BORDER_DEFAULT

           

            grad_x = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=update_ksize, borderType=update_border_type)
            
            if self.range_method == "Abs and normalize to 255":
             sobel_image = np.abs(grad_x)
             sobel_image = cv2.normalize(sobel_image, None, 0, 255, cv2.NORM_MINMAX)
        
            elif self.range_method == "Abs and normalize 0 to 255":
             sobel_image = np.abs(grad_x)
             sobel_image = np.clip(sobel_image, None, 0, 255, cv2.NORM_MINMAX)
            
            elif self.range_method == "Normalize 0 to 255":
             sobel_image = cv2.normalize(grad_x, 0, 255).astype(np.uint8)
            
            elif self.range_method == "Clamp 0 ... 255":
             sobel_image = np.clip(grad_x, 0, 255).astype(np.uint8)


            sobel_image = np.clip(grad_x, 0, 255).astype(np.uint8)
            print("Filtre Sobel applique")
            return sobel_image

    def apply_sobel_y(self, image):
            # Vérifie que le kernel est bien un entier impair incluant le 0
            if (self.kernel_size == 0):
                update_ksize = 0
            else:    
                update_ksize = max(0, self.kernel_size | 1)  # Assure que c'est impair et ≥ 3



            if self.handling_border_method == "Copy":
                update_border_type = cv2.BORDER_REPLICATE
            elif self.handling_border_method == "Circular":
                update_border_type = cv2.BORDER_WRAP 
            elif self.handling_border_method == "Mirror":
                update_border_type = cv2.BORDER_REFLECT
            elif self.handling_border_method == "None":
                update_border_type = cv2.BORDER_CONSTANT
            else:
                update_border_type = cv2.BORDER_DEFAULT

           

            grad_y = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=update_ksize, borderType=update_border_type)
            
            
            if self.range_method == "Abs and normalize to 255":
             sobel_image = np.abs(grad_y)
             sobel_image = cv2.normalize(sobel_image, None, 0, 255, cv2.NORM_MINMAX)
        
            elif self.range_method == "Abs and normalize 0 to 255":
             sobel_image = np.abs(grad_y)
             sobel_image = np.clip(sobel_image, None, 0, 255, cv2.NORM_MINMAX)
            
            elif self.range_method == "Normalize 0 to 255":
             sobel_image = cv2.normalize(grad_y, 0, 255).astype(np.uint8)
            
            elif self.range_method == "Clamp 0 ... 255":
             sobel_image = np.clip(grad_y, 0, 255).astype(np.uint8)


            sobel_image = np.clip(grad_y, 0, 255).astype(np.uint8)
            print("Filtre Sobel applique")
            return sobel_image


    def apply_sobel(self, image):
            # Vérifie que le kernel est bien un entier impair incluant le 0
            if (self.kernel_size == 0):
                update_ksize = 0
            else:    
                update_ksize = max(0, self.kernel_size | 1)  # Assure que c'est impair et ≥ 3



            if self.handling_border_method == "Copy":
                update_border_type = cv2.BORDER_REPLICATE
            elif self.handling_border_method == "Circular":
                update_border_type = cv2.BORDER_WRAP 
            elif self.handling_border_method == "Mirror":
                update_border_type = cv2.BORDER_REFLECT
            elif self.handling_border_method == "None":
                update_border_type = cv2.BORDER_CONSTANT
            else:
                update_border_type = cv2.BORDER_DEFAULT

           

            grad_x = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=update_ksize, borderType=update_border_type)
            grad_y = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=update_ksize, borderType=update_border_type)
            magnitide_sobel_image = cv2.magnitude(grad_x, grad_y)
            
            if self.range_method == "Abs and normalize to 255":
             sobel_image = np.absdiff(magnitide_sobel_image)
             sobel_image = cv2.normalize(magnitide_sobel_image, None, 0, 255, cv2.NORM_MINMAX)
        
            elif self.range_method == "Abs and normalize 0 to 255":
             sobel_image = np.abs(magnitide_sobel_image)
             sobel_image = np.clip(magnitide_sobel_image, None, 0, 255, cv2.NORM_MINMAX)
            
            elif self.range_method == "Normalize 0 to 255":
             sobel_image = cv2.normalize(magnitide_sobel_image, 0, 255).astype(np.uint8)
            
            elif self.range_method == "Clamp 0 ... 255":
             sobel_image = np.clip(magnitide_sobel_image, 0, 255).astype(np.uint8)


            sobel_image = np.clip(magnitide_sobel_image, 0, 255).astype(np.uint8)
            print("Filtre Sobel applique")
            return sobel_image
        
    def apply_gaussian(self, image):
        if self.kernel_size <= 0 or self.kernel_size % 2 == 0:
        # Si ce n'est pas valide, utilise une taille de noyau par défaut, par exemple 3
            print("Kernel size is invalid, using default kernel size + 1.")
            self.kernel_size +=1  # Valeur par défaut

        gaussian_image = cv2.GaussianBlur(image, (self.kernel_size, self.kernel_size), 0)
        print("Gaussian filter applied.")
        return gaussian_image

    def apply_median(self, image):
        median_image = cv2.medianBlur(image, self.kernel_size)
        print("Median filter applied.")
        return median_image



"""
1. Handling Border Method :
Dans OpenCV, la gestion des bordures est importante lorsqu'on applique des filtres, car l'image peut perdre des informations aux bords où la taille du noyau dépasse les dimensions de l'image. Les méthodes de gestion des bordures définissent comment les pixels en dehors de l'image sont traités.

Voici les options que tu mentionnes :

0 (ou cv2.BORDER_DEFAULT) : Cela correspond à cv2.BORDER_DEFAULT qui est la méthode standard dans OpenCV, qui applique par défaut une gestion des bords en utilisant la réplication des bords voisins. Cela signifie que les pixels aux bords de l'image sont dupliqués pour remplir les zones où l'image ne peut pas être utilisée (au niveau des bords).

Copy (ou cv2.BORDER_REPLICATE) : Avec cette méthode, les pixels aux bords de l'image sont copiés pour remplir les espaces hors de l'image. Par exemple, si l'image a un bord avec une couleur claire, cette couleur sera utilisée pour les pixels voisins hors image.

Circular (ou cv2.BORDER_WRAP) : Cela signifie que les pixels à l'extérieur de l'image sont calculés comme si l'image se répétait en boucle, comme si l'image était "pliée" sur elle-même. Par exemple, si un filtre essaie d'accéder à un pixel à gauche de l'image, il va "boucler" à partir du côté droit de l'image.

Miroir (ou cv2.BORDER_REFLECT) : Cela signifie que les pixels aux bords sont réfléchis par rapport à l'image. Par exemple, pour un pixel en dehors de l'image à gauche, l'image le "miroir" en utilisant le pixel le plus proche de l'intérieur. Cela crée une symétrie des bords.
"""