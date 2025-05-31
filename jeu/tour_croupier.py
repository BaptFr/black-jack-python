import pygame
class TourCroupier:
    def __init__(self, jeu, controleur):
        self.jeu = jeu
        self.controleur = controleur
        self.derniere_action = pygame.time.get_ticks()
        self.etape_terminee = False

    def action_croupier_etape(self):
        now = pygame.time.get_ticks()
        while  self.jeu.compteur.valeur_croupier < 16:
            print("le croupier tire")
            self.jeu.tirer_carte_croupier()
            self.jeu.compteur.mise_a_j_valeur_main(self.jeu)

        print("le croupier reste")
        self.controleur.tour_croupier_fini =True
        self.controleur.stand_croupier = True
        self.controleur.controle_fin_jeu()
        self.etape_terminee = True
