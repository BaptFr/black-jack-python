import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

class Paquet:
    def __init__(self):
        couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
        valeurs = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "As"]
        #Liste cartes
        self.cartes = []

        #Création paquet de cartes x52
        for couleur in couleurs:
            for valeur in valeurs:
                self.cartes.append(Carte(valeur, couleur))
        #mélange alétaoire liste
        random.shuffle(self.cartes)

    def style_carte(self, carte):
        if carte.couleur in["Coeur", "Carreau"]:
            return{"bg": "red", "fg": "white"}



    def tirer(self):
        return self.cartes.pop()

class Jeu:
    def __init__(self):
        self.joueur = []
        self.croupier = []
