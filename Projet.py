import tkinter as tk
import random

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Duel des mains") 
fenetre.geometry("400x300")
fenetre.config(bg="lightblue")

# Titre du jeu 
titre = tk.Label(fenetre, text="Duel des mains", font=("Helvetica", 16, "bold"), bg="lightblue")
titre.pack(pady=10)

# Instruction à l'utilisateur
invite = tk.Label(fenetre, text="Choisissez : pierre, papier ou ciseaux", font=("Helvetica", 12), bg="lightblue")
invite.pack(pady=5)

# Champ de saisie
entree_utilisateur = tk.Entry(fenetre, font=("Helvetica", 12))
entree_utilisateur.pack(pady=5)

# Choix aléatoire de l'ordinateur
options = ["pierre", "papier", "ciseaux"]
comp_pick = random.choice(options)

# Affichage temporaire pour vérification
print("Choix de l'ordinateur :", comp_pick)

fenetre.mainloop()
