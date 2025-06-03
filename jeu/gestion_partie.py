from jeu.controleur import Controleur
from jeu.tour_croupier import TourCroupier
from jeu.paquet import Paquet
from jeu.tirage import Tirage
class GestionPartie:
    def __init__(self):
        self.partie = None
        self.controleur = None
        self.tour_croupier = None

    def nouvelle_partie(self):
        self.partie = Tirage()
        self.partie.compteur.mise_a_j_valeur_main(self.partie)
        self.controleur = Controleur(self.partie)
        self.tour_croupier = TourCroupier(self.partie, self.controleur)