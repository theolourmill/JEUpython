import sys
import os
# Ajoute le dossier parent au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config

def cout_machine():
    cout= config.dict_ressource["cout-base-machine"]*1.3**config.dict_ressource['machine']
    return cout
def cout_machinelv2():
    cout= config.dict_ressource["cout-base-machinelv2"]*1.35**config.dict_ressource['machinelv2']
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

def production_machine():
    config.dict_ressource['ressource_actuelle']+=0.3*config.dict_ressource['machine']
    config.dict_ressource['ressource_total']+=0.3*config.dict_ressource['machine']

def production_machinelv2():
    config.dict_ressource['ressource_actuelle']+=2.5*config.dict_ressource['machinelv2']
    config.dict_ressource['ressource_total']+=2.5*config.dict_ressource['machinelv2']
