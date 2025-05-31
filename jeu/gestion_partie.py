
class GestionPartie:
    def __init__(self):
        self.jeu = Partie()
        self.controleur = Controleur(self.jeu)
        self.tour_croupier = TourCroupier(self.jeu, self.controleur)

    def restart(self):
        self.jeu.nouvelle_partie()
        self.controleur = Controleur(self.jeu)
        self.tour_croupier = TourCroupier(self.jeu, self.controleur)
        self.controleur.tour_joueur_fini = False
        self.controleur.tour_croupier_fini = False
        self.controleur.jeu_fini = False
         self.controleur.message_jeu_fini = ""