import random
from .cartes import Carte
#*1 paquet de 52 cartes
class Paquet:
    def __init__(self):
        couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
        valeurs = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "As"]
        #Liste cartes
        self.cartes = []
        #Boucles imbriquées pour valeurs sur les x4couleurs
        for couleur in couleurs:
            for valeur in valeurs:
                self.cartes.append(Carte(valeur, couleur))
        random.shuffle(self.cartes)

    def style_carte(self, carte):
        if carte.couleur in["Coeur", "Carreau"]:
            return{"color": (255, 0, 0)}
        return{"color": (0,0,0)}

    def tirer(self):
        return self.cartes.pop()