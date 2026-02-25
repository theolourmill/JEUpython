import tkinter as tk
from core.game import ajouter_ressource, production_machine,ajouter_machine, cout_machine, production_machinelv2, ajouter_machinelv2, cout_machinelv2
import config
from save.save_manager import charger, sauvegarder

#charger la sauvegarde au début de la session
config.dict_ressource = charger(config.dict_ressource)

def actualisation_ressource():
    ajouter_ressource()
    label_ressource_actuel.config(text=f"Vous avez {config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {config.dict_ressource['ressource_total']:.1f} ressource")

def actualiser_prod_machine():
    production_machine()
    label_ressource_actuel.config(text=f"Vous avez {config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {config.dict_ressource['ressource_total']:.1f} ressource")
    fenetre_jeu.after(config.dict_ressource['tick-rate'], actualiser_prod_machine)

def actualiser_prod_machinelv2():
    production_machinelv2()
    label_ressource_actuel.config(text=f"Vous avez {config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {config.dict_ressource['ressource_total']:.1f} ressource")
    fenetre_jeu.after(config.dict_ressource['tick-rate'], actualiser_prod_machinelv2)

def actualiser_prix_machine():
    ajouter_machine()
    label_nb_machine.config(text=f"Stock : {config.dict_ressource['machine']}" )
    label_ressource_actuel.config(text=f"Vous avez {config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {config.dict_ressource['ressource_total']:.1f} ressource")
    cout = cout_machine()
    bouton_machine.config(text=f"Machine, coût : {cout:.1f}")

def actualiser_prix_machinelv2():
    ajouter_machinelv2()
    label_nb_machinelv2.config(text=f"Stock : {config.dict_ressource['machinelv2']}")
    label_ressource_actuel.config(text=f"Vous avez {config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {config.dict_ressource['ressource_total']:.1f} ressource")
    cout = cout_machinelv2()
    bouton_machinelv2.config(text=f"Machinelv2, coût: {cout:.1f}")

fenetre_jeu = tk.Tk()
fenetre_jeu.state('zoomed')
fenetre_jeu.title("Jeu")

#configuration des colonnes
fenetre_jeu.grid_columnconfigure(0, weight=1) #gauche
fenetre_jeu.grid_columnconfigure(1, weight=1) #centre
fenetre_jeu.grid_columnconfigure(2, weight=1) #droite

#haut:production (Au milieu)
label_ressource_actuel = tk.Label(fenetre_jeu, text=f"Vous avez {config.dict_ressource['ressource_actuelle']:.1f} ressource", font=("Arial", 25, "bold"))
label_ressource_actuel.grid(row=0, column=1, pady=(10))

label_ressource_total = tk.Label(fenetre_jeu, text=f"Total produit : {config.dict_ressource['ressource_total']:.1f}", fg="gray", font=("Arial", 12))
label_ressource_total.grid(row=1, column=1)

bouton_ressource = tk.Button(fenetre_jeu, text="PRODUIRE (+1)", command=actualisation_ressource, bg="lightgreen", width=30, height=2)
bouton_ressource.grid(row=2, column=1, pady=20)

#millieu :machine (À gauche)
# On les met un peu plus haut (row 3 et 4)
cout = cout_machine()
bouton_machine = tk.Button(fenetre_jeu, text=f"Machine, coût : {cout:.1f}", command=actualiser_prix_machine, width=25)
bouton_machine.grid(row=3, column=0, pady=10, sticky="e") 

label_nb_machine = tk.Label(fenetre_jeu, text=f"Stock : {config.dict_ressource['machine']}", font=("Arial", 10, "bold"))
label_nb_machine.grid(row=3, column=1, sticky="w", padx=10)

cout1 = cout_machinelv2()
bouton_machinelv2 = tk.Button(fenetre_jeu, text=f"Machinelv2, coût : {cout1:.1f}", command=actualiser_prix_machinelv2, width=25)
bouton_machinelv2.grid(row=4, column=0, pady=10, sticky="e")

label_nb_machinelv2 = tk.Label(fenetre_jeu, text=f"Stock : {config.dict_ressource['machinelv2']}", font=("Arial", 10, "bold"))
label_nb_machinelv2.grid(row=4, column=1, sticky="w", padx=10)

# On crée une ligne vide (row 5) pour placer sauvegarder
fenetre_jeu.grid_rowconfigure(5, weight=1) 

#bas: sauvegarder (À droite)
bouton_sauvegarder = tk.Button(fenetre_jeu, text="SAUVEGARDER LA PARTIE", command=lambda: sauvegarder(config.dict_ressource), bg="lightblue", width=30)
bouton_sauvegarder.grid(row=6, column=2, padx=30, pady=30, sticky="se")

actualiser_prod_machine()
actualiser_prod_machinelv2()

fenetre_jeu.mainloop()