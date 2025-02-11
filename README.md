# <p align="center">Laboratoire 2 : Filtrage </p>


### Partie 1 : Filtrage spatial

Le système fournit une interface usager composée de trois onglets. Sous le premier : ’’Spatial Filter’’, 4 paramètres peuvent être spécifiés (voir fig. 1): 

•	Le type du filtre à appliquer ‘’Filter type’’.
•	La taille des noyaux (utilisés par certains filtres)
•	La façon dont les bordures seront traitées ‘’Handling border’’.
•	La façon dont les valeurs filtrées sont converties dans l'intervalle affichable 0..255 ‘’Range’’.

L’interface et la gestion des boutons est déjà codée. Vous avez juste à modifier la fonction « apply_filter » dans le fichier modes/spatial_filter_model.py :

Les variables sont prêtes à être utilisées :
-	Filtering_method : type du filtre
-	Kernel_size: taille du noyau (attention si le champs est vide, le programme peut crash, il faut gérer cette exception)
-	Range_methode : Méthode pour gérer les pixels en dehors de [0 :255]
-	Handling_border_method : Méthode pour gérer les bordures (voir doc OpenCV)

En fonction de la version du code que vous avez, il se peut que vous n’arriviez pas à déclencher le filtre médian. La raison est que la chaîne de caractère est « median  » (avec un espace à la fin), vous pouvez donc modifier votre condition (if etc.) en conséquence

### Résumé de la partie 1 
- Filtre Moyen    🟡
- Filtre Gaussien 🟡
- Filtre Médian   🟡
- Filtre Sobel 
  - Sobel X :     🟡 
  - Sobel Y :     🟡 
  - Combié :      🟡 


# Partie 2 : Décomposition d’une image
Canny est un algorithme à plusieurs étapes, il faut lisser l'image avec un filtre Gaussien, calculer les composantes du gradient avec un filtre Sobel, puis isoler les maximas locaux dans la carte des gradients et appliquer un seuillage hystérésis pour identifier les contours de l'image. Pour vous aider, l’interface du filtre est déjà préparée. 

Ce qui est demandé :
•	Vous devez maitriser l’ajustement des paramètres du filtre (seuils et taille du filtre gaussien) car il vous sera demandé de filtrer de nouvelles images lors de la démonstration, puis de justifier les valeurs des paramètres.
•	Pour l’affichage, on doit retrouver l’image originale, l’image lissée, les composants du gradient, les maxima locaux, les contours résultant de Canny.

Pour cette partie, vous avez uniquement à modifier la fonction « apply_filter » dans models/canny_filter_model.py

### Résumé de la partie 2
- Lissage avec un filtre gaussien         🟡
- Gradient de l’image à l’aide de Sobel   🟡
- Suppression non maximale                🟡
- Résultat final                          🟡





# Partie 3 : Transformation d’image
Dans cette partie, vous testerez les filtres fréquentiels. Le travail demandé :
•	Utilisez l’interface fournie qui permet à l’utilisateur d’entrer la fréquence de coupure de chaque filtre ainsi que le paramètre du profil (n) du filtre Butterworth. À l’affichage, on doit retrouver pour chaque filtre : l’image originale, le spectre original, l’image filtrée, et le spectre de l'image filtrée.
•	Implémenter les deux filtres passe bas idéal et passe bas butterworth.
•	Tester les deux filtres avec différentes valeurs de n. Puis comparer le résultat obtenu avec les deux filtres.
•	Faites le même travail pour les filtres passe haut idéal et passe haut butterworth.

Pour cette partie vous avez 4 filtres à implémenter, donc 4 fonctions à compléter dans models/freq_filter_model.py
Par exemple pour le passe-bas avec butterworth 

### Résumé de la partie 3
- Passe haut et passe bas idéal
- Passe haut et passe bas Butterworth


