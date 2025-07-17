from jeu.controleur import Controleur
from jeu.tour_croupier import TourCroupier
from jeu.tour_joueur import TourJoueur
from jeu.tirage import Tirage
class GestionPartie:
    def __init__(self):
        self.partie = None
        self.controleur = None
        self.tour_croupier = None

    def nouvelle_partie(self, mise_initiale=50):
        if self.partie and self.partie.solde < mise:
            print("Solde insuffisant")
            return False
        self.partie = Tirage()
        self.partie.solde -= mise_initiale
        self.partie.mises = [mise_initiale]
        self.partie.compteur.mise_a_j_valeur_main(self.partie)
        self.controleur = Controleur(self.partie)
        self.tour_croupier = TourCroupier(self.partie, self.controleur)
        self.tour_joueur = TourJoueur(self.partie, self.controleur)
        self.controleur.tour_joueur = self.tour_joueur
        #Contrôle ?BlackJack
        self.controleur.controle_blackJack()

    def placer(self, montant, index_main=0):
        if montant <= self.partie.solde:
            self.partie.mises[index_main] = montant
            self.partie.solde -= montant
            return True
        return False