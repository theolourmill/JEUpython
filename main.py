import tkinter as tk
from core.game import ajouter_ressource, production_machine,ajouter_machine, cout_machine
import config
def actualisation_ressource():
    ajouter_ressource()
    label_ressource_actuel.config(text=f"Vous avez {config.dict_ressource['ressource_actuelle']} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {config.dict_ressource['ressource_total']} ressource")

def actualiser_prod_machine():
    production_machine()
    label_ressource_actuel.config(text=f"Vous avez {config.dict_ressource['ressource_actuelle']} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {config.dict_ressource['ressource_total']} ressource")
    fenetre_jeu.after(100, actualiser_prod_machine)

def actualiser_prix_machine():
    ajouter_machine()
    label_ressource_actuel.config(text=f"Vous avez {config.dict_ressource['ressource_actuelle']} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {config.dict_ressource['ressource_total']} ressource")
    cout= cout_machine()
    bouton_machine.config(text="Acheter, cout: {cout} ressources)")


fenetre_jeu = tk.Tk()
fenetre_jeu.state('zoomed')
fenetre_jeu.title("jeu")
label = tk.Label(fenetre_jeu, text="Bienvenue dans ce jeu")
label.pack()

label_ressource_actuel = tk.Label(fenetre_jeu, text=f"Vous avez {config.dict_ressource['ressource_actuelle']} ressource")
label_ressource_actuel.pack()

label_ressource_total = tk.Label(fenetre_jeu, text="Vous avez produit un total de 0 ressource")
label_ressource_total.pack()

bouton_ressource = tk.Button(text="Produire une ressource", command=actualisation_ressource )
bouton_ressource.pack(pady=10)

bouton_machine = tk.Button(text="acheter une machine (cout :10)", command =actualiser_prix_machine)
bouton_machine.pack()
actualiser_prod_machine()
fenetre_jeu.mainloop()