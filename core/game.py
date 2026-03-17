import sys
import os
# Ajoute le dossier parent au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
#pour pouvoir parcourir les machines dans une boucle
suffixes = ["", "lv2", "lv3", "lv4", "lv5"]

def cout_machine():
    cout= config.dict_ressource["cout-base-machine"]*1.3**config.dict_ressource['machine']
    return cout
def cout_machinelv2():
    cout= config.dict_ressource["cout-base-machinelv2"]*1.35**config.dict_ressource['machinelv2']
    return cout
def cout_machinelv3():
    cout= config.dict_ressource["cout-base-machinelv3"]*1.38**config.dict_ressource['machinelv3']
    return cout 
def cout_machinelv4():
    cout= config.dict_ressource["cout-base-machinelv4"]*1.41**config.dict_ressource['machinelv4']
    return cout
def cout_machinelv5():
    cout= config.dict_ressource["cout-base-machinelv5"]*1.44**config.dict_ressource['machinelv5']
    return cout

def ajouter_ressource():
    config.dict_ressource['ressource_actuelle']+=1
    config.dict_ressource['ressource_total']+=1
    
def ajouter_machine():
    a= cout_machine()
    print(a)
    if config.dict_ressource['ressource_actuelle']<a :
        pass
    else :
        config.dict_ressource['machine']+=1
        config.dict_ressource['ressource_actuelle']-=a

def ajouter_machinelv2():
    a= cout_machinelv2()
    print(a)
    if config.dict_ressource['ressource_actuelle']<a :
        pass
    else :
        config.dict_ressource['machinelv2']+=1
        config.dict_ressource['ressource_actuelle']-=a
def ajouter_machinelv3():
    a= cout_machinelv3()
    print(a)
    if config.dict_ressource['ressource_actuelle']<a :
        pass
    else :
        config.dict_ressource['machinelv3']+=1
        config.dict_ressource['ressource_actuelle']-=a
def ajouter_machinelv4():
    a= cout_machinelv4()
    print(a)
    if config.dict_ressource['ressource_actuelle']<a :
        pass
    else :
        config.dict_ressource['machinelv4']+=1
        config.dict_ressource['ressource_actuelle']-=a
def ajouter_machinelv5():
    a= cout_machinelv5()
    print(a)
    if config.dict_ressource['ressource_actuelle']<a :
        pass
    else :
        config.dict_ressource['machinelv5']+=1
        config.dict_ressource['ressource_actuelle']-=a

def production_machine():
    prod_totale=0
    d=config.dict_ressource
    for s in suffixes:
        nom_prod = f"prod_base_machine{s}"
        nom_qty = f"machine{s}"
        prod_totale += d[nom_prod] * d[nom_qty]
    d['ressource_actuelle'] += prod_totale
    d['ressource_total'] += prod_totale