Pour installer **Processing** sur Linux, vous pouvez suivre ces étapes :

### 1. Télécharger Processing
1. Rendez-vous sur le site officiel de Processing : [https://processing.org/download](https://processing.org/download).
2. Téléchargez la version Linux appropriée (généralement pour 64 bits).

### 2. Extraire l'archive
1. Ouvrez un terminal.
2. Naviguez jusqu'au répertoire où se trouve l'archive téléchargée :
   ```bash
   cd ~/Téléchargements
   ```
3. Décompressez l'archive :
   ```bash
   tar -xvzf processing-X.X-linux64.tgz
   ```
   (Remplacez `X.X` par la version que vous avez téléchargée.)

### 3. Déplacer Processing dans un répertoire système (optionnel)
Pour rendre Processing accessible depuis n'importe où, vous pouvez le déplacer dans un répertoire système, comme `/opt` :
   ```bash
   sudo mv processing-X.X /opt/processing
   ```

### 4. Ajouter Processing au PATH (optionnel)
Pour exécuter Processing directement depuis le terminal :
1. Éditez votre fichier `~/.bashrc` ou `~/.zshrc` (selon le shell que vous utilisez) :
   ```bash
   nano ~/.bashrc
   ```
2. Ajoutez la ligne suivante :
   ```bash
   export PATH=$PATH:/opt/processing
   ```
3. Rechargez le fichier de configuration du shell :
   ```bash
   source ~/.bashrc
   ```

### 5. Lancer Processing
Vous pouvez lancer Processing avec :
```bash
/opt/processing/processing
```
Ou, si vous avez ajouté Processing au PATH :
```bash
processing
```

### 6. Créer un raccourci (optionnel)
Pour un accès plus pratique :
1. Créez un fichier desktop dans `~/.local/share/applications/` :
   ```bash
   nano ~/.local/share/applications/processing.desktop
   ```
2. Ajoutez-y le contenu suivant :
   ```plaintext
   [Desktop Entry]
   Name=Processing
   Exec=/opt/processing/processing
   Icon=/opt/processing/lib/icons/pde-256.png
   Type=Application
   Categories=Development;
   ```
3. Sauvegardez et fermez. Processing apparaîtra maintenant dans votre menu d'applications.

### Dépendances éventuelles
Si vous rencontrez des erreurs, il peut être nécessaire d'installer Java :
```bash
sudo apt install openjdk-17-jre
```
(Remplacez `openjdk-17` par la version recommandée par Processing, si nécessaire.)

Avec ces étapes, Processing devrait être installé et fonctionnel sur votre système Linux ! 🚀