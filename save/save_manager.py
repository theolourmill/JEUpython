import os
import json
# 1. On définit le nom du dossier et du fichier
FOLDER_NAME = "data"
FILE_NAME = "sauvegarde.json"

# 2. On crée le chemin complet vers le fichier
# os.path.join s'assure que le chemin marche sur Windows, Mac et Linux
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, FOLDER_NAME)
FILE_PATH = os.path.join(DATA_FOLDER, FILE_NAME)

def sauvegarder(donnees):
    # "Sécurité" : Si le dossier data n'existe pas, on le crée
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
        
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(donnees, f, indent=4)
    

def charger(donnees_par_defaut):
    # On vérifie si le fichier existe au chemin complet
    if not os.path.exists(FILE_PATH):
        return donnees_par_defaut
    
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)