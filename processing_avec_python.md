Pour utiliser **Processing** depuis un script Python classique, vous pouvez utiliser une bibliothèque appelée **Processing.py**. Processing.py permet d'intégrer et d'exécuter du code Processing à partir de Python. Voici les étapes pour commencer à utiliser Processing depuis un script Python.

### Étapes pour utiliser Processing avec Python

1. **Installer Processing et Processing.py** :
   - **Télécharger et installer Processing** : Allez sur le site officiel de [Processing](https://processing.org/download/) et téléchargez la version de Processing pour votre système d'exploitation.
   - **Installer Processing.py** : Vous devez installer le mode Python dans l'IDE Processing. Cela se fait directement depuis l'IDE Processing.
     - Ouvrez l'IDE Processing.
     - Allez dans `Tools` -> `Mode` -> et sélectionnez `Python` pour activer le mode Python.

2. **Créer un sketch Python avec Processing** :
   - Ouvrez l'IDE Processing.
   - Allez dans `File` -> `New`, puis changez le mode en `Python` (en bas à droite de l'IDE).
   - Vous pouvez maintenant écrire du code Python avec les fonctions Processing.

3. **Utiliser Processing dans un script Python externe** :
   Si vous souhaitez intégrer Processing dans un script Python classique (en dehors de l'IDE Processing), vous devrez utiliser une méthode différente, car l'IDE de Processing crée un environnement spécial pour cela. Voici une approche simple :

### Utilisation de `pyprocessing` (alternative à Processing.py)

1. **Installer pyprocessing** :
   `pyprocessing` est une bibliothèque qui permet d'exécuter du code Processing depuis un script Python classique.
   
   Vous pouvez installer `pyprocessing` via `pip` :
   ```bash
   pip install pyprocessing
   ```

2. **Exemple de code avec pyprocessing** :
   Une fois que vous avez installé `pyprocessing`, vous pouvez créer un script Python comme suit :

   ```python
   from pyprocessing import *

   # Définir la taille de la fenêtre
   def setup():
       size(400, 400)

   # Dessiner dans la fenêtre
   def draw():
       background(255)
       fill(255, 0, 0)
       ellipse(mouseX, mouseY, 50, 50)

   # Lancer l'application
   run()
   ```

   Ce script crée une fenêtre de 400x400 pixels, et un cercle rouge suit la position de la souris.

### Alternative avec Processing via Jython

Une autre méthode consiste à utiliser **Jython**, qui est une implémentation de Python sur la JVM (Java Virtual Machine). Vous pouvez ainsi utiliser le framework Processing (qui est écrit en Java) à partir de Python via Jython. Toutefois, cette méthode est plus complexe à mettre en place.

### Conclusion

- **Processing.py dans l'IDE Processing** : Il est préférable d'utiliser l'IDE Processing avec le mode Python si vous êtes débutant.
- **pyprocessing** : Si vous préférez un environnement Python standard pour travailler avec Processing, `pyprocessing` est une bonne option.
