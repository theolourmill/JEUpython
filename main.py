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
    label_ressource_actuel.config(text=f"Vous avez {config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {config.dict_ressource['ressource_total']:.1f} ressource")
    cout = cout_machine()
    bouton_machine.config(text=f"Machine, coût : {cout:.1f}")

def actualiser_prix_machinelv2():
    ajouter_machinelv2()
    label_ressource_actuel.config(text=f"Vous avez {config.dict_ressource['ressource_actuelle']:.1f} ressource")
    label_ressource_total.config(text=f"Vous avez produit un total de  {config.dict_ressource['ressource_total']:.1f} ressource")
    cout = cout_machinelv2()
    bouton_machinelv2.config(text=f"Machine, coût : {cout:.1f}")

#Permet a la fenetre de resté ouverte
fenetre_jeu = tk.Tk()
fenetre_jeu.state('zoomed')
fenetre_jeu.title("jeu")
label = tk.Label(fenetre_jeu, text="Bienvenue dans ce jeu")
label.pack()

label_ressource_actuel = tk.Label(fenetre_jeu, text=f"Vous avez {config.dict_ressource['ressource_actuelle']:.1f} ressource")
label_ressource_actuel.pack()

label_ressource_total = tk.Label(fenetre_jeu, text=f"Vous avez produit un total de {config.dict_ressource['ressource_total']:.1f} ressource")
label_ressource_total.pack()

bouton_ressource = tk.Button(text="Produire une ressource", command=actualisation_ressource )
bouton_ressource.pack(pady=10)

cout = cout_machine()
bouton_machine = tk.Button(text=f"Machine, coût : {cout}", command =actualiser_prix_machine)
bouton_machine.pack()

cout1= cout_machinelv2()
bouton_machinelv2 = tk.Button(text=f"Machinelv2, coût : {cout1}", command =actualiser_prix_machinelv2)
bouton_machinelv2.pack()

bouton_sauvegarder = tk.Button(text="Sauvegarder", command= lambda : sauvegarder(config.dict_ressource))
bouton_sauvegarder.pack(pady=10)

actualiser_prod_machine()
actualiser_prod_machinelv2()

fenetre_jeu.mainloop()