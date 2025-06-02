
from .paquet import Paquet
from .compteur import Compteur

class Tirage:
    def __init__(self):
        self.joueur = []
        self.croupier = []
        self.compteur = Compteur()
        self.paquet = Paquet()

        for _ in range(2):
            self.tirer_carte_joueur()
            self.tirer_carte_croupier()

    def afficher_valeurs(self):
        print(f"Main Croupier: {self.compteur.valeur_croupier}")
        print(f"Main Joueur: {self.compteur.valeur_joueur}")

    def  tirer_carte_joueur(self):
        carte = self.paquet.tirer()
        self.joueur.append(carte)
        self.compteur.mise_a_j_valeur_main(self)

    def  tirer_carte_croupier(self):
        carte = self.paquet.tirer()
        self.croupier.append(carte)
        self.compteur.mise_a_j_valeur_main(self)
