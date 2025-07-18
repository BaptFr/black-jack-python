from jeu.controleur import Controleur
from jeu.tour_croupier import TourCroupier
from jeu.tour_joueur import TourJoueur
from jeu.tirage import Tirage
from jeu.paquet import Paquet
from jeu.compteur import Compteur
class GestionPartie:
    def __init__(self):
        self.partie = None
        self.controleur = None
        self.tour_croupier = None
        self.tour_joueur = None

    def nouvelle_partie(self, mise_initiale=None):
        solde_actuel = self.partie.solde if self.partie else 1000

        if mise_initiale is not None:
            if mise_initiale > solde_actuel:
                print("Mise trop élevée")
                return False

        if self.partie is None:
            self.partie = Tirage(solde=solde_actuel - mise_initiale)
        else:
            self.partie.joueur = [[]]
            self.partie.croupier = []
            self.partie.mises = [mise_initiale]
            self.partie.paquet = Paquet()
            self.partie.compteur = Compteur()
        if mise_initiale is not None:
            if mise_initiale > self.partie.solde:
                print("Solde insuffisant")
                return False
            self.partie.mises = [mise_initiale]
        else:
            self.partie.mises = [100]

        self.partie.compteur.mise_a_j_valeur_main(self.partie)

        self.controleur = Controleur(self.partie)
        self.tour_croupier = TourCroupier(self.partie, self.controleur)
        self.tour_joueur = TourJoueur(self.partie, self.controleur)
        self.controleur.tour_joueur = self.tour_joueur

        #Contrôle ?BlackJack
        self.controleur.controle_blackJack()
        if self.controleur.jeu_fini:
                self.controleur.regler_mises()
        print(self.controleur.message_jeu_fini)
        return True

    def placer(self, montant, index_main=0):
        if montant <= self.partie.solde:
            self.partie.mises[index_main] = montant
            self.partie.solde -= montant
            return True
        return False