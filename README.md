# Lab_1_imagerie
Laboratoire_1_GTI411

# Partie 1 : Conversion entre les espaces de couleur

L’objectif est d’apprendre à manipuler les espaces de couleurs suivants

•	RGB
•	HSV
•	CMYK
•	L.A.B

Interface de départ
Pour cette partie vous devrez ajouter une forme à l’aide de l’interface fournie (Figure 1). Vous pourrez ensuite changer la couleur en appuyant sur le bouton « Color ». A ce moment, une fenêtre supplémentaire s’ouvrira (Figure 2). A partir de celle-ci vous pourrez changer la couleur en glissant les curseurs. 

Consignes
Dans l’exemple, le format RGB est implémenté. Vous devrez faire de même pour HSV, CMYK et L.A.B. Pour chacun de ces formats de devrez :
1.	Afficher correctement la palette de couleur à l’arrière : Exemple (Figure 2) pour le rouge la palette va du noir au rouge. Pour savoir à quoi doivent ressembler les palettes, vous pouvez vous aider du site : https://www.w3schools.com/colors/colors_rgb.asp
2.	Choisir la bonne plage de valeur pour chaque curseur (ex : rouge du RGB : [0 : 255])
3.	Convertir la valeur reçue en RGB et placer les curseurs au bon endroit dans l’espace de couleur
4.	Convertir la couleur dans l’espace de couleur actuel (CMYK, HSV ou lab) vers RGB pour l’afficher dans la fonction _sliders_to_rgb de chaque curseur

Pour chaque slider à modifier, un fichier a été créé dans le dossier Lab1/views/components, vous devrez donc modifier les fichiers cmyk_slider.py, hsv_slider.py et lab_slider.py. Afin de séparer l’interface graphique et la partie « logique » du code, les fonctions de conversion d’espace de couleur seront placées dans le fichier Lab1/models/color_conversion.py. Pour implémenter les différents curseurs, aidez-vous du curseur RGB fourni et déjà implémenté. Des commentaires avec écrit « TODO » vous indiquerons les endroits à modifier.

Pour cette partie vous devez implémenter les conversions vous-même à partir des formules du cours, sans utiliser OpenCV (ou équivalent).

- ## Résumé Partie 1
- ✅ RGB
- ✅ HSV
- ✅ CMYK
- 🟡L.A.B (En cours)



# Partie 2 : Décomposition d’une image
Dans cette partie vous devrez charger une image (Menu > Add > Image) puis la décomposer en ces différents canaux (Il est conseillé d’utiliser l’image cube.jpg). Par exemple pour le format R.G.B, on a trois canaux (Rouge, Vert et Bleu), ainsi on souhaite les afficher de façon séparés (Figure 3). 
Pour cela vous devrez modifier les fonctions présentent dans le fichier Lab1/models/decomposition.py (voir les « TODO »). Pour cette partie vous pouvez utiliser les fonctions de conversion d’OpenCV au besoin. Les canaux devront être affichés avec leur couleur respectives (exemple le rouge de RGB en niveau de rouge ou le Cyan de CMYK en niveau de cyan).


- ## Résumé Partie 2
- ✅ RGB
- ✅ HSV
- ✅ CMYK
- 🟡L.A.B (En cours)


# Partie 3 : Transformation d’image
Pour cette partie, vous devrez implémentation la logique (Lab1/model/transform.py) pour pouvoir modifier le contraste et la luminosité de l’image lorsque l’on bouge les curseurs.

- ## Résumé Partie 3
- 🟡(En cours)