import sys
import os
# Ajoute le dossier parent au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
#pour pouvoir parcourir les machines dans une boucle
suffixes = ["", "lv2", "lv3", "lv4", "lv5"]

def ajouter_ressource():
    config.dict_ressource['ressource_actuelle']+=1
    config.dict_ressource['ressource_total']+=1

def ajouter_machine(niveau):
    d = config.dict_ressource
    s = suffixes[niveau - 1]
    cout = cout_machine(niveau)
    if d['ressource_actuelle'] >= cout:
        d[f"machine{s}"] += 1  # ← corrigé
        d['ressource_actuelle'] -= cout

def cout_machine(niveau):
    d = config.dict_ressource
    s = suffixes[niveau - 1]
    coef = f"multiplicateur_cout_machine{s}"
    nb_machine = f"machine{s}"
    cout_base = f"cout-base-machine{s}"  # tirets OK, ça correspond à config
    cout = d[cout_base] * d[coef] ** d[nb_machine]
    return cout

def production_machine():
    prod_totale=0
    d=config.dict_ressource
    for s in suffixes:
        nom_prod = f"prod_base_machine{s}"
        nom_qty = f"machine{s}"
        prod_totale += d[nom_prod] * d[nom_qty]
    d['ressource_actuelle'] += prod_totale
    d['ressource_total'] += prod_totale