import pygame
class TourCroupier:
    def __init__(self, jeu, controleur):
        self.jeu = jeu
        self.controleur = controleur
        self.delai = 1000 # Délai tirage
        self.dernier_tirage = 0
        self.en_cours = False

    def demarrer(self):
        self.en_cours = True
        self.dernier_tirage = pygame.time.get_ticks()

    def mise_a_jour(self):
        """Appelée à chaque frame pendant que le tour du croupier est actif"""
        if not self.en_cours:
            return

        maintenant = pygame.time.get_ticks()

        if self.jeu.compteur.valeur_croupier <= 16:
            if maintenant - self.dernier_tirage > self.delai:
                print("le croupier tire")
                self.jeu.tirer_carte_croupier()
                self.jeu.compteur.mise_a_j_valeur_main(self.jeu)
                self.dernier_tirage = maintenant
        else:
            if maintenant - self.dernier_tirage > self.delai:
                print("le croupier reste")
                self.controleur.tour_croupier_fini =True
                self.controleur.stand_croupier = True
                self.controleur.controle_fin_jeu()
                self.en_cours = False
