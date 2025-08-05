# Duel-des-mains
jeu python avec Tkinter

Objectif du projet
Créer un jeu simple “Pierre-Papier-Ciseaux” (appelé ici Duel des mains), où un joueur humain affronte un ordinateur. Le joueur saisit son choix dans une interface graphique réalisée avec Tkinter, et l’ordinateur choisit au hasard.

# Travail réalisé jusqu’à présent
1. Importation des bibliothèques :
tkinter pour créer l’interface graphique.
random pour générer un choix aléatoire pour l’ordinateur.

2. Création de la fenêtre de jeu :
Fenêtre Tkinter initialisée avec le titre “Duel des mains”.
Dimensions de la fenêtre : 400x300
Couleur d’arrière-plan : bleu clair (lightblue).

3. Ajout des éléments graphiques :
Titre du jeu affiché dans la fenêtre avec une police lisible.
Message d’invitation demandant à l’utilisateur de choisir entre pierre, papier ou ciseaux.
Champ de saisie permettant à l’utilisateur d’entrer son choix.

4. Choix aléatoire de l’ordinateur :
Une sélection parmi ["pierre", "papier", "ciseaux"] est faite au hasard à chaque lancement du programme.
Le choix est temporairement affiché dans la console pour test (sera amélioré dans les prochaines étapes).
