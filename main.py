import tkinter as tk
import core.game as game
from save.save_manager import charger, sauvegarder

#charger la sauvegarde au début de la session
game.config.dict_ressource = charger(game.config.dict_ressource)

def actualisation_ressource():
    game.ajouter_ressource()
    label_ressource_actuel.config(text=f"Vous avez {game.config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {game.config.dict_ressource['ressource_total']:.1f} ressource")

def actualiser_prod_machine():
    game.production_machine()
    label_ressource_actuel.config(text=f"Vous avez {game.config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {game.config.dict_ressource['ressource_total']:.1f} ressource")
    fenetre_jeu.after(game.config.dict_ressource['tick-rate'], actualiser_prod_machine)

def actualiser_prod_machinelv2():
    game.production_machinelv2()
    label_ressource_actuel.config(text=f"Vous avez {game.config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {game.config.dict_ressource['ressource_total']:.1f} ressource")
    fenetre_jeu.after(game.config.dict_ressource['tick-rate'], actualiser_prod_machinelv2)

def actualiser_prod_machinelv3():
    game.production_machinelv3()
    label_ressource_actuel.config(text=f"Vous avez {game.config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {game.config.dict_ressource['ressource_total']:.1f} ressource")
    fenetre_jeu.after(game.config.dict_ressource['tick-rate'], actualiser_prod_machinelv3)

def actualiser_prod_machinelv4():
    game.production_machinelv4()
    label_ressource_actuel.config(text=f"Vous avez {game.config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {game.config.dict_ressource['ressource_total']:.1f} ressource")
    fenetre_jeu.after(game.config.dict_ressource['tick-rate'], actualiser_prod_machinelv4)

def actualiser_prod_machinelv5():
    game.production_machinelv5()
    label_ressource_actuel.config(text=f"Vous avez {game.config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {game.config.dict_ressource['ressource_total']:.1f} ressource")
    fenetre_jeu.after(game.config.dict_ressource['tick-rate'], actualiser_prod_machinelv5)

def actualiser_prix_machine():
    game.ajouter_machine()
    label_nb_machine.config(text=f"Stock : {game.config.dict_ressource['machine']}" )
    label_ressource_actuel.config(text=f"Vous avez {game.config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {game.config.dict_ressource['ressource_total']:.1f} ressource")
    cout = game.cout_machine()
    bouton_machine.config(text=f"Machine, coût : {cout:.1f}")

def actualiser_prix_machinelv2():
    game.ajouter_machinelv2()
    label_nb_machinelv2.config(text=f"Stock : {game.config.dict_ressource['machinelv2']}")
    label_ressource_actuel.config(text=f"Vous avez {game.config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {game.config.dict_ressource['ressource_total']:.1f} ressource")
    cout = game.cout_machinelv2()
    bouton_machinelv2.config(text=f"Machinelv2, coût: {cout:.1f}")

def actualiser_prix_machinelv3():
    game.ajouter_machinelv3()
    label_nb_machinelv3.config(text=f"Stock : {game.config.dict_ressource['machinelv3']}")
    label_ressource_actuel.config(text=f"Vous avez {game.config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {game.config.dict_ressource['ressource_total']:.1f} ressource")
    cout = game.cout_machinelv3()
    bouton_machinelv3.config(text=f"Machinelv3, coût: {cout:.1f}")

def actualiser_prix_machinelv4():
    game.ajouter_machinelv4()
    label_nb_machinelv4.config(text=f"Stock : {game.config.dict_ressource['machinelv4']}")
    label_ressource_actuel.config(text=f"Vous avez {game.config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {game.config.dict_ressource['ressource_total']:.1f} ressource")
    cout = game.cout_machinelv4()
    bouton_machinelv4.config(text=f"Machinelv4, coût: {cout:.1f}")

def actualiser_prix_machinelv5():
    game.ajouter_machinelv5()
    label_nb_machinelv5.config(text=f"Stock : {game.config.dict_ressource['machinelv5']}")
    label_ressource_actuel.config(text=f"Vous avez {game.config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {game.config.dict_ressource['ressource_total']:.1f} ressource")
    cout = game.cout_machinelv5()
    bouton_machinelv5.config(text=f"Machinelv5, coût: {cout:.1f}")

fenetre_jeu = tk.Tk()
fenetre_jeu.state('zoomed')
fenetre_jeu.title("Jeu")

#configuration des colonnes
fenetre_jeu.grid_columnconfigure(0, weight=1) #gauche
fenetre_jeu.grid_columnconfigure(1, weight=1) #centre
fenetre_jeu.grid_columnconfigure(2, weight=1) #droite

#haut:production (Au milieu)
label_ressource_actuel = tk.Label(fenetre_jeu, text=f"Vous avez {game.config.dict_ressource['ressource_actuelle']:.1f} ressource", font=("Arial", 25, "bold"))
label_ressource_actuel.grid(row=0, column=1, pady=(10))

label_ressource_total = tk.Label(fenetre_jeu, text=f"Total produit : {game.config.dict_ressource['ressource_total']:.1f}", fg="gray", font=("Arial", 12))
label_ressource_total.grid(row=1, column=1)

bouton_ressource = tk.Button(fenetre_jeu, text="PRODUIRE (+1)", command=actualisation_ressource, bg="lightgreen", width=30, height=2)
bouton_ressource.grid(row=2, column=1, pady=20)

#millieu :machine (À gauche)
# On les met un peu plus haut (row 3 et 4)
cout = game.cout_machine()
bouton_machine = tk.Button(fenetre_jeu, text=f"Machine, coût : {cout:.1f}", command=actualiser_prix_machine, width=25)
bouton_machine.grid(row=3, column=0, pady=10, sticky="e") 

label_nb_machine = tk.Label(fenetre_jeu, text=f"Stock : {game.config.dict_ressource['machine']}", font=("Arial", 10, "bold"))
label_nb_machine.grid(row=3, column=1, sticky="w", padx=10)

cout1 = game.cout_machinelv2()
bouton_machinelv2 = tk.Button(fenetre_jeu, text=f"Machinelv2, coût : {cout1:.1f}", command=actualiser_prix_machinelv2, width=25)
bouton_machinelv2.grid(row=4, column=0, pady=10, sticky="e")

label_nb_machinelv2 = tk.Label(fenetre_jeu, text=f"Stock : {game.config.dict_ressource['machinelv2']}", font=("Arial", 10, "bold"))
label_nb_machinelv2.grid(row=4, column=1, sticky="w", padx=10)

cout2 = game.cout_machinelv3()
bouton_machinelv3 = tk.Button(fenetre_jeu, text=f"Machinelv2, coût : {cout1:.1f}", command=actualiser_prix_machinelv3, width=25)
bouton_machinelv3.grid(row=5, column=0, pady=10, sticky="e")

label_nb_machinelv3 = tk.Label(fenetre_jeu, text=f"Stock : {game.config.dict_ressource['machinelv3']}", font=("Arial", 10, "bold"))
label_nb_machinelv3.grid(row=5, column=1, sticky="w", padx=10)

cout3 = game.cout_machinelv4()
bouton_machinelv4 = tk.Button(fenetre_jeu, text=f"Machinelv2, coût : {cout1:.1f}", command=actualiser_prix_machinelv4, width=25)
bouton_machinelv4.grid(row=6, column=0, pady=10, sticky="e")

label_nb_machinelv4 = tk.Label(fenetre_jeu, text=f"Stock : {game.config.dict_ressource['machinelv4']}", font=("Arial", 10, "bold"))
label_nb_machinelv4.grid(row=6, column=1, sticky="w", padx=10)

cout4 = game.cout_machinelv5()
bouton_machinelv5 = tk.Button(fenetre_jeu, text=f"Machinelv5, coût : {cout1:.1f}", command=actualiser_prix_machinelv5, width=25)
bouton_machinelv5.grid(row=7, column=0, pady=10, sticky="e")

label_nb_machinelv5 = tk.Label(fenetre_jeu, text=f"Stock : {game.config.dict_ressource['machinelv5']}", font=("Arial", 10, "bold"))
label_nb_machinelv5.grid(row=7, column=1, sticky="w", padx=10)

# On crée une ligne vide (row 5) pour placer sauvegarder
fenetre_jeu.grid_rowconfigure(5, weight=1) 

#bas: sauvegarder (À droite)
bouton_sauvegarder = tk.Button(fenetre_jeu, text="SAUVEGARDER LA PARTIE", command=lambda: sauvegarder(game.config.dict_ressource), bg="lightblue", width=30)
bouton_sauvegarder.grid(row=6, column=2, padx=30, pady=30, sticky="se")

actualiser_prod_machine()
actualiser_prod_machinelv2()

fenetre_jeu.mainloop()