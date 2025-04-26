import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"


class Paquet:
    #Création paquet de cartes x52
    def __init__(self):
        couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
        valeurs = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "As"]
        #Liste cartes
        self.cartes = []
        #Boucles imbriquées pour valeurs sur les x4couleurs
        for couleur in couleurs:
            for valeur in valeurs:
                self.cartes.append(Carte(valeur, couleur))
        #mélange aléat. liste
        random.shuffle(self.cartes)

    #Style des cartes (pygame rgba)
    def style_carte(self, carte):
        if carte.couleur in["Coeur", "Carreau"]:
            return{"color": (255, 0, 0)}
        return{"color": (0,0,0)} #else
    # Fonction tirage d'une carte
    def tirer(self):
        return self.cartes.pop()



class Compteur:
    def __init__(self):
        self.valeur_joueur= 0
        self.valeur_croupier = 0
        self.valeurs_cartes = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "V": 10, "D": 10, "R": 10, "As": 11
        }
    def calcul_valeur_main(self, main):
        total_main = 0
        for carte in main:
            #d'abord reprendre valeur (string)
            valeur = carte.valeur
            #utiliser la conversion en int
            total_main = total_main + self.valeurs_cartes[valeur]
        return total_main

    def mise_a_j_valeur_main(self, jeu):
        self.valeur_joueur = self.calcul_valeur_main(jeu.joueur)
        self.valeur_croupier = self.calcul_valeur_main(jeu.croupier)


class Jeu:
    #contient les mains
    def __init__(self):
        self.joueur = []
        self.croupier = []
        self.compteur = Compteur()

    def afficher_valeurs(self):
        print(f"Main Croupier: {self.compteur.valeur_croupier}")
        print(f"Main Joueur: {self.compteur.valeur_joueur}")

