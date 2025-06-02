from jeu.controleur import Controleur
from jeu.tour_croupier import TourCroupier
from jeu.paquet import Paquet
from jeu.tirage import Tirage
class GestionPartie:
    def __init__(self):
        self.partie = Tirage()
        self.controleur = Controleur(self.partie)
        self.tour_croupier = TourCroupier(self.partie, self.controleur)

    def nouvelle_partie(self):
        self.partie = Tirage()
        self.partie.compteur.mise_a_j_valeur_main(self.partie)
        self.controleur = Controleur(self.partie)
        self.tour_croupier = TourCroupier(self.partie, self.controleur)
        self.controleur.tour_joueur_fini = False
        self.controleur.tour_croupier_fini = False
        self.controleur.jeu_fini = False
        self.controleur.message_jeu_fini = ""