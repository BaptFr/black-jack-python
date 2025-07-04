from .compteur import Compteur
from .tour_croupier import TourCroupier

class Controleur:
    def __init__(self, partie):
        self.partie = partie
        self.tour_joueur_fini = False
        self.stand_joueur = False
        self.tour_croupier_fini = False
        self.stand_croupier = False
        self.jeu_fini = False
        self.message_jeu_fini = " "
        #Main en cours pour gérer split:
        self.index_main_joueur = 0
        self.tour_croupier = TourCroupier(partie, self)


    def controle_blackJack(self):
         #main en cours
        valeur_main = self.partie.compteur.valeur_joueur[self.index_main_joueur]
        valeur_croupier = self.partie.compteur.valeur_croupier
        if valeur_main == 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = " BLACKJACK - VOUS AVEZ GAGNÉ"
        elif valeur_croupier == 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = "Le croupier a un BLACKJACK - VOUS AVEZ PERDU"

    #Contrôle fin de jeu
    def controle_fin_jeu(self):
        nombre_mains = len(self.partie.joueur) #POur gérer multiple mains du Split

        #contrôle dépassement Index si Split
        if self.index_main_joueur >= nombre_mains:
            print("[DEBUG] Index main joueur hors limite dans controle_fin_jeu")
            return
        valeur_main = self.partie.compteur.valeur_joueur[self.index_main_joueur]
        valeur_croupier = self.partie.compteur.valeur_croupier

        if valeur_main > 21:
            if self.index_main_joueur == nombre_mains - 1:
                self.tour_joueur_fini = True
                self.tour_croupier_fini = True
                self.jeu_fini = True
                self.message_jeu_fini = " Au dessus de 21 - VOUS AVEZ PERDU"
            else:
                self.index_main_joueur +=1
        elif valeur_main == 21:
            if self.index_main_joueur == nombre_mains - 1:
                self.tour_joueur_fini = True
                self.tour_croupier.en_cours = True
            else:
                self.index_main_joueur += 1
        # Cas : le joueur "Stand"
        elif self.stand_joueur:
            if self.index_main_joueur == nombre_mains - 1:
                self.tour_joueur_fini = True
                self.tour_croupier.en_cours = True
            else:
                self.index_main_joueur += 1
                self.stand_joueur = False

        # Comparaison des scores (après stands)
        if self.stand_croupier and self.stand_joueur and self.index_main_joueur == nombre_mains - 1:
            self.jeu_fini = True
            valeur_main_finale = valeur_main
            if valeur_main_finale > valeur_croupier:
                self.message_jeu_fini = f"Vous avez une meilleur main - VOUS AVEZ GAGNÉ"
            elif valeur_main_finale < valeur_croupier:
                self.message_jeu_fini = f"Le croupier a une meilleur main -VOUS AVEZ PERDU"
            else:
                self.message_jeu_fini = f"ÉGALITÉ"
                
        if self.tour_joueur_fini and not self.tour_croupier.en_cours:
            self.tour_croupier.demarrer()
        # Cas : Le croupier Bust
        if valeur_croupier > 21:
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = "Le croupier a dépassé 21 - VOUS AVEZ GAGNÉ"
        elif valeur_croupier == 21:
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = " VOUS AVEZ PERDU"

        if self.jeu_fini:
            print(self.message_jeu_fini)
