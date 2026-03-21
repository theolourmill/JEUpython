import sys
import os
import time
# Ajoute le dossier parent au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
#pour pouvoir parcourir les machines dans une boucle
suffixes = ["", "lv2", "lv3", "lv4", "lv5"]

def ajouter_ressource():
    config.dict_ressource['ressource_actuelle']+=config.dict_ressource['puissance_clic_total']
    config.dict_ressource['ressource_total']+=config.dict_ressource['puissance_clic_total']
    config.dict_ressource['nombre_clic_total']+=1

def ajouter_machine(niveau):
    d = config.dict_ressource
    s = suffixes[niveau - 1]
    cout = cout_machine(niveau)
    if d['ressource_actuelle'] >= cout:
        d[f"machine{s}"] += 1  
        d['ressource_actuelle'] -= cout

def cout_machine(niveau):
    d = config.dict_ressource
    s = suffixes[niveau - 1]
    coef = f"multiplicateur_cout_machine{s}"
    nb_machine = f"machine{s}"
    cout_base = f"cout-base-machine{s}" 
    cout = d[cout_base] * d[coef] ** d[nb_machine]
    return cout

def cout_clic():
    d = config.dict_ressource
    cout = d['cout_base_puissance_clic']*d['nombre_amélioration_du_clic']**d['multiplicateur_prix_puissance_clic']
    return cout

def ajouter_clic():
    d = config.dict_ressource
    cout = cout_clic()
    if d['ressource_actuelle'] >= cout:
        d['nombre_amélioration_du_clic']+=1
        d['puissance_clic_total']*=d['multiplicateur_du_clic']
        d['ressource_actuelle'] -= cout

def production_machine():
    prod_totale=0
    d=config.dict_ressource
    for s in suffixes:
        nom_prod = f"prod_base_machine{s}"
        nom_qty = f"machine{s}"
        prod_totale += d[nom_prod] * d[nom_qty]
    d['ressource_actuelle'] += prod_totale
    d['ressource_total'] += prod_totale

def compteur_temps_de_jeu():
        config.dict_ressource['temps_de_jeu'] += 1