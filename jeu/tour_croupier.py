
class TourCroupier:
    def __init__(self, jeu, controleur):
        self.jeu = jeu
        self.controleur = controleur

    def action_croupier_etape(self):
        if  self.jeu.compteur.valeur_croupier < 16:
            print("le croupier tire")
            self.jeu.tirer_carte_croupier()
            self.jeu.compteur.mise_a_j_valeur_main(self.jeu)

        else:
            print("le croupier reste")
            self.controleur.tour_croupier_fini =True
            self.controleur.stand_croupier = True
            self.controleur.controle_fin_jeu()